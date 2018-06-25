"""
Good Handlers

Method and function handlers that implement common
behaviors without writing the entire function

Author:  Anshul Kharbanda
Created: 6 - 24 - 2018
"""
from unittest import TestCase
from good_handlers.init import *


class Person1:
    """
    Tests NameInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = NameInitHandler(names=('name', 'age'), defaults={'age':23})


class Person2:
    """
    Tests UnderscoreInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = UnderscoreInitHandler(names=('name', 'age'), defaults={'age':23})


class Person3:
    """
    Tests DunderInitHandler

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    __init__ = DunderInitHandler(names=('name', 'age'), defaults={'age':23})


class NameInitHandlerTest(TestCase):
    """
    Tests named init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person1(name='Joe Schmoe', age=21)
        self.assertEqual(self.person.name, 'Joe Schmoe')
        self.assertEqual(self.person.age, 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person1(name='Joe Schmoe')
        self.assertEqual(self.person.name, 'Joe Schmoe')
        self.assertEqual(self.person.age, 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person1(age=21)
            self.assertEqual(self.person.age, 21)


class UnderscoreInitHandlerTest(TestCase):
    """
    Tests underscore init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person2(name='Joe Schmoe', age=21)
        self.assertEqual(self.person._name, 'Joe Schmoe')
        self.assertEqual(self.person._age, 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person2(name='Joe Schmoe')
        self.assertEqual(self.person._name, 'Joe Schmoe')
        self.assertEqual(self.person._age, 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person2(age=21)
            self.assertEqual(self.person._age, 21)


class DunderInitHandlerTest(TestCase):
    """
    Tests dunder init

    Author:  Anshul Kharbanda
    Created: 10 - 17 - 2017
    """
    def test_all_names(self):
        """
        Tests all names given
        """
        self.person = Person3(name='Joe Schmoe', age=21)
        self.assertEqual(getattr(self.person, '__name'), 'Joe Schmoe')
        self.assertEqual(getattr(self.person, '__age'), 21)

    def test_defaults(self):
        """
        Tests only non-default names given
        """
        self.person = Person3(name='Joe Schmoe')
        self.assertEqual(getattr(self.person, '__name'), 'Joe Schmoe')
        self.assertEqual(getattr(self.person, '__age'), 23)

    def test_non_default_not_given(self):
        """
        Tests when non-default name is not given
        """
        with self.assertRaises(Exception):
            self.person = Person3(age=21)
            self.assertEqual(getattr(self.person, '__age'), 21)