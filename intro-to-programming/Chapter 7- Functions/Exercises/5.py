def describe_city(city, country='United Arab Emirates'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('abu dhabi')
describe_city('bangkok', 'thailand')
describe_city('dubai')