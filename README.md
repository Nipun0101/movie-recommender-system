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
