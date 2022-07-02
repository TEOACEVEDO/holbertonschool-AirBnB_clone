#!/usr/bin/python3

"""module"""
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
        self.id = str(uuid.uuid4())

        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            self.id = kwargs["id"]

            datetime_created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime_created_at
            datetime_updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime_updated_at

    def __str__(self):
        return f"{[self.__class__.__name__]} ({self,id}) {self.__dict__}"

    def save(self)
        self.updated_at = datetime.today()

    def to_dict(self):
        Dictionary = self.__dict__
        Dictionary = ["__clas__"] = self.__clas__.__name__
        Dictionary["created_at"] = self.created_at.isoformat()
        Dictionary["updated_at"] = self.updated_at.isoformat()
        return (Dictionary)

if __name__ == '__main__':
    b1 = BaseModel()
    print(b1.id)
    print(type(b1.id))
    print(b1.created_at)
    print(b1.updated_at)
