#!/usr/bin/python3

import models
from models import base_model
from models import user
from models import state
from models import city
from models import amenity
from models import place
from models import review
import json
import os


class FileStorage:
    """File storage class"""

    classes = {"BaseModel": base_model, "Amenity": amenity,
                      "City": city, "Place": place,
                      "Review": review, "State": state, "User": user}

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name,
                                        fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
