# Using list constructor
my_list1 = list((1,2,3))
print(my_list1)

# Using square brackets[]
my_list2 = [1,2,3]
print(my_list2)

# with heterogeneous items
my_list3 = [1.0, 'Jessa', 3]
print(my_list3)

# empty list using list()
my_list4 = list()
print(my_list4)

# empty list using []
my_list5 = []
print(my_list4)

#length of a list
my_list6 = [1,2,3]
print(len(my_list6))

#list indexing
my_list = [10, 20, 'Jessa', 12.50, 'Emma']
# accessing 2nd element of the list
print(my_list[1])  
# accessing 5th element of the list
print(my_list[4])  

# accessing last element of the list
print(my_list[-1])

# accessing second last element of the list
print(my_list[-2])

# accessing 4th element from last
print(my_list[-4])

#list slicing
#listname[start_index : end_index : step]
my_list7 = [10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
# Extracting a portion of the list from 2nd till 5th element
print(my_list7[2:5])

my_list8 = [5, 8, 'Tom', 7.50, 'Emma']

# slice first four items
print(my_list8[:4])
# Output [5, 8, 'Tom', 7.5]

# print every second element
# with a skip count 2
print(my_list8[::2])
# Output [5, 'Tom', 'Emma']

# reversing the list
print(my_list8[::-1])
# Output ['Emma', 7.5, 'Tom', 8, 5]

# Without end_value
# Stating from 3nd item to last item
print(my_list8[3:])
# Output [7.5, 'Emma']

#iterating a list
my_list9 = [5,8,'Tom', 7.50, 'Emma']
for i in my_list9:
    print(i)

#Iterate along with an index number
my_list10 = [5, 8, 'Tom', 7.50, 'Emma']

# iterate a list
for i in range(0, len(my_list10)):
    # print each item using index number
    print(my_list10[i])

#adding element to the list
#append item at the end of the list
my_list11 = [5,8,'Tom', 7.50]
#using append()
my_list11.append('Emma')
print(my_list11)
# Output [5, 8, 'Tom', 7.5, 'Emma']
# append the nested list at the end
my_list.append([25, 50, 75])
print(my_list)
# Output [5, 8, 'Tom', 7.5, 'Emma', [25, 50, 75]]

#Add item at the specified position in the list
#insert(index, object)
y_list = list([5, 8, 'Tom', 7.50])

# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list)
# Output [5, 8, 25, 'Tom', 7.5]

# insert nested list at at position 3
my_list.insert(3, [25, 50, 75])
print(my_list)
# Output [5, 8, 25, [25, 50, 75], 'Tom', 7.5]

#Using extend()
#The extend method will accept the list of elements and add them at the end of the list. We can even add another list by using this method.
my_list12 = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list.extend([25, 75, 100])
print(my_list12)
# Output [5, 8, 'Tom', 7.5, 25, 75, 100]

#Modify the items of a List
my_list = list([2, 4, 6, 8, 10, 12])

# modify single item
my_list[0] = 20
print(my_list)
# Output [20, 4, 6, 8, 10, 12]

# modify range of items
# modify from 1st index to 4th
my_list[1:4] = [40, 60, 80]
print(my_list)
# Output [20, 40, 60, 80, 10, 12]

# modify from 3rd index to end
my_list[3:] = [80, 100, 120]
print(my_list)
# Output [20, 40, 60, 80, 100, 120]

#modify all item
my_list = list([2, 4, 6, 8])

# change value of all items
for i in range(len(my_list)):
    # calculate square of each number
    square = my_list[i] * my_list[i]
    my_list[i] = square

print(my_list)
# Output [4, 16, 36, 64]

#Remove specific item
my_list13 = list([2, 4, 6, 8, 10, 12])

# remove item 6
my_list13.remove(6)
# remove item 8
my_list13.remove(8)

print(my_list13)
# Output [2, 4, 10, 12]

#Remove item present at given index
#Use the pop() method to remove the item at the given index. The pop() method removes and returns the item present at the given index.
my_list14 = list([2, 4, 6, 8, 10, 12])

# remove item present at index 2
my_list14.pop(2)
print(my_list14)
# Output [2, 4, 8, 10, 12]

# remove item without passing index number
my_list14.pop()
print(my_list14)
# Output [2, 4, 8, 10]

#Remove the range of items
my_list15 = list([2, 4, 6, 8, 10, 12])

# remove range of items
# remove item from index 2 to 5
del my_list15[2:5]
print(my_list15)
# Output [2, 4, 12]

# remove all items starting from index 3
my_list16 = list([2, 4, 6, 8, 10, 12])
del my_list16[3:]
print(my_list16)
# Output [2, 4, 6]

#Finding an element in the list
my_list17 = list([2, 4, 6, 8, 10, 12])

print(my_list17.index(8))
# Output 3
# returns error since the element does not exist in the list.
# my_list.index(100)

#Concatenation of two lists
my_list18 = [1, 2, 3]
my_list19 = [4, 5, 6]

# Using + operator
my_list20 = my_list18 + my_list19
print(my_list20)
# Output [1, 2, 3, 4, 5, 6]

# Using extend() method
my_list18.extend(my_list19)
print(my_list18)
# Output [1, 2, 3, 4, 5, 6]

#Using the copy() method
my_list21 = [1, 2, 3]
# Using copy() method
new_list22 = my_list21.copy()
# printing the new list
print(new_list22)
# Output [1, 2, 3]

# making changes in the original list
my_list21.append(4)

# print both copies
print(my_list21)
# result [1, 2, 3, 4]
print(new_list22)
# result [1, 2, 3]

#also sort(), reverse(), max(), min(), sum(), all(), any()

#Item Values in List	Return Value
#All Values are True -- True
# One or more False Values -- False
# All False Values -- False
# Empty List -- True

# all() function
#with all true values
samplelist1 = [1,1,True]
print("all() All True values::",all(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("all() with One false value ::",all(samplelist2))

#with all false
samplelist3 = [0,0,False]
print("all() with all false values ::",all(samplelist3))

#empty list
samplelist4 = []

#any() function
# Item Values in List -- Return Value
# All Values are True -- True
# One or more False Values -- True
# All False Values -- False
# Empty List -- False

#with all true values
samplelist1 = [1,1,True]
print("any() True values::",any(samplelist1))

#with one false
samplelist2 = [0,1,True,1]
print("any() One false value ::",any(samplelist2))


#with all false
samplelist3 = [0,0,False]
print("any() all false values ::",any(samplelist3))

#empty list
samplelist4 = []
print("any() Empty list ::",any(samplelist4))

# List Comprehension

# List comprehension is a simpler method to create a list from an existing list. 
# It is generally a list of iterables generated with an option to include only the items which satisfy a condition.

# outputList = [expression(variable) for variable in inputList [if variable condition1][if variable condition2]
inputList = [4,7,11,13,18,20]
#creating a list with square values of only the even numbers
squareList = [var**2 for var in inputList if var%2==0]
print(squareList)





