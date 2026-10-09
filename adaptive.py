"""Lightweight session-local preference adaptation; no user account or server database."""
from recommender import movies, similarities, genres_list


def update_preferences(preferences, movie_title, liked):
    """Reward or penalize genres of a rated movie, capped to avoid runaway scores."""
    item = next((m for m in movies if m['title'] == movie_title), None)
    if item is None:
        raise ValueError('Please rate a movie from the catalog.')
    scores = dict(preferences)
    for genre in item['genres'].split():
        scores[genre] = max(-3, min(3, int(scores.get(genre, 0)) + (1 if liked else -1)))
    return scores


def adaptive_recommendations(title, genre='', preferences=None):
    """Re-rank positive-similarity movies using explicit feedback genre scores."""
    if genre and genre not in genres_list:
        raise ValueError('Please select a genre from the list.')
    idx = next((i for i, m in enumerate(movies) if m['title'].lower() == title.strip().lower()), None)
    if idx is None:
        raise ValueError('Please select a movie from the list.')
    preferences = preferences or {}
    ranked = []
    for i, movie in enumerate(movies):
        if i == idx or similarities[idx, i] <= 0:
            continue
        labels = movie['genres'].split()
        if genre and genre not in labels:
            continue
        # Keep original genre similarity as primary signal; modest personalization.
        bonus = 0.12 * sum(int(preferences.get(g, 0)) for g in labels)
        ranked.append((-float(similarities[idx, i]) - bonus, i, movie, bonus))
    ranked.sort(key=lambda row: (row[0], row[1]))
    return [{**movie, 'reason': ('Genre similarity plus your feedback' if bonus else 'Similar genres to your selected movie')} for _, _, movie, bonus in ranked[:5]]


def favorite_genres(preferences):
    return [g for g, score in sorted(preferences.items(), key=lambda x: (-x[1], x[0])) if score > 0][:3]
