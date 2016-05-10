class Node(object):
    def __init__(self,value,prev,next):
        self.value = value
        self.prev = prev
        self.next = next

class DList(object):
    head = None
    tail = None

    def add_node(self,data):
        node = Node(data, None, None)
        # if self.head is None:
        #
    def delete_node(self):
        pass
    def insert_node(self):
        pass
a = DList()
a.add_node(5)
print a.value
