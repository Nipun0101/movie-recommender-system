# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Machine Learning and Streamlit.

The system recommends movies similar to the selected movie using cosine similarity.

---

## Live Demo
https://movie-recommender-system-hrgv3svzlnrkujhsnrjjyl.streamlit.app/

---

## Features
• Content-based movie recommendation  
• Movie posters fetched using TMDB API  
• Interactive Streamlit interface  
• Fast recommendations using precomputed similarity matrix  

---

## Tech Stack
Python  
Pandas  
Scikit-learn  
Streamlit  
TMDB API  

---

## Project Structure

app.py – Streamlit web application

movie-recommender-system.ipynb – Model training notebook

movies_dict.pkl – Movie dataset

similarity.pkl – Precomputed similarity matrix

requirements.txt – Python dependencies

---

## Run Locally

pip install -r requirements.txt

streamlit run app.py


## App Preview
<img width="1916" height="948" alt="Screenshot 2026-03-17 222005" src="https://github.com/user-attachments/assets/d2db236d-b76b-4a6b-82b5-96eb5688143c" />

## How It Works

The system uses a content-based filtering approach.
Movies are converted into vectors using text features like genres, keywords, and cast.
Cosine similarity is then used to find movies that are most similar to the selected movie.

## Note

The similarity matrix is precomputed and stored as similarity.pkl (compressed to fit GitHub limits).




