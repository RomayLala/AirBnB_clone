#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModelDict(unittest.TestCase):
    """Test cases for the BaseModel class, focusing on the to_dict() method."""

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        bm = BaseModel()
        bm_dict = bm.to_dict()

        # Ensure that to_dict returns a dictionary
        self.assertEqual(type(bm_dict), dict)
        
        # Ensure the dictionary contains the required keys
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)
        
        # Ensure the values are in the correct format
        self.assertIsInstance(bm_dict["id"], str)  # id should be a string
        self.assertIsInstance(bm_dict["created_at"], str)  # created_at should be a string (ISO format)
        self.assertIsInstance(bm_dict["updated_at"], str)  # updated_at should be a string (ISO format)
        self.assertEqual(bm_dict["__class__"], "BaseModel")  # __class__ should be 'BaseModel'
        
        # Check if created_at and updated_at are in the ISO format
        created_at_dt = datetime.fromisoformat(bm_dict["created_at"])
        updated_at_dt = datetime.fromisoformat(bm_dict["updated_at"])

        # Ensure that the datetime objects are correct
        self.assertEqual(bm.created_at, created_at_dt)
        self.assertEqual(bm.updated_at, updated_at_dt)

    def test_to_dict_with_kwargs(self):
        """Test initializing BaseModel with kwargs and converting to dict."""
        bm_dict = {
            "id": "1234",
            "created_at": "2024-11-14T11:22:31.794332",
            "updated_at": "2024-11-14T11:22:31.794332",
            "name": "Test Model",
            "my_number": 42,
        }
        bm = BaseModel(**bm_dict)
        bm_dict_out = bm.to_dict()

        # Check that the to_dict() method produces the correct dictionary
        self.assertEqual(bm_dict_out["id"], "1234")
        self.assertEqual(bm_dict_out["created_at"], "2024-11-14T11:22:31.794332")
        self.assertEqual(bm_dict_out["updated_at"], "2024-11-14T11:22:31.794332")
        self.assertEqual(bm_dict_out["name"], "Test Model")
        self.assertEqual(bm_dict_out["my_number"], 42)

        # Check that __class__ is added to the dictionary
        self.assertEqual(bm_dict_out["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()
