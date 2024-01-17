locations = ['Tbilisi', 'Boracay', 'Seoul', 'Osaka', 'Akihabara']

print("Original order:")
print(locations)
#using Sorted for alphabetical list
print("\nAlphabetical:")
print(sorted(locations))
#using orignal list order
print("\nOriginal order:")
print(locations)
 #using sorted() for reverse alphabetical list output
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))
#show original order
print("\nOriginal order:")
print(locations)
#change the order of your list
print("\nReversed:")
locations.reverse()
print(locations)
#changed list to reverse
print("\nOriginal order:")
locations.reverse()
print(locations)
#list so it’s stored in alphabetical order and changed
print("\nAlphabetical")
locations.sort()
print(locations)
#changed list to reverse 
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)