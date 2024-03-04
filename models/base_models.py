import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""
    
    
    def __init__(self):
        """init instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime().utcnow
        self.updated_at = datetime().utcnow

    def __str__(self):
        print(f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        
    
    def to_dict(self):
        pass
