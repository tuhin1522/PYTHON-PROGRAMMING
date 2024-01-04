book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
if 'Harry Potter' in book_set:
    print("Book exists in the book set")
else:
    print("Book doesn't exist in the book set")
# Output Book exists in the book set

# check another item which is not present inside a set
print("A Man called Ove" in book_set)  
# Output False

book_set1 = {'Harry Potter', 'Angels and Demons'}
# add() method
book_set1.add('The God of Small Things')
# display the updated set
print(book_set1)
# Output {'Harry Potter', 'The God of Small Things', 'Angels and Demons'}

# update() method to add more than one item
book_set1.update(['Atlas Shrugged', 'Ulysses'])
# display the updated set
print(book_set1)
# Output {'The God of Small Things', 'Angels and Demons', 'Atlas Shrugged', 'Harry Potter', 'Ulysses'}

color_set = {'red', 'orange', 'yellow', 'white', 'black'}

# remove single item
color_set.remove('yellow')
print(color_set)
# Output {'red', 'orange', 'white', 'black'}

# remove single item from a set without raising an error
color_set.discard('white')
print(color_set)
# Output {'orange', 'black', 'red'}

color_set.discard('yellow')
print(color_set)
# Output {'red', 'black', 'white', 'orange'}

# remove single item using remove()
color_set.remove('yellow')
print(color_set)
# Output KeyError: 'yellow'

# remove any random item from a set
deleted_item = color_set.pop()
print(deleted_item)

# remove all items
color_set.clear()
print(color_set)
# output set()

# delete a set
del color_set

# Union of sets
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# union of two set using OR operator
vibgyor_colors = color_set | remaining_colors
print(vibgyor_colors)
# Output {'indigo', 'blue', 'violet', 'yellow', 'red', 'orange', 'green'}

# union using union() method
vibgyor_colors = color_set.union(remaining_colors)
print(vibgyor_colors)
# Output {'indigo', 'blue', 'violet', 'yellow', 'red', 'orange', 'green'}

# Intersection of Sets
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# intersection of two set using & operator
new_set = color_set & remaining_colors
print(new_set)
# Output {'indigo'}

# using intersection() method
new_set = color_set.intersection(remaining_colors)
print(new_set)
# Output {'indigo'}

# There are two key differences between intersection() and intersection_update()

#     intersection() will not update the original set but intersection_update() will update the original set with only the common elements.
#     intersection() will have a return value which is the new set with common elements between two or more sets whereas intersection_update() will not have any return value.

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# intersection of two sets
common_colors = color_set.intersection(remaining_colors)
print(common_colors)  # output {'indigo'}
# original set after intersection
print(color_set)
# Output {'indigo', 'violet', 'green', 'yellow', 'blue'}

# intersection of two sets using intersection_update()
color_set.intersection_update(remaining_colors)
# original set after intersection
print(color_set)
# output {'indigo'}

















