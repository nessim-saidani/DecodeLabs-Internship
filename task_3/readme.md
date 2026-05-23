# Project 3: AI Recommendation Logic

## Movie Recommendation System

---

## Overview

This project implements a simple AI recommendation system that suggests movies based on user genre preferences. The system uses similarity matching to calculate how closely each movie aligns with the user's interests.

**Project Focus:** Pattern Alignment and Similarity Logic

---

## Project Goals

1. Take user input (genre preferences)
2. Match preferences using similarity logic
3. Display recommended movies ranked by relevance

---

## Key Concepts

### Recommendation Systems

A recommendation system is an algorithm that suggests items (movies, products, songs) to users based on their preferences or behavior.

### Similarity Matching

Comparing user preferences with item attributes to find the best matches.

### Similarity Score

A numerical value (0 to 1) representing how well an item matches user preferences.

**Formula:**
```
Similarity Score = (Matching Genres) / (Total User Genres)

Example:
User wants: Action, Sci-Fi (2 genres)
Movie has: Action, Sci-Fi, Thriller (3 genres)
Matches: 2 (Action and Sci-Fi)
Score = 2/2 = 1.0 (100% match)
```

---

## How It Works

### Step 1: Get User Input

```python
user_input = input("what genre of movies do you like (comma seperated): ").split(",")
user_genre = [genre.strip() for genre in user_input]
```

User enters: `Action, Sci-Fi, Thriller`
Result: `['Action', 'Sci-Fi', 'Thriller']`

### Step 2: Calculate Match Scores

For each movie in the database:
- Compare user genres with movie genres
- Count how many match
- Calculate percentage

**Example:**
```
User genres: [Action, Sci-Fi]
Movie "The Matrix": [Action, Sci-Fi, Thriller]
Matches: Action (yes), Sci-Fi (yes)
Score: 2/2 = 1.0 (100%)

Movie "The Notebook": [Romance, Drama]
Matches: Action (no), Sci-Fi (no)
Score: 0/2 = 0.0 (0%)
```

### Step 3: Filter and Sort

- Keep only movies above minimum score (0.2 = 20%)
- Sort by score (highest first)
- Display to user

### Step 4: Display Results

```
we recommend you the following movies:
1. The Matrix with a score of 100.0%
2. Avengers with a score of 100.0%
3. Inception with a score of 50.0%
```

---

## Project Structure

```
Project_3_Recommendation/
├── recommendation_system.py  # Main recommendation script
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

---

## Installation

### Requirements

- Python 3.6 or higher
- No external libraries required (uses only built-in Python)

### Setup

1. Download the script:
```bash
git clone <repository-url>
cd Project_3_Recommendation
```

2. Ensure Python is installed:
```bash
python --version
```

3. No additional packages needed - ready to run!

---

## Usage

### Run the Program

```bash
python recommendation_system.py
```

### Example Interaction

```
welcome to the ai recommendation system
what genre of movies do you like (comma seperated): Action, Sci-Fi
You prefer: ['Action', 'Sci-Fi'] movies
we recommend you the following movies:
The Matrix with a score of 100.0%
Avengers with a score of 100.0%
Inception with a score of 50.0%
Interstellar with a score of 50.0%
The Dark Knight with a score of 50.0%
```

---

## Code Explanation

### Movie Database

```python
movies = {
    "The Matrix": ["Action", "Sci-Fi", "Thriller"],
    "Inception": ["Sci-Fi", "Thriller", "Mystery"],
    ...
}
```

Dictionary mapping movie names to their genres (attributes).

### calculate_match Function

```python
def calculate_match(user_genre, movie):
    """
    Calculate match percentage between user preferences and movie genres
    """
    matches = 0
    for i in user_genre:
        for j in movie:
            if i.lower() == j.lower():  # Case-insensitive comparison
                matches += 1
    
    if len(user_genre) == 0:
        pourcentage = 0
    else:
        pourcentage = matches / len(user_genre)
    
    return pourcentage
```

**What it does:**
- Compares each user genre with each movie genre
- Counts total matches
- Calculates percentage (matches / user_genres)
- Returns score between 0 and 1

**Example:**
```
Input: user_genre = ['Action', 'Sci-Fi'], movie = ['Action', 'Sci-Fi', 'Thriller']
Process: 
  - Check 'Action': found in movie = 1 match
  - Check 'Sci-Fi': found in movie = 2 matches
