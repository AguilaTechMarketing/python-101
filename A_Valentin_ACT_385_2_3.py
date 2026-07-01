# Alejandro Valentin
# GLAB 385.2.3 - Dictionary Exercises
# Date: 2026 June

# Problem 1: Create a dictionary utilizing the provided city & states
print("Problem 1: Create a dictionary utilizing city & states")
# Tasks
# Create a dictionary object using curly brace {} notation, where the states are the keys and the capitals are the values.
# Create a dictionary object using the built-in dict() function, where the states are the keys and the capitals are the values.
# Use the type() function to check the data type of each dictionary.
# Print each dictionary to display all key-value pairs.
print("")
print("step 1: create a dictionary using {}")
# Step 1: Create a dictionary using {}, where the states are keys and cities are values
states_capitals = {
    "California": "Los Angeles",
    "New York": "Albany",
    "Hawaii": "Honolulu",
    "Alaska": "Juneau",
    "Texas": "Austin"
}
print("States & Capitals Dictionary:", states_capitals)
print("")
print("---------")
# Step 2: Create a dictionary using dict(), where states are keys and cities are values
print("step 2: create a dictionary using dict()")
states_cities = dict([
    ("California", "Los Angeles"),
    ("New York", "Albany"),
    ("Hawaii", "Honolulu"),
    ("Alaska", "Juneau"),
    ("Texas", "Austin")
])
print("States & Cities Dictionary:", states_cities)
print("")
print("---------")
# Step 3: Use type() to check the data type of each dictionary
print("step 3: check data types of each dictionary")
print("Data Type of states_capitals:", type(states_capitals))
print("")
print("Data Type of states_cities:", type(states_cities))
print("")
print("!*---------*!")
# Problem 2 
print("Problem 2: Dictionary Manipulation")
# Tasks
# Retrieve the value associated with the key "California".
# Add a new key-value pair for Florida and its capital to the dictionary.
# Update the value for "California" to "Sacramento".
# Remove the key-value pair for "Alaska" from the dictionary.
# Step 1: Retrieve the value of California
print("step 1: retrieve the value of California")
print("Listed Capital of California:", states_capitals.get("California"))
print("")
print("---------")
# Step 2 Update the value of "California"
print("step 2: update the value of California")
states_capitals["California"] = "Sacramento"
print("Update California Capital:", states_capitals)
print("")
print("---------")
# Step 3: add new key-value for Florida
print("step 3: add new key-value for Florida")
states_capitals["Florida"] = "Tallahassee"
print("Florida Added:", states_capitals)
print("")
print("---------")
# Step 4: Remove Alaska from the dictionary
print("step 4: remove Alaska from the dictionary")
del states_capitals["Alaska"]
print("Final Dictionary, All Steps Complete:", states_capitals)
print("")
print("!*---------*!")
# Problem 3: Using Dictionary Methods & for loops
print("Problem 3: Using Dictionary Methods & for loops")
# step 1: Create the playlist dictionary
print("step 1: create playlist dictionary")
playlist = {
    "Mark Anthony": "Vivir Mi Vida",
    "Frank Sinatra": "My Way",
    "Frankie Negron": "La Cura",
    "Nina Simone": "Feeling Good",
    "Bad Bunny": "Monaco",
    "Hozier": "Too Sweet",
    "Rauw Alejandro": "Tu Con El",
    "Teddy Swims": "Dose",
}
print(playlist)
print("")
print("---------")
# step 2: Loop to print all artists (keys)
print("step 2: loop to print all artists")
print("--- Artists ---")
for artist in playlist.keys():
    print(artist)
print("")
print("---------")
# step 3: loop to print all songs (values)
print("step 3: loop to print all songs")
print("\n--- songs ---")
for song in playlist.values():
    print(song)
print("")
print("---------")
# step 4: loop to print the formatted statement
print("step 4: loop to print formatted statement")
print("\n--- Formatted List ---")
for artist, song in playlist.items():
    print(f"{song} by {artist} is in the current playlist.")
print("")
print("---------")
# step 5: remove the last key-value pair (.popitem())
removed_item = playlist.popitem()
print(f"\nRemoved last item: {removed_item}")
print("")
print("Playlist after removed last item:", playlist)
print("")
print("---------")
# step 6: Add "Anti-Hero" by Taylor Swift
print("step 6: add 'Anti-Hero' by Taylor Swift")
playlist["Taylor Swift"] = "Anti-Hero"
print("")
print("Playlist after additional song added:", playlist)
print("")
print("---------")
# step 7: update one song so that titles begins with remix
print("step 7: Update song title")
playlist["Rauw Alejandro"] = "Remix - Tu Con El"
print("")
print("Playlist after title update:", playlist)
print("")
print("---------")
# step 8: Define a function to print all entries
def display_playlist(music_dict):
    print("\n--- Final Updated Playlist ---")
    for artist, song in music_dict.items():
        print(f"Artist: {artist}, | Song: {song}")
display_playlist(playlist)
print("")
print("---------Fin---------")

      

