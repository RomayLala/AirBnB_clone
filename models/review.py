from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    
    place_id = ""  # Place ID that links to a specific Place
    user_id = ""  # User ID that links to a specific User
    text = ""  # Text of the review, default to an empty string
