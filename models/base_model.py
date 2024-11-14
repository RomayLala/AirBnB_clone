#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project.
This module contains the BaseModel class that serves as the base
class for all other models, handling common attributes and methods.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all AirBnB clone models."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        # Ensure created_at and updated_at are formatted as strings using isoformat
        created_at_str = self.created_at.isoformat()
        updated_at_str = self.updated_at.isoformat()
        return f"[{self.__class__.__name__}] ({self.id}) {{'id': '{self.id}', 'created_at': '{created_at_str}', 'updated_at': '{updated_at_str}'}}"

    def save(self):
        """Updates `updated_at` with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
