rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'columbia': 'canada & united states',
    'tigris': 'turkey, syria, and iraq',
    'orinoco': 'south america',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

# the program is arranged with the output of the name of the river and the countries of the rivers.
    