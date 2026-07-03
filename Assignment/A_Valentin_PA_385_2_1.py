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

# Sprint 2a: Search by Title
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

