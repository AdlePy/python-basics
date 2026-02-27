# class creation through type metaclass
def echo_bar(self):
    print(f"foobar value: {self.foobar}")


Foo = type("Foo", (), {"foobar": "spam and eggs", "echo_bar": echo_bar})

print(Foo)
print(Foo.mro())
print(type(Foo))

foo = Foo()
print(foo)
foo.echo_bar()

# metaclass creation
class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        print(f"new class {name}")
        print(f"with bases: {bases}")
        print(f"with attrs: {dct}")
        new_class = super().__new__(cls, name, bases, dct, *args, **kwargs)
        return new_class
    
Bar = MyMetaclass("Bar", (), {"spam": "eggs"})
print(Bar)
print(type(Bar))


class Zoo(metaclass=MyMetaclass):
    def __new__(cls, *args, **kwargs):
        print(f"__new__ class: {cls}")


print(Zoo)
print(type(Zoo))


# abstract class
from abc import ABC, abstractmethod

class FileManagerABC(ABC):
    @abstractmethod
    def read_file(self):
        pass

class FileManager(FileManagerABC):
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        print(f"read file: {self.filename}")


print(FileManagerABC)
print(FileManagerABC.mro())
print(type(FileManagerABC))