movies = {
    "The Matrix": ["Action", "Sci-Fi", "Thriller"],
    "Inception": ["Sci-Fi", "Thriller", "Mystery"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "Deadpool": ["Action", "Comedy"],
    "Avengers": ["Action", "Sci-Fi"],
    "The Notebook": ["Romance", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Toy Story": ["Comedy", "Animation"]
}

#calculate match pourcentage function
def calculate_match(user_genre,movie):
    matches=0
    for i in user_genre:
        for j in movie:
            if i.lower() == j.lower():
                matches+=1
    if len(user_genre) == 0:
        pourcentage=0
    else: 
        pourcentage=matches/len(user_genre)
    return pourcentage


def get_recommendations(user_genres, movies_db, min_score=0.2):
    recommendations = {}
    
    for movie_name, movie_genres in movies_db.items():  
        score = calculate_match(user_genres, movie_genres) 
        
        if score >= min_score:
            recommendations[movie_name] = score
    #sorting the result 
    recommendations_sorted = sorted(recommendations.items(),key=lambda item: item[1],reverse=True)
    return recommendations_sorted


def affichage(recommendation):
    print("we recommend you the following movies : ")
    if not recommendation :
        print("sorry we couldn't find any movie that match your preferences")
    
    else :
        for movie in recommendation :
            print(movie[0], "with a score of ", movie[1]*100, "%")


#main 

#this is an ai recommendation system for movies
print("welcome to the ai recommendation system ")
user_input=input("what genre of movies do you like (comma seperated)   ").split(",")
user_genre=[genre.strip() for genre in user_input]
print ("You prefer : ",user_genre , "movies")
recommendation=get_recommendations(user_genre,movies,0.2)
affichage(recommendation)
