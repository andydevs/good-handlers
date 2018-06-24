"""
Good Handlers

Method and function handlers that implement common
behaviors without writing the entire function

Author:  Anshul Kharbanda
Created: 6 - 24 - 2018
"""
from functools import partial
from . import InstanceHandler

class ValueStringHandler(InstanceHandler):
    """
    String representation which displays values of given keys

    Author:  Anshul Kharbanda
    Created: 11 - 10 - 2017
    """
    def __init__(self, keys=tuple()):
        """
        Initializes the ValueStringHandler with the given keys

        :param keys: the keys to display
        """
        self._keys = keys

    def __call__(self, inst):
        """
        Calls the ValueStringHandler

        :param inst: the bound inst
        """
        return '{name}({vals})'.format(
            name=type(inst).__name__,
            vals=', '.join(self._vstr(inst, key) for key in self._keys))

    def _vstr(self, obj, key):
        """
        Returns the value string for the given key

        :param obj: the bound object
        :param key: the key of the value to return

        :return: the value string for the given key
        """
        return repr(getattr(obj, key))

class KeyValueStringHandler(ValueStringHandler):
    """
    String representation which displays given key-value pairs

    Author:  Anshul Kharbanda
    Created: 11 - 9 - 2017
    """
    def _vstr(self, obj, key):
        """
        Returns the value string for the given key

        :param obj: the bound object
        :param key: the key of the value to return

        :return: the value string for the given key
        """
        return '{key}={val}'.format(key=key, val=repr(getattr(obj, key)))
