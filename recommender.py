# Adapted from shyam1998/Movie-Recommendation-System-GUI (MIT).
# Retains the CSV -> CountVectorizer -> cosine_similarity -> title lookup pipeline.
# Simplified to genres only; adds optional genre filtering and explicit seed exclusion.
import csv
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with Path(__file__).with_name("movies.csv").open(newline="") as file:
    movies = list(csv.DictReader(file))
titles_list = [movie["title"] for movie in movies]
genres_list = sorted({g for movie in movies for g in movie["genres"].split()})
cv = CountVectorizer()
dtm = cv.fit_transform([movie["genres"] for movie in movies])
similarities = cosine_similarity(dtm)

def get_movie_data():
    return titles_list

def get_recommendations(title, genre=""):
    if genre and genre not in genres_list:
        raise ValueError("Please select a genre from the list.")
    title = title.strip().lower()
    idx = next((i for i, movie in enumerate(movies)
                if movie["title"].lower() == title), None)
    if idx is None:
        raise ValueError("Please select a movie from the list.")
    ranked = sorted(range(len(movies)), key=lambda i: (-similarities[idx, i], i))
    recommendations = []
    for i in ranked:
        if i == idx or similarities[idx, i] <= 0:
            continue
        if genre and genre not in movies[i]["genres"].split():
            continue
        recommendations.append(movies[i])
        if len(recommendations) == 5:
            break
    return recommendations
