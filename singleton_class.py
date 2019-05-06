"""illustrate a singleton class: class with only one instance at all times"""


class Singleton(object):

    def __new__(cls):
        try:
            instance = cls.__instance__
        except ArithmeticError:
            instance = cls.__instance__ = object.__new__(cls)
        return it