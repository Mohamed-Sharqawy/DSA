class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class LinkedList:        
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else : 
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node
            
    def insert_at_end(self, data):
        if self.head is None :
            self.head = Node(data)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None, itr)
        
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        
        itr = self.head
        ll = ""
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.next 
        print(ll)      
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
            
        return itr
    def print_backward(self):
        if self.head is None:
            print("linked list is empty!")
            return
        
        last_node = self.get_last_node()
        itr = last_node
            
        bll = ''
        while itr:
            bll += str(itr.data) + '-->'
            itr = itr.prev
        print(bll)
    def get_len(self):
        if self.head is None:
            print("This list is empty")
            
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    def  insert_at(self, index, data):
        if 0 > index or self.get_len() < index:
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
    def remove_at(self, index):
        if 0 > index or self.get_len() < index:
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            
            itr = itr.next
            count += 1
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)