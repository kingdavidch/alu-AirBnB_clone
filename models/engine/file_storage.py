'''
Author: Shobi Ola-Adisa
File: file_storage.py
Date: 2024-01-11
Description: FileStorage class
'''

import json

FILE_PATH = 'file.json'


class FileStorage:
    '''
    FileStorage class

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects by <class name>.id
    '''
    __file_path = FILE_PATH
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return FileStorage.__objects.copy()

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: object to set in __objects
        '''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        '''
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            casted_dict = {}
            for key, value in FileStorage.__objects.items():
                casted_dict[key] = value.to_dict()
            json.dump(casted_dict, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects
        '''
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)                
        except NameError:
            pass
        except IOError:
            pass
