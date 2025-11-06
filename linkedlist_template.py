class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def set_next(self, node):
        self._next_node = node


    def get_next(self):
        return self._head_node._next_node

    def get_data(self):
        return self._head_node._data

class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        """ Allows the use of len(stack) to find the number of elements in the stack """
        return self._size


    def push(self, data):
        new_node = Node(data,self._head_node)
        self._head_node = new_node
        self._size += 1


    def pop(self):
        if LinkedList.is_empty(self) == False :
            oldheaddata = Node.get_data(self)
            self._head_node = Node.get_next(self)
            self._size -= 1
        else:
            oldheaddata = 'empty'
        return oldheaddata


    def peek(self):
        return self._head_node
    
    def is_empty(self):
        return self._size == 0
    
    def __str__(self):
        """ Defines what should be displayed when the user prints a linked list object. """
        size = self._size
        headnoden = self._head_node
        for i in range(0, self._size):
            headdata = Node.get_data(self)
            if i == 0:
                print(f"[{headdata},", end=" ")
            elif i < (self._size - 1):
                print(f"{headdata},", end=" ")
            elif i == (self._size - 1):
                print(f"{headdata}]", end="")
            self._head_node = Node.get_next(self)
            size -=1
        self._head_node = headnoden
        return ","
        

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    # my_stack.append(4)

    print(my_stack, len(my_stack))

    while not my_stack.is_empty():
       print(my_stack.pop())

