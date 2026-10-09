import unittest
from recommender import get_recommendations
from app import app

class Checks(unittest.TestCase):
    def test_similar_movies_and_exclusion(self):
        result = get_recommendations("Toy Story")
        self.assertEqual(len(result), 5)
        self.assertNotIn("Toy Story", [m["title"] for m in result])
        self.assertEqual(result[0]["title"], "Finding Nemo")
        self.assertEqual(result[1]["title"], "Finding Dory")
    def test_filter(self):
        result = get_recommendations("Toy Story", "Drama")
        self.assertTrue(result)
        self.assertTrue(all("Drama" in m["genres"].split() for m in result))
    def test_no_match(self):
        self.assertEqual(get_recommendations("Toy Story", "Crime"), [])
    def test_invalid(self):
        with self.assertRaises(ValueError): get_recommendations("not a movie")
        with self.assertRaises(ValueError): get_recommendations("Toy Story", "invalid")
    def test_web(self):
        with app.test_client() as c:
            self.assertEqual(c.get("/").status_code, 200)
            r=c.post("/",data={"movie":"Toy Story","genre":""})
            self.assertIn(b"Finding Nemo",r.data)
            self.assertIn(b"Recommended movies",r.data)
    def test_web_error(self):
        with app.test_client() as c:
            r=c.post("/",data={"movie":"wrong"})
            self.assertIn(b"Please select a movie",r.data)

if __name__ == "__main__": unittest.main()

class AdaptiveChecks(unittest.TestCase):
    def test_feedback_and_rerank(self):
        from adaptive import update_preferences, adaptive_recommendations, favorite_genres
        base = adaptive_recommendations('Toy Story')
        pref = update_preferences({}, 'Finding Nemo', True)
        self.assertIn('Animation', favorite_genres(pref))
        changed = adaptive_recommendations('Toy Story', preferences=pref)
        self.assertEqual(len(changed), 5)
        self.assertTrue(any('feedback' in m['reason'] for m in changed))
        self.assertEqual(len(base), len(changed))
    def test_feedback_persists_and_reset(self):
        with app.test_client() as c:
            c.post('/', data={'action':'feedback','movie':'Toy Story','rated_movie':'Finding Nemo','rating':'like'})
            self.assertIn(b'emerging preferences', c.get('/').data)
            c.post('/', data={'action':'reset'})
            self.assertNotIn(b'emerging preferences', c.get('/').data)
    def test_invalid_feedback(self):
        from adaptive import update_preferences
        with self.assertRaises(ValueError): update_preferences({}, 'nonexistent', True)
