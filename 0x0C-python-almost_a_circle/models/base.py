#!/usr/bin/python3
"""define base module"""
import json
import os
import csv


class Base:
    """define base class"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                List = [object.to_dictionary() for object in list_objs]
                f.write(cls.to_json_string(List))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == [""]:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(0, 0)
        else:
            instance = cls(0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        json_file = str(cls.__name__) + ".json"
        if not os.path.exists(json_file):
            return []
        with open(json_file, 'r') as f:
            data = Base.from_json_string(f.read())
        return [cls.create(**d) for d in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
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
