import json


def serializable(cls):
    """
        Adds to_json() method to the decorated class

        to_json() method recursively serializes all the subfields
        as long as the subfields are also serializable or are primitive types
    """

    def __to_json_if_possible(obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return obj

    def to_json(self):
        return {
            k: __to_json_if_possible(v) for k, v in self.__dict__.items() if v is not None
        }

    setattr(cls, 'to_json', to_json)

    return cls
