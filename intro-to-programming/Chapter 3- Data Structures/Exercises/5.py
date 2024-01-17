
guests = ['Taylor Swift', 'Matthew Perry', 'Kim Namjoon']
#List of guest to invite 

#Print the guest names for dinner
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nUnfortunately, {name} can't make it to dinner.")

#Name of guest not going to come
del(guests[1])
guests.insert(1, 'Katy Perry')

#Output of invitation again.
name = guests[0].title()
print(f"\n{name}, come to the dinner.")

name = guests[1].title()
print(f"{name}, come to the dinner.")

name = guests[2].title()
print(f"{name}, come to the dinner.")