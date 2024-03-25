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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):

        classes = {"BaseModel": base_model, "Amenity": amenity,
                "City": city, "Place": place,
                "Review": review, "State": state, "User": user}

        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r") as file:
            serialized_objects = json.load(file)
            for key, value in serialized_objects.items():
                class_name = value["__class__"]
                if class_name in classes:
                    cls = getattr(classes[class_name], class_name)
                    self.__objects[key] = cls(**value)
