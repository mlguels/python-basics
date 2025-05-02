names = ["Andres", "Mathew", "John"]

# Lists can be a mixure of different data types
my_favorite_things = ["working out", 7, ["Inner list"]]

print(names)
print(my_favorite_things[2][0])

# Unlike strings, lists are mutable
names[0] = "Andrew"

print(names)

# Copying data
"""
When assigning a list to another variable
the new variable is just another reference to the same list
so it will not copy the list but poin to the same list 
using a differnet variable
"""
colors = ["red", "blue", "green"]
colors2 = colors
colors[0] = "yellow"
print(colors)

"""
In order to copy a list you can slice 
"""

"""
This is just a shallow copy
which means the copy points to the same data
"""
my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]
my_favorite_things2 = my_favorite_things.copy();

#modify the original
my_favorite_things[2][0] = "Audible"
print(my_favorite_things2) #CONTAINS AUDIBLE 


# to make a deep copy use the deepcopy method
import copy
my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]
my_favorite_things2 = copy.deepcopy(my_favorite_things)
#modify the original
my_favorite_things[2][0] = "Audible"
print(my_favorite_things2) #CONTAINS NETFLIX
