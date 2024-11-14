import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models import storage

class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_place_creation(self):
        """Test creation of Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_save(self):
        """Test saving Place instance to storage."""
        city = City()
        city.name = "New York"
        city.save()
        
        user = User()
        user.name = "John Doe"
        user.save()
        
        place = Place()
        place.city_id = city.id
        place.user_id = user.id
        place.name = "Penthouse"
        place.save()

        all_places = storage.all()
        place_key = f"Place.{place.id}"
        self.assertIn(place_key, all_places)
        self.assertEqual(all_places[place_key].name, "Penthouse")
        self.assertEqual(all_places[place_key].city_id, city.id)
        self.assertEqual(all_places[place_key].user_id, user.id)

    def test_place_reload(self):
        """Test reloading Place instance from storage."""
        city = City()
        city.name = "Los Angeles"
        city.save()

        user = User()
        user.name = "Alice"
        user.save()

        place = Place()
        place.city_id = city.id
        place.user_id = user.id
        place.name = "Studio"
        place.save()

        # Reload the storage to simulate a fresh load
        storage.reload()

        # Verify that the place instance is reloaded correctly
        place_key = f"Place.{place.id}"
        reloaded_place = storage.all().get(place_key)
        self.assertIsNotNone(reloaded_place)  # Ensure the place exists after reload
        self.assertEqual(reloaded_place.name, "Studio")  # Ensure the name is correct

if __name__ == "__main__":
    unittest.main()
