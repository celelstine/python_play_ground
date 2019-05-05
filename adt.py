"""sample od different abstract data type"""


class Stack(object):
    """last in - first out List"""


    def __init__(self, initial_content = []):
        self.data = initial_content

    def size(self):
        return len(self.data)

    def pop(self):
        """return and remove last element"""
        if self.size() < 1:
            raise ValueError('Stack is empty')
        return self.data.pop()

    def push(self, val):
        """add element to the end of the list"""
        self.data.append(val)
    
    def peek(self):
        """"returns the last element without removing it"""
        if self.size() < 1:
            raise ValueError('Stack is empty')
        return self.data[-1]



class Plate(object):
    """ basic class for kitchen plate"""

    def __init__(self, name):
        self.name = name



plate1 = Plate('1')
plate2 = Plate('2')
plate3 = Plate('3')
plate_rack = Stack()
plate_rack.size()
plate_rack.push(plate1)
plate_rack.push(plate2)
plate_rack.push(plate3)
take = plate_rack.pop()
take.name
plate_rack.pop()
plate_rack.pop()
