# Good Handlers

Method and function handlers that implement common behaviors without writing the entire function

## Handlers

Handlers are objects that act as methods in a class. They are good for configurable, predefined functions which will otherwise be redundant to implement. Handler functionality is implemented in standard python's `__call__` method, which otherwise treats the handler like a function.

```python
from good_handlers import InstanceHandler

class MyHandler(InstanceHandler):
    def __init__(self, scale):
        self._scale = scale

    def __call__(self, instance, arg1, arg2):
        instance.result = scale*(arg1+arg2)
```

The class `InstanceHandler` binds to an instance. This requires the extra `instance` parameter, which will become the bound instance of the handler

```python
from good_handlers import InstanceHandler

class MyHandler(InstanceHandler):
    def __init__(self, scale, save='last_result'):
        self._scale = scale
        self._save = save

    def __call__(self, instance, arg1, arg2):
        setattr(instance, self._save, scale*(arg1+arg2))

class MyClass:
    def __init__(self):
        self.last_result = None

    handler = MyHandler(3)
```

The class `ClassHandler` binds to a class and passes the bound class to the extra `klass` parameter.

```python
from good_handlers import ClassHandler

class DefaultAgePersonMaker(ClassHandler):
    def __init__(self, defage):
        self._defage = defage

    def __call__(self, klass, name):
        return klass(name=name, age=self._defage)

class Person:
    make_twenty_year_old = DefaultAgePersonMaker(20)

    def __init__(self, name, age):
        self._name = name
        self._age = age

jim = Person.make_twenty_year_old('Jim Shim') # Makes Person('Jim Shim', 20)
```

### Init Handlers

A special case of redundant programming is the `__init__` method. Often times, the `__init__` is only used to set a series of member variables. Thus, they will often contain a lot of boilerplate code. The Good Library offers a few `__init__` handlers, which simplify creating `__init__` methods. `NamedInitHandler` sets member variables according to a tuple of names provided in the `names` parameter.

```python
from good_handlers.init import NameInitHandler

class Person:
    __init__ = NameInitHandler(
        names=('name', 'age', 'apparel', 'thoughts')
    )
```

Default values for these can be provided as a dict in the `defaults` parameter.

```python
from good_handlers.init import NameInitHandler

class Person:
    __init__ = NameInitHandler(
        names=('name', 'age', 'apparel', 'thoughts'),
        defaults={
            'apparel': 'Pajamas',
            'thoughts': 'Nothing at the moment...'
        }
    )
```

`UnderscoreInitHandler` is a type of `NamedInitHandler` that appends an underscore `_` to each name before setting it in the instance. `DunderInitHandler` adds a dunder, or a double-underscore `__` before each name

### String Handlers

Another case of redundant programming is string representations. The Good Library provides `ValueStringHandler`, which prints the object name and the values of the given keys to show, and `KeyValueStringHandler`, which is like `ValueStringHandler`, but displays key=value pairs instead of just values

```python
from good_handlers.string import ValueStringHandler, KeyValueStringHandler

class Person1:
    """
    Docstring for Person
    """
    def __init__(self, name, age):
        """
        Initializes instance
        """
        self.name = name
        self.age = age

    __repr__ = ValueStringHandler(('name', 'age'))

class Person2:
    """
    Docstring for Person2
    """
    def __init__(self, name, age):
        """
        Initializes instance
        """
        self.name = name
        self.age = age

    __repr__ = KeyValueStringHandler(('name', 'age'))

john1 = Person1('John Numberone', 21)
john2 = Person2('John Numbertwo', 28)

print(john1) # prints 'Person1(\'John Numberone\', 21)'
print(john2) # prints 'Person2(name=\'John Numbertwo\', age=28)'
```