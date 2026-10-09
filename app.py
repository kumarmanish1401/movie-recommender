from flask import Flask, render_template, request, session, redirect, url_for
from recommender import get_movie_data, genres_list
from adaptive import adaptive_recommendations, update_preferences, favorite_genres

app = Flask(__name__)
# Set an environment-specific secret for deployments; the default is local coursework only.
import os
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'local-coursework-demo-change-before-deployment')

@app.route('/', methods=['GET', 'POST'])
def index():
    title, genre, results, error = '', '', None, ''
    preferences = session.get('preferences', {})
    if request.method == 'POST':
        action = request.form.get('action', 'recommend')
        title = request.form.get('movie', '')
        genre = request.form.get('genre', '')
        try:
            if action == 'feedback':
                preferences = update_preferences(preferences, request.form.get('rated_movie', ''), request.form.get('rating') == 'like')
                session['preferences'] = preferences
            elif action == 'reset':
                session.pop('preferences', None)
                preferences = {}
            elif action != 'recommend':
                raise ValueError('Unknown action.')
            if title:
                results = adaptive_recommendations(title, genre, preferences)
        except ValueError as exc:
            error = str(exc)
    return render_template('index.html', titles=get_movie_data(), genres=genres_list,
                           title=title, genre=genre, results=results, error=error,
                           favorites=favorite_genres(preferences), preferences=preferences)

if __name__ == '__main__':
    app.run(debug=False)
