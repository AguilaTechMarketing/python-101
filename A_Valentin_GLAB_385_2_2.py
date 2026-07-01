# Alejandro Valentin
# GLAB 385.2.2 - Python Dictionary Manipulation
# Date: 2026_June

# *-Example 1-* Python Dictionaries Manipulation:

# 1. Define a dictionary
student_info = {
    "name": "Alice",
    "age": 21,
    "course": "Data Science",
    "is_enrolled": True
}

# 2. Accessing Values
print(student_info["name"])
print("")
# Use .get() to prevent errors if key doesn't exist
print(student_info.get("age"))
print("")
# 3. Modify and add elements
# update an existing value
student_info["age"] = 22
print("updated age:", student_info["age"])
print("")
# Adding a new key value pair
student_info["grade"] = "A"
print("Original Dictionary", student_info)
print("")
# 4. Removing elements
# using delete to remove specific key
del student_info["is_enrolled"]
print("Verify Deletion:", student_info)
print("")
# Using .pop() to remove a key & return its value
removed_course = student_info.pop("course")
print(f"Removed: {removed_course}")
print("After removing elements:", student_info)
print("")
# 5. Common Dictionary Methods
# accessing all keys, values, or items (pairs)
print(student_info.keys())
print(student_info.values())
print("")
# the .items()
print(student_info.items())
print("")
# example of using .items() in a loop
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")
    print("")

# *-Example 2-* Using Dictionary Methods:

# The network() function accepts a dictionary "servers" as a parameter.
def network(servers):
    # A string variable is initialized to hold the "result".
    results = ""
    # For each "hostname" (key) and "IP address" (value) in the "server" dictionary items
    for hostname, IP_address in servers.items():
        #.items() returns all key-value pairs in a dictionary.Each pair is returned as a tuple:
       results += "The IP address of the  {} server is {}".format(hostname, IP_address) + "\n"
        # Return the "result" variable string.
    return results
# Call the "network" function with dictionary
print(network({"Domain Name Server":"8.8.8.8",
               "Gateway Server":"192.168.1.1",
               "Print Server":"192.168.1.33",
               "Mail Server":"192.168.1.190"}))

