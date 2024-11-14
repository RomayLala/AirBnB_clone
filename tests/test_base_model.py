#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_create_base_model(self):
        """Test creating an instance of BaseModel."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)  # Ensure it's an instance of BaseModel
        self.assertIsInstance(bm.created_at, datetime)  # Ensure created_at is a datetime object
        self.assertIsInstance(bm.updated_at, datetime)  # Ensure updated_at is a datetime object
        self.assertTrue(hasattr(bm, "id"))  # Ensure it has an id attribute
        self.assertTrue(hasattr(bm, "created_at"))  # Ensure it has a created_at attribute
        self.assertTrue(hasattr(bm, "updated_at"))  # Ensure it has an updated_at attribute

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIn(bm.id, bm_str)  # Check if the id is part of the string representation
        self.assertIn(bm.__class__.__name__, bm_str)  # Check if the class name is part of the string
        self.assertIn(bm.created_at.isoformat(), bm_str)  # Check if created_at is part of the string (in ISO format)
        self.assertIn(bm.updated_at.isoformat(), bm_str)  # Check if updated_at is part of the string (in ISO format)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(type(bm_dict), dict)  # Ensure the result is a dictionary
        self.assertIn("id", bm_dict)  # Ensure the dictionary contains 'id'
        self.assertIn("created_at", bm_dict)  # Ensure the dictionary contains 'created_at'
        self.assertIn("updated_at", bm_dict)  # Ensure the dictionary contains 'updated_at'
        self.assertIn("__class__", bm_dict)  # Ensure the dictionary contains '__class__'
        self.assertEqual(bm_dict["__class__"], "BaseModel")  # Ensure __class__ is 'BaseModel'
        self.assertIsInstance(bm_dict["created_at"], str)  # Ensure created_at is a string
        self.assertIsInstance(bm_dict["updated_at"], str)  # Ensure updated_at is a string

    def test_init_with_kwargs(self):
        """Test initializing BaseModel with kwargs."""
        bm_dict = {
            "id": "1234",
            "created_at": "2024-11-14T11:22:31.794332",
            "updated_at": "2024-11-14T11:22:31.794332",
            "name": "Test Model",
            "my_number": 42,
        }
        bm = BaseModel(**bm_dict)
        self.assertEqual(bm.id, "1234")  # Ensure the id matches
        self.assertEqual(bm.created_at, datetime.fromisoformat("2024-11-14T11:22:31.794332"))  # Ensure the created_at matches
        self.assertEqual(bm.updated_at, datetime.fromisoformat("2024-11-14T11:22:31.794332"))  # Ensure the updated_at matches
        self.assertEqual(bm.name, "Test Model")  # Ensure the name attribute is correctly set
        self.assertEqual(bm.my_number, 42)  # Ensure the my_number attribute is correctly set

if __name__ == "__main__":
    unittest.main()
