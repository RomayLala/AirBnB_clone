import json
from models.base_model import BaseModel

class FileStorage:
    """Class to handle storage of objects to a file in JSON format."""
    
    __file_path = "file.json"  # The path to the JSON file
    __objects = {}  # This will store all objects by <class name>.id as keys

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the objects to the JSON file."""
        # Create a dictionary representation of all objects
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()  # Convert object to dict
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(obj_dict, f)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                # Get the class corresponding to the class name in the dictionary
                if class_name == "BaseModel":
                    self.new(BaseModel(**value))  # Recreate the object
                # Add more models here if needed in the future
        except FileNotFoundError:
            pass  # If the file does not exist, we do nothing
        except json.JSONDecodeError:
            pass  # If the file is empty or corrupted, we ignore it
