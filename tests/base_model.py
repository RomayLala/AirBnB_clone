#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_create_base_model(self):
        """Test creating an instance of BaseModel"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)

    def test_save(self):
        """Test the save method"""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)

    def test_str(self):
        """Test the string representation of the BaseModel"""
        bm = BaseModel()
        self.assertEqual(str(bm), f"[BaseModel] ({bm.id}) {bm.__dict__}")

if __name__ == '__main__':
    unittest.main()
