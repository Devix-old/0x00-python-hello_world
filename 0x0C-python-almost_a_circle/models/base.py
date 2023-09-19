#!/usr/bin/python3
"""Defines the Base module."""

import json
import os
import csv


class Base:
    """Defines the Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representing the list of dictionaries.
        """
        if list_dictionaries == "" or list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be serialized and saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                List = [object.to_dictionary() for object in list_objs]
                f.write(cls.to_json_string(List))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == [""]:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance from a dictionary.

        Args:
            **dictionary (dict): Keyword arguments representing
        object attributes.

        Returns:
            instance: An instance of the class with attributes
        set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(0, 0)
        else:
            instance = cls(0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a JSON file and creates instances.

        Returns:
            list: A list of instances of the class.
        """
        json_file = str(cls.__name__) + ".json"
        if not os.path.exists(json_file):
            return []
        with open(json_file, 'r') as f:
            data = Base.from_json_string(f.read())
        return [cls.create(**d) for d in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be serialized and saved.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a CSV file and creates instances.

        Returns:
            list: A list of instances of the class.
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            objects = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls(int(row[1]), int(row[2]), int(
                        row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(row[1]), int(row[2]),
                              int(row[3]), int(row[0]))
                objects.append(obj)
            return objects
