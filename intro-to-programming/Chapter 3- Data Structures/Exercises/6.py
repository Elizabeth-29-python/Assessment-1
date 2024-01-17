#Invitation to guest
guests = ['Taylor Swift', 'Kim Namjoon', 'Matthew Perry']

name = guests[0].title()
print(f"{name}, come to the dinner.")

name = guests[1].title()
print(f"{name}, come to the dinner.")

name = guests[2].title()
print(f"{name}, come to the dinner.")

name = guests[1].title()
print(f"\nSadly, {name} can't make it to dinner.")

# Matthew Perry my guest won't come.
del(guests[2])
guests.insert(1, 'Katy Perry')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to the dinner.")

name = guests[1].title()
print(f"{name}, please come to the dinner.")

name = guests[2].title()
print(f"{name}, please come to the dinner.")

# I ordered a bigger table to invite for more guests 
print("\nWe got a bigger table!")
guests.insert(0, 'Emma Stone')
guests.insert(2, 'Ryan Reynolds')
guests.append('IU')

name = guests[0].title()
print(f"{name}, come to my dinner.")

name = guests[1].title()
print(f"{name}, come to my dinner.")

name = guests[2].title()
print(f"{name}, come to my dinner.")

name = guests[3].title()
print(f"{name}, come to my dinner.")

name = guests[4].title()
print(f"{name}, come to my dinner.")

name = guests[5].title()
print(f"{name}, come to my dinner.")

# There was a problem with the delivery, Invitation got short
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"My biggest apologies, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"My biggest apologies, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"My biggest apologies, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"My biggest apologies, {name.title()} there's no room at the table.")

# Only 2 people can be invited 
name = guests[1].title()
print(f"{name}, please come to the dinner.")

name = guests[0].title()
print(f"{name}, please come to the dinner.")

# Emptying out the list
del(guests[0])
del(guests[0])

# Output of empty list
print(guests)