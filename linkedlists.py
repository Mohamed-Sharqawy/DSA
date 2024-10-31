class Node:
    def __init__ (self, data, next):
        self.data = data
        self.next = next

class linked_list:
    def __init__ (self):
        self.head = None 
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def printll(self):
        if self.head is None :
            print("This list is empty")
            return

        itr  = self.head 
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
        

if __name__ == '__main__':
    ll=linked_list()
    ll.insert_at_begining(5)
    ll.insert_at_begining(8)
    ll.insert_at_begining(9)
    ll.insert_at_end(6)
    ll.printll()
    