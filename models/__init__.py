# models/__init__.py

from models.engine.file_storage import FileStorage

# Create a single instance of FileStorage for the application
storage = FileStorage()
storage.reload()  # Load existing data if available
