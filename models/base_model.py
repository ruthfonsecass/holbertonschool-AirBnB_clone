#!/usr/bin/python3

# models/base_model.py
import uuid
from models import storage
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs: 
            for key, value in kwargs.items(): 
                if key == 'created_at' or key == 'updated_at': 
                    if type(value) is str: 
                        value = datetime.strptime( 
                            value, "%Y-%m-%dT%H:%M:%S.%f") 

  
                elif key != '__class__':
                    setattr(self, key, value)

        else:           
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

