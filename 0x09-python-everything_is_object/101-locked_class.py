#!/usr/bin/python3
class LockedClass:
    """LockedClass"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 str(name)+"'")
        self.__dict__[name] = value
