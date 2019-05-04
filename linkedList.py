"""Create a linked List struct in python"""


class Node(object):
    """A single node in a linked list"""

    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

    def getNext(self):
        return self.next
    
    def _str_(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    """a struct with linked items"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """check if a linkedlist has no node"""

        return self.head is None

    def prependNode(self, node):
        """add a node to the beginning of a linkedlist"""

        node.setNext(self.head)
        self.head = node

    def append(self, node):
        """add a  node to the end of a linkedlist"""

        # loop through the linkedlist and add node to the end
        current_node = self.head
        previous_node = None

        while current_node is not None:
            previous_node = current_node
            current_node = current_node.getNext()

        if previous_node is not None:
            previous_node.setNext(node)
        else:
            self.head = None

    def removeNode(self, val):
        """remove the first node with the value passed"""

        current_node = self.head
        previous_node = None

        # loop through and check if other node has the value
        while current_node is not None:
            if val == current_node.getData():
                if previous_node is None:
                    self.head = current_node.getNext()
                else:
                    previous_node.setNext(current_node.getNext())
                return
            previous_node = current_node
            current_node = current_node.getNext()
    
        # else raise an error
        raise ValueError('Value not found')

    def size(self):
        """get the number of node in a linkedlist"""

        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.getNext()

        return count

    def findIndex(self, val):
        """find the index of this item"""

        current_node = self.head
        index = 0

        while current_node:
            if current_node.getData() == val:
                return index
            index += 1
            current_node = current_node.getNext()

        # val was not found
        raise ValueError("value does not exist")

    def insert(self, node, position):
        """insert a node at a positon"""

        if position > self.size():
            raise ValueError("Position exceeds the size of the linkedlist")

        index = 0
        current_node = self.head
        previous_node = None

        while current_node is not None or self.head == current_node:
            if index == position:
                node.setNext(current_node)

                # set the parent of the current node to point to the new node
                if previous_node is not None:
                    previous_node.setNext(node)
                else:
                    self.head = node
                return
            index += 1
            previous_node = current_node
            current_node = current_node.getNext()
            
    def pop(self):
        """return and remove the last node"""

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.getNext() is None:
                if previous_node is not None:
                    previous_node.setNext(None)
                    return current_node
            
            previous_node = current_node
            current_node = current_node.getNext()


    def __str__(self):
        if self.head is None:
            return None
        output = ''
        current_node = self.head
        while current_node.getNext() is not None:
            output = "{}{} \n".format(output, current_node.getData())
            current_node = current_node.getNext()
        output = "{}{}".format(output, current_node.getData())
        return output


linkedlist = LinkedList()

node1 = Node(1)
linkedlist.prependNode(node1)

node2 = Node(2)
linkedlist.prependNode(node2)

node3 = Node(3)
linkedlist.append(node3)

print(' \n---findIndex------')
print(linkedlist.findIndex(3))

print(' \n----size-----')
print(linkedlist.size())

node4  = Node(4)
linkedlist.insert(node4, 0)
print(' \n----insert----- ')
print(linkedlist)

print(' \n----pop----- ')
print(linkedlist.pop().getData())

print(' \n----after pop----- ')
print(linkedlist)

linkedlist.removeNode(1)
print(' \n----after removeNode----- ')
print(linkedlist)