Output: 2/2 = 1.0 (100%)
```

### get_recommendations Function

```python
def get_recommendations(user_genres, movies_db, min_score=0.2):
    """
    Find and rank movie recommendations
    """
    recommendations = {}
    
    # Calculate score for each movie
    for movie_name, movie_genres in movies_db.items():
        score = calculate_match(user_genres, movie_genres)
        
        # Only include if score meets minimum
        if score >= min_score:
            recommendations[movie_name] = score
    
    # Sort by score (highest first)
    recommendations_sorted = sorted(
        recommendations.items(),
        key=lambda item: item[1],
        reverse=True
    )
    
    return recommendations_sorted
```

**What it does:**
- Loops through all movies
- Calculates match score for each
- Filters movies below minimum score (0.2)
- Sorts by score in descending order
- Returns ranked list

### affichage Function

```python
def affichage(recommendation):
    """
    Display recommendations to user
    """
    print("we recommend you the following movies: ")
    
    if not recommendation:
        print("sorry we couldn't find any movie that match your preferences")
    else:
        for movie in recommendation:
            print(movie[0], "with a score of ", movie[1]*100, "%")
```

**What it does:**
- Checks if recommendations exist
- Shows message if no matches
- Prints each movie with score

---

## Available Genres in Database

1. Action
2. Animation
3. Comedy
4. Crime
5. Drama
6. Mystery
7. Romance
8. Sci-Fi
9. Thriller

---

## Sample Input and Output

### Input 1: Action and Sci-Fi
```
User Input: Action, Sci-Fi
Output:
The Matrix with a score of 100.0%
Avengers with a score of 100.0%
Inception with a score of 50.0%
Interstellar with a score of 50.0%
The Dark Knight with a score of 50.0%
```

### Input 2: Romance
```
User Input: Romance
Output:
Forrest Gump with a score of 100.0%
The Notebook with a score of 100.0%
```

### Input 3: Comedy, Animation
```
User Input: Comedy, Animation
Output:
Toy Story with a score of 100.0%
Deadpool with a score of 50.0%
```

### Input 4: Jazz, Classical (No Matches)
```
User Input: Jazz, Classical
Output:
sorry we couldn't find any movie that match your preferences
```

---

## Algorithm Analysis

### Time Complexity

```
O(m * u * g)

Where:
m = number of movies
u = number of user genres
g = average genres per movie

For this dataset: 10 movies, max 3 user inputs, 3 genres per movie
= 10 * 3 * 3 = 90 operations (very fast)
```

### Space Complexity

```
O(m)

Stores recommendations for all movies
For this dataset: 10 movies = minimal memory
```

---

## Parameters Explanation

### min_score (Minimum Score Threshold)

Controls which movies are recommended.

**Default:** `0.2` (20%)

**Effects:**
- `min_score=0.0`: Show all movies
- `min_score=0.2`: Show movies with 20%+ match
- `min_score=0.5`: Show movies with 50%+ match
- `min_score=1.0`: Show only 100% matches

**Example:**
```python
# Only show perfect matches
recommendations = get_recommendations(user_genre, movies, min_score=1.0)

# Show any match
recommendations = get_recommendations(user_genre, movies, min_score=0.0)
```

---

## How to Modify

### Add More Movies

```python
movies["Interstellar"] = ["Sci-Fi", "Drama"]
movies["Parasite"] = ["Drama", "Thriller"]
movies["Joker"] = ["Crime", "Drama", "Thriller"]
```

### Change Minimum Score

```python
# More strict (only best matches)
recommendation = get_recommendations(user_genre, movies, 0.5)

# More lenient (show more options)
recommendation = get_recommendations(user_genre, movies, 0.0)
```

### Add New Genres

Simply use them in movie definitions:
```python
movies["Avatar"] = ["Action", "Sci-Fi", "Adventure"]
```

---

## Enhancements and Extensions

### Enhancement 1: Add Movie Ratings

```python
movies_extended = {
    "The Matrix": {
        "genres": ["Action", "Sci-Fi", "Thriller"],
        "rating": 8.7,
        "year": 1999
    },
    ...
}
```

### Enhancement 2: Add Weighted Scoring

```python
# Some genres more important than others
genre_weights = {
    "Action": 2.0,
    "Comedy": 1.5,
    "Drama": 1.0
}
```

### Enhancement 3: User Rating Feedback

```python
def rate_recommendation(movie, rating):
    print(f"You rated {movie}: {rating}/5 stars")
    # Store for future learning
