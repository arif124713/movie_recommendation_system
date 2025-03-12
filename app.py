import pickle
import streamlit as st
import requests

# Set page config for dark theme
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #ff5c8d;
        }
        .movie-name {
            font-size: 16px;
            font-weight: bold;
            color: #ff5c8d;
        }
        .recommend-button {
            background-color: #ff5c8d;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .recommend-button:hover {
            background-color: #ff3399;
        }
        .stImage {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        }
    </style>
    """, unsafe_allow_html=True
)

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')  # Handle missing posters
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750?text=Error"


# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# Streamlit App
st.markdown('<h1 class="title">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)

# Load Data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie Selection
movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Select a movie:", movie_list)

# Show Recommendations
if st.button('Show Recommendations', key="recommend_button"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display movies in 5 columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f'<p class="movie-name">{recommended_movie_names[i]}</p>', unsafe_allow_html=True)
            # Use st.markdown to add image with custom class
            st.markdown(f'<img src="{recommended_movie_posters[i]}" class="stImage" style="width:100%"/>', unsafe_allow_html=True)
