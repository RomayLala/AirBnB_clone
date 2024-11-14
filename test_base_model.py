#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel class."""

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique ID."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_save_updates_updated_at(self):
        """Test that save method updates `updated_at` attribute."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertTrue(instance.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test that to_dict method returns a dictionary with correct keys."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"], instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        instance = BaseModel(id=str(uuid.uuid4()),
                             created_at="2023-01-01T12:00:00",
                             updated_at="2023-01-01T12:00:00")
        self.assertEqual(instance.id, instance.id)
        self.assertEqual(instance.created_at, datetime.fromisoformat("2023-01-01T12:00:00"))
        self.assertEqual(instance.updated_at, datetime.fromisoformat("2023-01-01T12:00:00"))

    def test_str_method(self):
        """Test that __str__ method outputs the correct format."""
        instance = BaseModel()
        expected_output = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_output)


if __name__ == "__main__":
    unittest.main()
