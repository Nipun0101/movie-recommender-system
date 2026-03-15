import streamlit as st
import pickle
import pandas as pd
import requests

import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b0d4944ffa137c23c7e1fa16b779c205&language=en-US"
    data = requests.get(url).json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select movie name',movies['title'].values)

if st.button('Recommend'):
    with st.spinner("Finding similar movies..."):
        names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.caption(names[0])
        st.image(posters[0], use_container_width=True)

    with col2:
        st.caption(names[1])
        st.image(posters[1], use_container_width=True)

    with col3:
        st.caption(names[2])
        st.image(posters[2], use_container_width=True)

    with col4:
        st.caption(names[3])
        st.image(posters[3], use_container_width=True)

    with col5:
        st.caption(names[4])
        st.image(posters[4], use_container_width=True)