```

### Enhancement 4: Show Why It Matched

```python
def show_matching_genres(user_genres, movie_genres):
    matches = [g for g in user_genres if g in movie_genres]
    print(f"Matched genres: {matches}")
```

### Enhancement 5: Top N Recommendations

```python
def get_top_n_recommendations(user_genres, movies_db, n=3, min_score=0.2):
    """Return only top N recommendations"""
    all_recs = get_recommendations(user_genres, movies_db, min_score)
    return all_recs[:n]
```

---

## Common Issues and Solutions

### Issue 1: Case Sensitivity

**Problem:** "action" doesn't match "Action"

**Solution:** Already implemented with `.lower()`
```python
if i.lower() == j.lower():
    matches += 1
```

### Issue 2: Whitespace in Input

**Problem:** "Action " (with space) doesn't match "Action"

**Solution:** Already implemented with `.strip()`
```python
user_genre = [genre.strip() for genre in user_input]
```

### Issue 3: No Matches Found

**Problem:** User genres don't exist in database

**Solution:** Happens when no movies have even one matching genre

**Fix:** Lower the minimum score or add more genres

### Issue 4: Typos in Input

**Problem:** User types "Sic-Fi" instead of "Sci-Fi"

**Solution:** Show available genres first or implement fuzzy matching

---

## Skills Demonstrated

### Programming Skills
- Function definition and organization
- Dictionary data structures
- List comprehension and iteration
- String manipulation (lower, strip, split)
- Conditional logic
- Sorting with lambda functions
- Input/output operations

### Algorithm Skills
- Similarity calculation
- Pattern matching
- Scoring systems
- Data filtering
- Sorting algorithms
- Ranking systems

### Recommendation System Skills
- Content-based filtering
- Similarity metrics
- User preference analysis
- Item ranking
- Result presentation

---

## Learning Outcomes

Upon completing this project, you understand:

1. How recommendation systems work
2. Content-based filtering approach
3. Similarity calculation between profiles
4. Ranking and scoring mechanisms
5. Data filtering and sorting
6. User preference matching
7. Algorithm complexity analysis
8. How to extend recommendation logic

---

## Real-World Applications

### Netflix
- Recommends movies/shows based on watched content
- Uses similar algorithms to match user preferences

### Amazon
- Recommends products based on purchase history
- Matches customer preferences with product attributes

### Spotify
- Recommends songs based on listening history
- Matches user taste with song characteristics

### YouTube
- Recommends videos based on viewing history
- Suggests content based on interests

---

## Performance Metrics

### Dataset Size
- Movies: 10
- Genres: 9
- Processing time: Milliseconds

### Scalability

For larger datasets:
```
100 movies: Still instant
1,000 movies: Still instant
100,000 movies: May need optimization
1,000,000 movies: Requires caching/indexing
```

---

## Contact Information

DecodeLabs Industrial Training Kit
Batch: 2026

Phone: +91 89330 06408
Email: decodelabs.tech@gmail.com
Website: www.decodelabs.tech
Location: Greater Lucknow, India

---

## Version History

- Version 1.0 (May 2026): Initial project completion
  - Movie recommendation system with genre matching
  - Similarity score calculation
  - Ranked recommendations
  - Minimum score filtering

---

## Notes

- Case-insensitive genre matching
- Whitespace automatically handled
- No external dependencies required
- Fast execution on dataset
- Easily expandable to more movies
- Ready for enhancement with additional features

---

## Troubleshooting

### Issue: No output after entering genres

**Solution:** Make sure you press Enter after typing genres

### Issue: All movies shown even unwanted ones

**Solution:** Increase min_score parameter
```python
recommendation = get_recommendations(user_genre, movies, 0.5)
```

### Issue: No movies recommended

**Solution:** Lower min_score or check genre spelling
```python
recommendation = get_recommendations(user_genre, movies, 0.0)
```

---

End of Project 3 Documentation