# 🎬 Movie Recommendation System

This project is a **content-based movie recommender system** built using Python and deployed as a web application. It recommends similar movies based on user input using movie metadata like genres, keywords, cast, and crew.

🚀 **Live Demo (optional)**: *[will be added soon]*  
📁 **Tech Stack**: Python, Pandas, Scikit-learn, Streamlit

---

## 📌 Features

- Search for a movie and get **top 5 similar movies** as recommendations
- Uses **cosine similarity** on vectorized metadata
- Clean and responsive **Streamlit UI**
- Fast and lightweight — no login required

---

## 🧠 How It Works

The system is built using **content-based filtering**, specifically:

1. **Data Preprocessing**:
   - Extracts and combines genres, keywords, cast, and director into a single string
2. **Vectorization**:
   - Applies `CountVectorizer` to convert text into numerical features
3. **Similarity Computation**:
   - Uses **cosine similarity** to measure similarity between movies
4. **Recommendation**:
   - For a given movie, returns the top N most similar titles

---

## 📂 Project Structure

movie-recommendation-system/
├── app.py # Streamlit app
├── movies.csv # Movie metadata
├── similarity.pkl # Precomputed similarity matrix
├── requirements.txt # Required packages
└── README.md # Project documentation


---

## 🛠️ Setup & Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/arif124713/movie_recommendation_system.git
   cd movie_recommendation_system
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
streamlit run app.py

