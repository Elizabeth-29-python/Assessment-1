pets = []

pet = {
    'animal type': 'dog',
    'name': 'caramel',
    'owner': 'elizah',
    'weight': 4,
    'eats': 'plushies',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'niki',
    'owner': 'jillian',
    'weight': 4,
    'eats': 'fish treats',
}
pets.append(pet)

pet = {
    'animal type': 'hamster',
    'name': 'eunice',
    'owner': 'denise',
    'weight': 1,
    'eats': 'seads',
}
pets.append(pet)

# this will display the information of the pets.
for pet in pets:
    print(f"\nWhat I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")