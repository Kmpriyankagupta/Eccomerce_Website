from django import template
from math import floor

register = template.Library()
@register.simple_tag
def calculate_stars(rating):
    """
    Calculate the number of full, half, and empty stars based on the rating.
    """
    try:
        # Ensure the rating is a float
        rating = float(rating)
    except ValueError:
        rating = 0  # Default to 0 if conversion fails
    print('rate',rating)
    # Calculate the number of full stars
    full_stars = int(rating)  # Integer part only

    # Check for a half star
    fractional_part = rating - full_stars
    half_stars = 1 if 0.25 <= fractional_part < 0.75 else 0  # Half star if between 0.25 and 0.75

    # Adjust empty stars to ensure a total of 5 stars
    empty_stars = 5 - full_stars - half_stars

    # Ensure we don't exceed the limit of 5 stars
    if full_stars + half_stars > 5:
        full_stars = 5
        half_stars = 0
        empty_stars = 0
    print('star',{
        "full_stars": full_stars,
        "half_stars": half_stars,
        "empty_stars": empty_stars,
    }
    )
    return {
        "full_stars": full_stars,
        "half_stars": half_stars,
        "empty_stars": empty_stars,
    }
    
@register.filter
def range_filter(value):
    """
    Returns a range object up to the given value.
    """
    return range(value)