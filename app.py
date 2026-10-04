from flask import Flask, render_template, request
from recommender import get_movie_data, get_recommendations, genres_list

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title, genre, results, error = "", "", None, ""
    if request.method == "POST":
        title = request.form.get("movie", "")
        genre = request.form.get("genre", "")
        try:
            results = get_recommendations(title, genre)
        except ValueError as exc:
            error = str(exc)
    return render_template("index.html", titles=get_movie_data(), genres=genres_list,
                           title=title, genre=genre, results=results, error=error)

if __name__ == "__main__":
    app.run(debug=False)
