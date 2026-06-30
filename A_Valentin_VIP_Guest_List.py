# Alejandro Valentin
# VIP Guest List Manager

# Initial Guest List
guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Initial List:", guests)

# 1. Add Frank to the end
# Using .append()
guests.append("Frank")

# 2. Add Grace to the front
# using .insert() at index 0
guests.insert(0, "Grace")
# verify addition
print("verify add", guests)

# 3. Replace Charlie w/ Chuck
# 1st find Charlies index
target = "Charlie"
# verify if "Charlie" in list
if target in guests:
    charlie_index = guests.index(target)
    # print index to see in bash
    print(f"Charlie was found at index: {charlie_index}")
    # use index to replace "Charlie" w/ "Chuck"
    guests[charlie_index] = "Chuck"
else:
    print(f"{target} is not on the guest list")
# verify the update
print(f"Verify change complete: {guests}")

# 4. Remove the person at index 3
guests.remove(guests[3])
# verify index[3] "Chuck" removed
print("Removed index[3]:", guests)

# Print Final results
print("Final List:", guests)
print("Total Guests:", len(guests))




