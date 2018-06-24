"""
Good Handlers

Method and function handlers that implement common
behaviors without writing the entire function

Author:  Anshul Kharbanda
Created: 6 - 24 - 2018
"""
from . import InstanceHandler

class NameInitHandler(InstanceHandler):
    """
    Handles initialization of an object by defining named parameters according
    to specifications given in instantiation

    ...
    class Person:
        ___init___ = NameInitHandler(
            names=('name', 'age', 'apparel', 'thoughts')
            defaults={
                'apparel': 'Pajamas',
                'thoughts': 'Nothing at the moment...'
            }
        )
    ...

    The names argument defines all of the names in the class
    The defaults argument defines defaults for names

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    _prefix = ''

    def __init__(self, names=tuple(), defaults=dict()):
        """
        Initializes the NamedInit handler

        :param names: member variable names
        :param defaults: defaults for input names
        """
        self._names = names
        self._defaults = defaults

    def __call__(self, instance, *args, **kwargs):
        """
        Handles initialization for the given instance
            - Only parameters that have been defined in the init will be set
            - Keyword args that are set will override varargs

        :param instance: the instance to handle
        :param *args: the positional arguments
        :param **kwargs: the keyword arguments
        """
        # Set positional arguments
        for name,value in zip(self._names, args):
            setattr(instance, self._prefix+name, value)

        # Set remaining arguments as defaults
        for name in self._names[len(args):]:
            if name in self._defaults:
                setattr(instance, self._prefix+name, self._defaults[name])

        # Set keyword arguments
        for name,value in kwargs.items():
            if name in self._names:
                setattr(instance, self._prefix+name, value)

        # TODO: Custom error for undefined parameters
        for name in self._names:
            if not hasattr(instance, self._prefix+name):
                raise Exception('Required name \'{}\' is not given!'.format(name))

class UnderscoreInitHandler(NameInitHandler):
    """
    NamedInit that appends an underscore to each name in the init

    Author:  Anshul Kharbanda
    Created: 10 - 13 - 2017
    """
    _prefix = '_'

class DunderInitHandler(NameInitHandler):
    """
    NamedInit that appends an dunder, or double-underscore, to each name in the init

    Author:  Anshul Kharbanda
    Created: 10 - 13 - 2017
    """
    _prefix = '__'
