#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project.
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
            from models import storage  # Delayed import to avoid circular dependency
            storage.new(self)  # Register the new object in storage

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates `updated_at` and saves the object in storage."""
        self.updated_at = datetime.now()
        from models import storage  # Delayed import to avoid circular dependency
        storage.save()  # Save all objects to the file

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
