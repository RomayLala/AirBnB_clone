import json
from models.base_model import BaseModel
from models.user import User  # Import the User model
from models.state import State  # Import the State model
from models.city import City  # Import the City model
from models.amenity import Amenity  # Import the Amenity model
from models.place import Place  # Import the Place model
from models.review import Review  # Import the Review model

class FileStorage:
    """Class to handle storage of objects to a file in JSON format."""
    
    __file_path = "file.json"  # The path to the JSON file
    __objects = {}  # Stores all objects by <class name>.id as keys

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the objects to the JSON file."""
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
                
                # Dynamically recreate the object based on its class
                if class_name == "BaseModel":
                    self.new(BaseModel(**value))
                elif class_name == "User":
                    self.new(User(**value))
                elif class_name == "State":
                    self.new(State(**value))
                elif class_name == "City":
                    self.new(City(**value))
                elif class_name == "Amenity":
                    self.new(Amenity(**value))
                elif class_name == "Place":
                    self.new(Place(**value))
                elif class_name == "Review":
                    self.new(Review(**value))
        except FileNotFoundError:
            pass  # If the file does not exist, do nothing
        except json.JSONDecodeError:
            pass  # If the file is empty or corrupted, ignore it
