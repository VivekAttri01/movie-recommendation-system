import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YTQwZGRiZjEzMjVhZTRiOTk3MWY1ZTMyZjQzMDYzYSIsInN1YiI6IjY1YjhlZDZjOGMzMTU5MDE3YmYyNTBkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Mo8975n1s_3fz7y8oH9BKIxBkoSQ3DZayp3BfJey3Rg"
    }

    response = requests.get(url, headers=headers)
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]
    recommended_movies_posters=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].id
        #fetch movie poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters

# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list= movies_list['title'].values
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox(
#     "How would you like to be contacted?",
#     movies_list)

selected_movie_name  = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])