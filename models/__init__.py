# models/__init__.py

from models.engine.file_storage import FileStorage
from models.state import State  # Import the State model
from models.city import City  # Import the City model
from models.amenity import Amenity  # Import the Amenity model
from models.place import Place  # Import the Place model
from models.review import Review  # Import the Review model
from models.user import User  # Import the User model

# Create a single instance of FileStorage for the application
storage = FileStorage()
storage.reload()  # Load existing data if available
