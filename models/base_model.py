'''
Author: Shobi Ola-Adisa
File: base_model.py
Date: 2024-01-11
Description: BaseModel class
'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    Base class for all models

    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor for BaseModel class
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        String representation of BaseModel class
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        Updates the public instance attribute updated_at with the current datetime
        '''

        self.updated_at = datetime.now()
        storage
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of __dict__ of the instance
        '''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
