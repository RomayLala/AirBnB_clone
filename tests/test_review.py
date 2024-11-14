import unittest
from models.review import Review
from models.place import Place
from models.user import User
from models import storage

class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_review_creation(self):
        """Test creation of Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_save(self):
        """Test saving Review instance to storage."""
        place = Place()
        place.name = "Apartment"
        place.save()
        
        user = User()
        user.name = "Jane Doe"
        user.save()

        review = Review()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Great place!"
        review.save()

        all_reviews = storage.all()
        review_key = f"Review.{review.id}"
        self.assertIn(review_key, all_reviews)
        self.assertEqual(all_reviews[review_key].place_id, place.id)
        self.assertEqual(all_reviews[review_key].user_id, user.id)
        self.assertEqual(all_reviews[review_key].text, "Great place!")

    def test_review_reload(self):
        """Test reloading Review instance from storage."""
        place = Place()
        place.name = "Apartment 101"
        place.save()

        user = User()
        user.name = "John Smith"
        user.save()

        review = Review()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Nice stay!"
        review.save()

        # Reload the storage to simulate a fresh load
        storage.reload()

        # Verify that the review instance is reloaded correctly
        review_key = f"Review.{review.id}"
        reloaded_review = storage.all().get(review_key)
        self.assertIsNotNone(reloaded_review)  # Ensure the review exists after reload
        self.assertEqual(reloaded_review.text, "Nice stay!")  # Ensure the text is correct

if __name__ == "__main__":
    unittest.main()
