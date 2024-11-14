from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel."""
    
    city_id = ""  # City ID that links to a specific City
    user_id = ""  # User ID that links to a specific User
    name = ""  # Name of the place
    description = ""  # Description of the place
    number_rooms = 0  # Number of rooms, default to 0
    number_bathrooms = 0  # Number of bathrooms, default to 0
    max_guest = 0  # Maximum number of guests, default to 0
    price_by_night = 0  # Price per night, default to 0
    latitude = 0.0  # Latitude, default to 0.0
    longitude = 0.0  # Longitude, default to 0.0
    amenity_ids = []  # List of Amenity IDs, default to an empty list
