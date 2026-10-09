# Foundation and modifications
Foundation: shyam1998 (2020), Movie Recommendation System GUI, MIT license.
https://github.com/shyam1998/Movie-Recommendation-System-GUI
Reviewed source: imdb_recommendation_system.py and the repository GUI example.
The recommendation module is a simplified adaptation of the displayed source,
not a full repository fork. It retains CountVectorizer, cosine_similarity,
titles_list, get_movie_data, and title-based ranking.
Changes: genres only (remove ratings/votes and television branching); small CSV;
plain Flask form instead of desktop GUI; optional genre filter; five results;
explicitly exclude selected movie; clear invalid/empty-result handling.
movies.csv is manually assembled from 20 real titles. Genre labels are simplified
project annotations, not an export from IMDb or official metadata. SciFi is one token.
The upstream dataset and media assets are not redistributed. Original license retained.
Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
https://flask.palletsprojects.com/en/stable/quickstart/
AI disclosure: ChatGPT/Codex assisted with code adaptation, report drafting and checks.
Review, run, understand and personalize the work before submission. No user study was run.
