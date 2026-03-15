# Movie Recommender System

A content-based movie recommendation system built using Machine Learning and Streamlit.

## Features
- Recommend movies based on similarity
- Built using cosine similarity
- Interactive web app using Streamlit

## Tech Stack
- Python
- Pandas
- Scikit-Learn
- Streamlit

## Run Locally

Clone the repository

git clone https://github.com/Nipun0101/movie-recommender-system

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

## Model Files

The file `similarity.pkl` is not included in the repository because it exceeds GitHub's 100MB file size limit.

To generate it, run the notebook:

movie-recommender-system.ipynb

This will create:

similarity.pkl

The application loads this file to compute movie recommendations.
