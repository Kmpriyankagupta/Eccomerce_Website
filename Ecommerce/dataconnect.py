import sqlite3
import psycopg2
from psycopg2 import sql

# SQLite database file
sqlite_db_path = 'D:\eccommerce_website\Eccomerce_Website\db.sqlite3'

# PostgreSQL connection details
postgres_config = {
    'dbname': 'Ecommerce',
    'user': 'priyanka',
    'password': '1234',
    'host': 'localhost',
    'port': 5432,
   
}

def migrate_table(table_name, sqlite_db_path, postgres_config):
    try:
        # Connect to SQLite
        sqlite_conn = sqlite3.connect(sqlite_db_path)
        sqlite_cursor = sqlite_conn.cursor()
        
        # Connect to PostgreSQL
        postgres_conn = psycopg2.connect(**postgres_config)
        postgres_cursor = postgres_conn.cursor()

        # Get SQLite table schema
        sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
        columns_info = sqlite_cursor.fetchall()
        if not columns_info:
            print(f"Table '{table_name}' does not exist in SQLite database.")
            return

        columns = [col[1] for col in columns_info]  # Extract column names
        
        # Drop table in PostgreSQL if it exists
        postgres_cursor.execute(sql.SQL("DROP TABLE IF EXISTS {table_name}").format(
            table_name=sql.Identifier(table_name)
        ))

        # Create table in PostgreSQL
        create_table_query = f"CREATE TABLE {table_name} ("
        for col in columns_info:
            create_table_query += f"{col[1]} {map_sqlite_to_postgres_type(col[2])}, "
        create_table_query = create_table_query.rstrip(", ") + ");"
        postgres_cursor.execute(create_table_query)

        # Fetch all data from SQLite table
        sqlite_cursor.execute(f"SELECT * FROM {table_name};")
        rows = sqlite_cursor.fetchall()

        # Insert data into PostgreSQL
        for row in rows:
            placeholders = ', '.join(['%s'] * len(row))
            insert_query = sql.SQL(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})")
            postgres_cursor.execute(insert_query, row)

        # Commit changes and close connections
        postgres_conn.commit()
        sqlite_conn.close()
        postgres_conn.close()

        print(f"Table '{table_name}' migrated successfully.")

    except Exception as e:
        print(f"Error while migrating table '{table_name}': {e}")

def map_sqlite_to_postgres_type(sqlite_type):
    """Map SQLite types to PostgreSQL types."""
    type_mapping = {
        'TEXT': 'TEXT',
        'INTEGER': 'INTEGER',
        'REAL': 'REAL',
        'BLOB': 'BYTEA',
        'NUMERIC': 'NUMERIC',
    }
    return type_mapping.get(sqlite_type.upper(), 'TEXT')  # Default to TEXT if unknown

if __name__ == "__main__":
    # Specify the table you want to migrate
    table_name = 'eapp_categories'
    migrate_table(table_name, sqlite_db_path, postgres_config)
