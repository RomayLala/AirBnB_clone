import unittest 
from models.city import City
from models.state import State
from models import storage

class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_city_creation(self):
        """Test creation of City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_save(self):
        """Test saving City instance to storage."""
        city = City()
        state = State()
        state.name = "Florida"
        state.save()  # Save the state to storage

        city.state_id = state.id
        city.name = "Miami"
        city.save()  # Save the city to storage

        all_cities = storage.all()
        city_key = f"City.{city.id}"
        self.assertIn(city_key, all_cities)
        self.assertEqual(all_cities[city_key].name, "Miami")
        self.assertEqual(all_cities[city_key].state_id, state.id)

    def test_city_reload(self):
        """Test reloading City instance from storage."""
        city = City()
        state = State()
        state.name = "Texas"
        state.save()  # Save the state to storage

        city.state_id = state.id
        city.name = "Austin"
        city.save()  # Save the city to storage

        # Reload storage to simulate fresh load
        storage.reload()

        # Verify that the city instance is reloaded correctly
        city_key = f"City.{city.id}"
        reloaded_city = storage.all().get(city_key)
        self.assertIsNotNone(reloaded_city)  # Ensure the city exists after reload
        self.assertEqual(reloaded_city.name, "Austin")  # Ensure the name is correct
        self.assertEqual(reloaded_city.state_id, state.id)  # Ensure the state_id is correct

if __name__ == "__main__":
    unittest.main()
