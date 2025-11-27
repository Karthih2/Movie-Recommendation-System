from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
import pickle
import difflib

app = Flask(__name__)

# Load the movie recommendation models
with open('English_Movie_Recommendation.pkl', 'rb') as file:
    movies_en, cosin_sim_en = pickle.load(file)


TMDB_API_KEY = 'YOUR_API_KEY' #API key


def get_movie_details(movie_name):
    """Fetches movie details from TMDB API based on movie name."""
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}&language=en-US'
    try:
        response = requests.get(search_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['results']:
            movie_id = data['results'][0]['id']
            return fetch_movie_details(movie_id)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")

    # Default details if movie not found
    return {
        "title": "Movie not found",
        "genre": "N/A",
        "rating": "N/A",
        "synopsis": "N/A",
        "poster_url": 'path/to/default_image.jpg',
        "trailer_url": "#"
    }


def fetch_movie_details(movie_id):
    """Fetches additional details for a specific movie ID."""
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US&append_to_response=videos,credits'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "title": data.get("title", "Title not available"),
            "genre": ", ".join([genre['name'] for genre in data.get("genres", [])]) or "Genre not available",
            "rating": data.get("vote_average", "Rating not available"),
            "synopsis": data.get("overview", "Synopsis not available"),
            "poster_url": f"https://image.tmdb.org/t/p/w500{data.get('poster_path', '')}" if data.get('poster_path') else 'path/to/default_image.jpg',
            "trailer_url": f"https://www.youtube.com/watch?v={data.get('videos', {}).get('results', [{}])[0].get('key', 'not found') if data.get('videos', {}).get('results') else 'not found'}",
            "cast": ", ".join([cast['name'] for cast in data.get('credits', {}).get('cast', [])[:5]]) or "Cast not available",
            "director": next((crew['name'] for crew in data.get('credits', {}).get('crew', []) if crew['job'] == "Director"), "Director not available"),
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")
        return {
            "title": "Movie not found",
            "genre": "N/A",
            "rating": "N/A",
            "synopsis": "N/A",
            "poster_url": 'path/to/default_image.jpg',
            "trailer_url": "#"
        }


def get_close_title(title, movie_titles):
   #closing matching
    close_matches = difflib.get_close_matches(title.lower(), movie_titles.str.lower(), n=1, cutoff=0.6)
    return close_matches[0] if close_matches else None


def get_recommendation(title):
    #Recommendation based on tags(Genre,Director,Actor/Actress)
    close_title = get_close_title(title, movies_en['MovieName'])
    if not close_title:
        return [{"title": "Movie not found"}]

    idx = movies_en[movies_en['MovieName'].str.lower() == close_title].index[0]
    sim_scores = list(enumerate(cosin_sim_en[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]  # Exclude the movie itself
    movie_indices = [i[0] for i in sim_scores]

    recommended_movies = []
    for idx in movie_indices:
        movie_detail = get_movie_details(movies_en['MovieName'].iloc[idx])
        recommended_movies.append(movie_detail)

    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    title = None  # Initialize title to None

    if request.method == 'POST':
        title = request.form.get('title')  # Get the title entered by the user
        if title:
            recommendations = get_recommendation(title)  # Fetch recommendations based on the title

    # Pass both recommendations and title to the template
    return render_template('index.html', recommendations=recommendations, title=title)



@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query', '').strip().lower()  # Strip whitespace and convert to lowercase
    if not query:
        return jsonify([])  # Return an empty list if no query is provided

    movie_titles = movies_en['MovieName'].str.lower().tolist()  # Convert to lowercase list once
    suggestions = difflib.get_close_matches(query, movie_titles, n=5, cutoff=0.5)

    return jsonify(suggestions)

@app.route('/trending')
def trending_movies():
    #Trending movies
    trending_url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}'
    try:
        response = requests.get(trending_url, timeout=5)
        response.raise_for_status()
        movies = response.json().get('results', [])
        trending_movies = [fetch_movie_details(movie['id']) for movie in movies]
        return jsonify(trending_movies)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trending movies: {e}")
        return jsonify([])


if __name__ == '__main__':
    app.run(debug=True)
