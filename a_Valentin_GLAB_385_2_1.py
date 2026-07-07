# GLAB 385.2.1
# Working with List & Functions in Python

# Example 1: List Manipulation
print("====================================")
print("LIST MANIPULATION:")
print("====================================")
print("")
print("Define list:")
# 1. Define a list
# Creating a list with mixed data types
tools = ["Laptop", "Monitor", "Keyboard", "Mouse"]
print("Original Tool List", tools)
print("")
# 2. Indexing & Slicing
print("Indexing & Slicing")
print("Indexing:")
# Accessing elements by position (0-based)
print("Find Element at Index 0:")
print("Index [0] = ", tools[0])
print("")
print("Find Element at Index -1 or last position")
print("Index [-1] = ",tools[-1])
print("")

# Slicing: [Start : Stop] - Note: Stop index is exclusive
print("Slicing:")
sub_List = tools[1:3]
print("Print Elements at Index [1] & [3] and name it 'Sub List'.")
print("Sub List =", sub_List)
print("")

# 3. Modifying Elements
# Changing a value at a specific index
print("Modify Elements:")
tools[2] = "Webcam"
print("Add Webcam to index 2 in list")
print(tools)
print("")

# 4. Adding Elements
# Use append() to add to the end ot the list
print("Adding Elements:")
tools.append("Desk")

# Use insert() to add at a specific index
tools.insert(1, "Headphones")
print(".append('Desk') will add 'Desk' to end of list; & .insert(1, 'Headphones') will add 'Headphones' to index [1]")
print("After Appending:", tools)
print("")

# 5. Removing Elements
print("Removing Elements")
# Use remove() to delete a specific value by name
tools.remove("Monitor")
print(".remove('Monitor') removes 'Monitor' from list")
print("After removal:", tools)
print("")

# 6. Checking Length
print("Checking length")
# Using the len() function to see total count
total_items = len(tools)
print("this, 'total_items = len(tools)', tells how many elements are in the list")
print(total_items)
print("")

print("Copy vs Creating Referencing")
# Copying lists vs creating references in Python
# Creating a reference (NOT a Copy)
print("")
print("Reference:")
# This does not copy a list
print("Creating a New Reference")
print("")
original_list = [1, 2, 3]
print(original_list)
print("")

# new_reference points to the same list object
new_reference = original_list
print(new_reference)
print("")
print("After .append() 'new_reference adding the ")
# Modify the list through the new reference
new_reference.append(4)
print("OG")
print("Original List:", original_list)
print("NR")
print("New Reference:", new_reference)
print("Boolean statement:")
print("Is 'OG' equal to 'NR'", original_list == new_reference)
print("")

# Properly copying a list using the .copy() method
print("Copy:")
print("")
original_list = ["A", "B", "C"]

copied_list = original_list.copy()

# Modify the copy list
copied_list.append(4)
print("OG")
print("Original List:", original_list)
print("Copy")
print("Copied List:", copied_list)
print("Boolean statement:")
print("Is 'OG' equal to 'Copy'?", original_list == copied_list)
print("")

# Variables reference the same list
# if two variables reference the same list, modifying one will also modify the other
print("Reference:")
print("")
furniture_list1 = ["table", "chair", "lamp"]

# this creates another reference not a copy
furniture_list_append = furniture_list1

furniture_list_append.append("armoire")
print("")
print("---FURNITURE---")
print(furniture_list1)
print("---FURNITURE APPEND---")
print(furniture_list_append)
print("")

# Example 2: Using .reverse() & .extend() methods

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]
print("")
print("Recent First", recent_first)
print("Recent Last", recent_last)
print("")
def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in chronological order
    recent_first.reverse()
    print("After Reversing Recent First:", recent_first)
    print("")

    # extend the "recent_last" list by appending the newly reversed "recent_first" list
    recent_last.extend(recent_first)

    #  return the "recent_last", which now contains the two lists combined in chronological order
    return recent_last

#  call the record_profit_years()
print("")

print("Record Profit Years", record_profit_years(recent_first, recent_last))