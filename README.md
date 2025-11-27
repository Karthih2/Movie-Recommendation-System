<h1 align="center">🎬 <b>Movie Recommendation System</b></h1>

<div align="center">

<img src="https://raw.githubusercontent.com/Karthih2/Movie-Recommendation-System/main/Movie-Recommendation-System%20Home.png" alt="Movie Recommendation System" style="width:100%;height:auto;display:block">

<br><br>

<!-- Badges -->

<a><img src="https://img.shields.io/badge/Python-3.8+-0A9EDC?logo=python&logoColor=white"></a> <a><img src="https://img.shields.io/badge/Flask-3.0.3-black?logo=flask&logoColor=white"></a> <a><img src="https://img.shields.io/badge/Pandas-2.2.2-150458?logo=pandas&logoColor=white"></a> <a><img src="https://img.shields.io/badge/Numpy-2.0.1-013243?logo=numpy&logoColor=white"></a> <a><img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn&logoColor=white"></a> <a><img src="https://img.shields.io/badge/TMDB-API-01d277?logo=themoviedatabase&logoColor=white"></a> <a><img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter"></a> <a><img src="https://img.shields.io/badge/License-MIT-green"></a>

---

### ⭐ **An Content-Based Movie Recommendation System powered by Flask, Machine Learning, and the TMDB API**

</div>

---

## 📌 **Overview**

This project is a **content-based movie recommendation web application** that analyzes movie metadata (genre, cast, director, keywords) and provides **accurate similarity-based movie recommendations**.
The system integrates with the **TMDB API** to fetch movie posters, trailers, and trending movies.

### 🔥 **Highlights**

* 🎯 **Content-Based Recommendation Engine**
* 🧠 **Cosine Similarity + TF-IDF Vectorization**
* 🔍 **Smart Auto-Complete Search (Fuzzy Matching)**
* 🎥 **TMDB Posters, Details, and Trailers**
* 📱 **Responsive UI with Smooth Animations**
* ⚡ **Fast — <100ms Recommendation Time**

---

## 📁 **Project Structure**

```
movie-recommendation-system/
│
├── static/
│   └── This is cinema.png
│
├── templates/
│   └── index.html
│
├── English_movies.csv
├── model.ipynb
├── movie_rec_app.py
├── requirements.txt
├── LICENSE
├── CITATION.cff
└── README.md
```

---

## 🛠 **Tech Stack**

### 🔹 Backend

* Python 3.8+
* Flask 3.0.3
* Pandas, NumPy
* Scikit-Learn
* TMDB API

### 🔹 Frontend

* HTML5, CSS3
* JavaScript (ES6)
* Font Awesome

### 🔹 ML Components

* TF-IDF Vectorizer
* Cosine Similarity Matrix
* Pickled Model (`English_Movie_Recommendation.pkl`)

---

## 🚀 **Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### **2️⃣ Create Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # macOS/Linux
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Add TMDB API Key**

Edit inside `movie_rec_app.py`:

```python
TMDB_API_KEY = "YOUR_API_KEY"
```

### **5️⃣ Run the App**

```bash
python movie_rec_app.py
```

### **6️⃣ Open in Browser**

```
http://127.0.0.1:5000
```

---

## 🎯 **Usage**

### 🔎 Get Movie Recommendations

* Type a movie name
* Choose from the auto-suggestions
* Receive top 10 similar movies
* View posters, cast, synopsis, trailers

### 🔽 API Endpoints

#### Suggestions

```
GET /suggest?query=dark
```

#### Recommendations

```
POST /
title=Inception
```

#### Trending Movies

```
GET /trending
```

---

## 📊 **Model Details**

### 🧠 **Algorithm: Content-Based Filtering**

* Combined **genre + cast + director + keywords** into a single feature string
* Converted features into vectors using **TF-IDF**
* Computed pairwise similarities using **Cosine Similarity**

### 🏎 Performance

| Metric               | Value                        |
| -------------------- | ---------------------------- |
| Recommendation Speed | **< 100ms**                  |
| Dataset              | 5000+ English movies         |
| Accuracy             | Based on metadata similarity |


## 🤝 Contributing

Contributions are **welcome**!

```bash
git checkout -b feature/YourFeature
git commit -m "Add Your Feature"
git push origin feature/YourFeature
```

Please follow:

* PEP8 standards
* Clear documentation
* Meaningful commit messages

### Future Enhancements

* [ ] Add collaborative filtering
* [ ] User login + watchlists
* [ ] Rating-based recommendations
* [ ] Multi-language movie dataset
* [ ] Cloud deployment


## 🔖 **Repository Tags**

`#machine-learning` `#flask` `#movies` `#recommendation-system`
`#tmdb` `#python` `#content-based-filtering`

---

## 📬 **Contact**

**Your Name**
📧 [Email](h2karthi04@gmail.com)
🌐 [GitHub](https://github.com/Karthih2)

---

<div align="center">

### ⭐ *If you found this project useful, consider giving it a star!*

<img src="https://img.shields.io/github/stars/yourusername/movie-recommendation-system?style=social">

</div>
