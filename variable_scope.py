"""illustrate variable scope in python"""

def counter():
    """create a function to yield consecutive numbers"""
    num = 0

    def increment():
        nonlocal num # overide the scope of the num variable to make it accessible here
        num += 1
        return num

    return increment


name = 'Saul' #gloabl definition

class SaulRepent(object):
    """class to illustate class scope and function in class name look up


    Classes have a local scope during definition, but functions inside the class do not use that scope when looking up
    names. Because lambdas are functions, and comprehensions are implemented using function scope, this can lead
    to some surprising behavior.
    """


    name = 'Paul' # local definition
    reverse_name = lambda: name[:] #  name is gloabl

    @staticmethod
    def judgement():
        print(name)
        return True if name == 'Paul' else False # name is gloabl


if __name__ == "__main__":
    counter1 = counter()
    for i in range(10):
        print(counter1())

    test = SaulRepent()
    print(test.name)
    print(SaulRepent.reverse_name())
    print(test.judgement())
    print(SaulRepent.judgement())
