class Node(object):
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
class DList(object):
    head = None
    tail = None

    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
    def delete_node(self,node_value):
        current_node = self.head
        while current_node is not None: # cycle through all the nodes
            if current_node.value == node_value: # if the node is found
                if current_node.prev is not None: #if not first element
                    current_node.prev.next = current_node.next #setting the next hooks to it's next
                    if current_node.next is not None:#if there is a next
                        current_node.next.prev = current_node.prev #setting the prev hooks to it's prev
                    else:
                        current_node.prev.next = None #setting the prev hooks to it's prev
                else:#no prev (current node is head)
                    self.head = current_node.next
                    current_node.next.prev = None
            current_node = current_node.next
    def insert_after(self, data,position):
        print data,position
        string1 = ""
        for i in range(1,position):
            string1 = string1+".next"
        string2 = "self.head"+string1
        current_node = eval(string2)
        print current_node.value
        new_node = Node(data)
        new_node.prev = current_node
        new_node.next = current_node.next
        current_node.next = new_node

    def show(self):
        print "List values:"
        current_node = self.head
        counter = 1
        print self.head.next.next.value
        while current_node is not None:
            print str(counter)+" ",
            print current_node.value
            current_node = current_node.next
            counter+=1

a = DList()
a.add_node('33')
a.add_node('b')
a.add_node('zz')
# a.delete_node('zz')
a.show()
a.insert_after('44',3)
a.insert_after('22',1)
a.show()
