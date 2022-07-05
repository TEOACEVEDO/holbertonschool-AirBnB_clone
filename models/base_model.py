#!/usr/bin/python3

"""module"""
from models import storage
import uuid
from datetime import datetime

class BaseModel:
    """Class BaseModel 
    Attr:
    __nb_objects: number instance
    """
    name = ""
    my_number = 0

    def __init__(self, *args, **kwargs):
        """initiliazes an instance"""

        if kwargs:
            self.id = kwargs["id"]

            datetime_created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime_created_at
            datetime_updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime_updated_at
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        Dictionary = self.__dict__
        Dictionary["__class__"] = self.__class__.__name__
        Dictionary["created_at"] = self.created_at.isoformat()
        Dictionary["updated_at"] = self.updated_at.isoformat()
        return (Dictionary)
