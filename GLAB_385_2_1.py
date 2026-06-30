# GLAB 385.2.1
# Working with List & Functions in Python

# Example 1: List Manipulation

# 1. Define a list
# Creating a list with mixed data types
tools = ["Laptop", "Monitor", "Keyboard", "Mouse",]

# 2. Indexing & Slicing
# Accessing elements by position (0-based)
print(tools[0])
print(tools[-1])

# Slicing: [Start : Stop] - Note: Stop index is exclusive
sub_List = tools[1:3]
print(sub_List)

# 3. Modifying Elements
# Changing a value at a specific index
tools[2] = "Webcam"
print(tools)

# 4. Adding Elements
# Use append() to add to the end ot the list
tools.append("Desk")

# Use insert() to add at a specific index
tools.insert(1, "Headphones")
print(tools)

# 5. Removing Elements
# Use remove() to delete a specific value by name
tools.remove("Monitor")
print(tools)

# 6. Checking Length
# Using the len() function to see total count
total_items = len(tools)
print(total_items)

# Copying lists vs creating references in Python
# Creating a reference (NOT a Copy)

# This does not copy a list

original_list = [1, 2, 3]

# new_reference points to the same list object
new_reference = original_list

# Modify the list through the new reference
new_reference.append(4)

print("Original List:", original_list)
print("New Reference:", new_reference)
print(original_list == new_reference)

# Properly copying a list using the .copy() method

original_list = ["A", "B", "C"]

copied_list = original_list.copy()

# Modify the copy list
copied_list.append(4)

print("Original List", original_list)
print("Copied List:", copied_list)
print(original_list == copied_list)

# Variables reference the same list
# if two variables reference the same list, modifying one will also modify the other

furniture_list1 = ["table", "chair", "lamp"]

# this creates another reference not a copy
furniture_list_append = furniture_list1

furniture_list_append.append("armoire")
print("---FURNITURE---")
print(furniture_list1)
print("---FURNITURE APPEND---")
print(furniture_list_append)

# Example 2: Using .reverse() & .extend() methods

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in chronological order
    recent_first.reverse()

    # extend the "recent_last" list by appending the newly reversed "recent_first" list
    recent_last.extend(recent_first)

    #  return the "recent_last", which now contains the two lists combined in chronological order
    return recent_last

#  call the record_profit_years()
print(record_profit_years(recent_first, recent_last))