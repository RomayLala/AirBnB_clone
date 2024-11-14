import unittest
from models.amenity import Amenity
from models import storage

class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    def test_amenity_creation(self):
        """Test creation of Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_amenity_save(self):
        """Test saving Amenity instance to storage."""
        amenity = Amenity()
        amenity.name = "Pool"
        amenity.save()  # Save the amenity to storage

        all_amenities = storage.all()
        amenity_key = f"Amenity.{amenity.id}"
        self.assertIn(amenity_key, all_amenities)
        self.assertEqual(all_amenities[amenity_key].name, "Pool")

    def test_amenity_reload(self):
        """Test reloading Amenity instance from storage."""
        amenity = Amenity()
        amenity.name = "Hot Tub"
        amenity.save()  # Save the amenity to storage

        # Reload storage to simulate fresh load
        storage.reload()

        # Verify that the amenity instance is reloaded correctly
        amenity_key = f"Amenity.{amenity.id}"
        reloaded_amenity = storage.all().get(amenity_key)
        self.assertIsNotNone(reloaded_amenity)  # Ensure the amenity exists after reload
        self.assertEqual(reloaded_amenity.name, "Hot Tub")  # Ensure the name is correct

if __name__ == "__main__":
    unittest.main()
