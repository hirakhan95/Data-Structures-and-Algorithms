class Node:
    value: any
    next: any

    def __init__(self, value: any):
        self.value = value
        self.next = None
        

class LinkedList:
    head: Node
    tail: Node
    length: int = 1

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


my_linked_list = LinkedList(0)
for i in range(1, 10):
    my_linked_list.append(i)

# (2) Items - Returns 2 Node

node = my_linked_list.pop()
while node:
    print(node.value)
    node = my_linked_list.pop()
