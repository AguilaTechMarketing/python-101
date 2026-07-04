#Alejandro Valentin
# GLAB 385.2.1
# Date: July 2026

# Phase 1: Dictionary Logic
# Sprint 1: Define a dictionary of movies w/ info
movies = {
    "The Usual Suspects": {
        "year": 1995,
        "Genre": "Crime/Thriller",
        "director": "Bryan Singer",
        "actors": ["Kevin Spacey", "Benicio del Toro", "Gabriel Byrne", "Stephen Baldwin", "Chazz Palminteri", "Kevin Pollak", "Pete Postlethwaite"]
    },
    "Reservoir Dogs": {
        "year": 1992,
        "Genre": "Crime/Thriller",
        "director": "Quentin Tarantino",
        "actors": ["Harvey Keitel", "Michael Madsen", "Tim Roth", "Steve Buscemi", "Chris Penn"]
    },
    "The Sixth Sense": {
        "year": 1999,
        "Genre": "Horror/Mystery",
        "director": "M. Night Shyamalan",
        "actors": ["Haley Joel Osment", "Bruce Willis", "Toni Collette", "Donnie Wahlberg"]
    },
    "Sin City": {
        "year": 2005,
        "Genre": "Action/Crime",
        "director": "Frank Miller",
        "actors": ["Mickey Rourke", "Bruce Willis", "Jessica Alba", "Rosario Dawson", "Benicio del Toro"]
    },
    "The Dark Knight": {
        "year": 2008,
        "Genre": "Action/Crime",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"]
    }

}

# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# print("Top 10 Movies Dictionary:", movies)
# ====================================

# Sprint 2: Search by Title
# Step 1: Check if the title exists in the dictionary
# Step 2: Displaying the movie details
def search_by_title(movie_db):
    search_title = input("Enter the movie title to search: ").strip()
    
    if search_title in movie_db:
        print(f"\nMovie found: {search_title}")
        movie_info = movie_db[search_title]
        
        for key, value in movie_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Movie not found in the database.")

# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     search_by_title(movies)
# ====================================

# step 3: Search by Genre
def search_by_genre(movie_db):
    search_genre = input("Enter movie genre to search: ").strip().lower()
    found = False

    print(f"\nSearching for genre: {search_genre}...")
    
    # Iterate through every movie in the database
    for title, info in movie_db.items():
        # Check if the search term is in the movie's Genre value
        if search_genre in info.get("Genre", "").lower():
            print(f"Found: {title} ({info['Genre']})")
            found = True
            
    if not found:
        print("Genre not found in database. Try a new search!")


# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     search_by_genre(movies)
# ====================================

# step 4: Search by Actors
def search_by_actor(movie_db):
    search_actor = input("Enter actor name to search movie list: ").strip().lower()
    found = False

    print(f"\nSearch for actor: {search_actor}...")

    # Iterate through every movie in the database
    for title, info in movie_db.items():
        # Get the list of actors and convert all names to lowercase for matching
        actors_list = [actor.lower() for actor in info.get("actors", [])]
        
        # Check if the search term is in that list
        if search_actor in actors_list:
            print(f"Found: {title} (Actors: {', '.join(info['actors'])})")
            found = True
            
    if not found:
        print("Actor not found in database. Try new search!")

# ====================================
# TEST BLOCK Comment out once verified
# ====================================
# if __name__ == "__main__":
#     search_by_actor(movies)
# ====================================

# Sprint 3: View All and Delete Functions
# View All: Displays all movies and their details View All and Delete Functions.

def view_all_movies(movie_db):
    if not movie_db:
        print("\nThe database is currently empty.")
        return
    
    print("\n--- Current Movie Database ---")
    for title, info in movie_db.items():
        print(f"\nTitle: {title}")
        print(f" Year: {info['year']}")
        print(f" Genre: {info['Genre']}")
        print(f" Director: {info['director']}")
        print(f" Actors: {', '.join(info['actors'])}")
    print("\n-------------------------------------")

# Delete a movie: Removes a movie entry by title

def delete_movie(movie_db):
    """
    Prompts the user for a movie title and removes it from the database if found.
    Includes a confirmation step to prevent accidental deletion.
    """
    title_to_delete = input("\nEnter the title of the movie you want to delete: ").strip()
    
    # Check if the title exists in the dictionary
    if title_to_delete in movie_db:
        confirm = input(f"Are you sure you want to delete '{title_to_delete}'? (y/n): ").strip().lower()
        
        if confirm == 'y':
            del movie_db[title_to_delete]
            print(f"Success: '{title_to_delete}' has been removed from the database.")
        else:
            print("Action cancelled. No changes were made.")
    else:
        print(f"Error: '{title_to_delete}' not found in the database. Please check the spelling and try again.")

# ====================================
# TEST BLOCK: Verify View All and Delete
# ====================================
if __name__ == "__main__":
    # 1. Show the database before deleting
    print("\n--- TEST: VIEW ALL ---")
    view_all_movies(movies)
    
    # 2. Test the delete function
    print("\n--- TEST: DELETE MOVIE ---")
    delete_movie(movies)
    
    # 3. Show the database after deleting to verify the change
    print("\n--- TEST: VERIFY DELETION ---")
    view_all_movies(movies)
# ====================================


