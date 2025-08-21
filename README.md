# 🎬 Movie Recommendation System  

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) 
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) 
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) 
![NLTK](https://img.shields.io/badge/NLTK-NLP-brightgreen?style=for-the-badge) 
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) 
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) 
![Dataset](https://img.shields.io/badge/Dataset-TMDB%205000-orange?style=for-the-badge) 
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge&logo=github)  

---

This project is a **Content-Based Movie Recommendation System** built using the **TMDB 5000 Movies + Credits dataset**.  
It uses **Natural Language Processing (NLP)** and **TF-IDF Vectorization** to recommend movies similar to a given one.  

---

## 🚀 Features 

- 📂 Uses **TMDB 5000 Movies + Credits dataset**  
- 📝 Preprocesses movie metadata (**genres, keywords, overview, cast, crew**)  
- 🔎 Recommends top N similar movies using **cosine similarity**  
- ⚡ Built with **Python, Pandas, NLTK, Scikit-learn**  
- 🧑‍💻 Works in both **Jupyter Notebook** and **Python script**  

---

## 📂 Dataset  

Download the dataset from Kaggle:  
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  

Files used:  
- `tmdb_5000_movies.csv`  
- `tmdb_5000_credits.csv`  

Place them inside a `data/` folder in your project:

## 📂 Project Structure

```text
project/
├─ data/
│  ├─ tmdb_5000_movies.csv
│  └─ tmdb_5000_credits.csv
├─ recommendation.py
├─ notebook.ipynb
├─ requirements.txt
└─ README.md
```

## 📊 Sample Output

🎥 Recommendations for **'The Dark Knight'**:

```text
            title
0   The Dark Knight Rises
1   Batman Begins
2   Batman Returns
3   Batman Forever
4   Batman v Superman: Dawn of Justice
```

## 📦 Tech Stack  

### 🖥️ Programming Language  
- **Python 3.8+** – Core language used for building the recommendation system  

### 📊 Data Handling  
- **Pandas** – Data manipulation & cleaning  
- **NumPy** – Numerical computations and matrix operations  

### 🧠 NLP & Machine Learning  
- **NLTK** – Natural Language Processing (tokenization, stopwords, stemming)  
- **Scikit-learn** – TF-IDF Vectorization, Cosine Similarity, ML utilities  

### 📉 Visualization (Optional)  
- **Matplotlib** – Data visualization & analysis (charts, plots)  
- **Seaborn** – (Optional) for advanced visualizations  

### ⚙️ Environment & Tools  
- **Jupyter Notebook** – Interactive coding & experimentation  
- **VS Code / PyCharm** – Development environment  
- **Virtualenv** – For dependency management  
- **Git & GitHub** – Version control & collaboration   

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to **fork this repo** and create a **Pull Request (PR)**.  
 
