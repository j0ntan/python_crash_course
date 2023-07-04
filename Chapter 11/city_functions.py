def get_formatted_city(city, country, population=''):
    """Generate a neatly formatted city."""
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted
