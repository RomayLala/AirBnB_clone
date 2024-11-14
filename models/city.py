from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel."""
    
    state_id = ""  # State ID to link City with a State
    name = ""  # City name, default to an empty string
