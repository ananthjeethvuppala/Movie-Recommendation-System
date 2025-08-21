# Content-Based Movie Recommendation System
# Dataset: TMDB 5000 Movies + Credits

import pandas as pd
import numpy as np
import re
import ast
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (run once)
nltk.download("punkt")
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge on id
movies = movies.merge(credits, left_on="id", right_on="movie_id")
movies = movies[["title_x", "genres", "keywords", "overview", "cast", "crew"]]
movies = movies.rename(columns={"title_x": "title"})

# Function to extract names from JSON-like fields
def extract_names(x):
    try:
        data = ast.literal_eval(x)
        return " ".join([d["name"] for d in data])
    except:
        return ""

# Function to get top 5 cast members
def extract_cast(x, top_n=5):
    try:
        data = ast.literal_eval(x)
        return " ".join([d["name"] for d in data[:top_n]])
    except:
        return ""

# Function to get director name
def extract_director(x):
    try:
        data = ast.literal_eval(x)
        directors = [d["name"] for d in data if d.get("job") == "Director"]
        return " ".join(directors)
    except:
        return ""

# Text preprocessing
def preprocess_text(text):
    text = re.sub(r"[^a-zA-Z\s]", " ", str(text))
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Apply feature extraction
movies["genres"] = movies["genres"].apply(extract_names)
movies["keywords"] = movies["keywords"].apply(extract_names)
movies["cast"] = movies["cast"].apply(extract_cast)
movies["crew"] = movies["crew"].apply(extract_director)

# Combine features
movies["combined"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"].astype(str) + " " +
    movies["cast"] + " " +
    movies["crew"]
)

# Clean combined text
movies["cleaned_text"] = movies["combined"].apply(preprocess_text)

# Vectorization using TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies["cleaned_text"])

# Cosine similarity between movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movies(movie_name, top_n=5):
    idx = movies[movies["title"].str.lower() == movie_name.lower()].index
    if len(idx) == 0:
        return f"Movie '{movie_name}' not found"
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices][["title"]]

# Example
if __name__ == "__main__":
    print("Recommendations for The Dark Knight:")
    print(recommend_movies("The Dark Knight"))
