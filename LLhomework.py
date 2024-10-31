class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:        
    def __init__(self):
        self.head = None

    def print(self):
        #check if the list is empty
        if self.head is None:
            print("this is an empty list")
            return
        #print listed elements
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' 
            itr = itr.next
            
        print(llstr)
        
    def get_length(self):
        #this tells how many element are in the list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count

    def insert_at_begining(self, data):
        #this insert at the begining of list
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        #this insert values at the end of list
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
    
    def insert_at(self, index, data):
        # this insert value after index
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
    def remove_at(self, index):
        # this removes element after index
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")
        
        if index == 0 :
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
        
        itr = self.head
        while itr :
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
        # Now insert data_to_insert after data_after node
        
        
    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
        
        
        itr = self.head
        
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next
        




if __name__ == "__main__":
    list = LinkedList ()
    list.insert_values(["abdulhameed", "borhan", "El-Qady", "El-bob"])
    list.insert_at_begining("Mamdouh")
    list.insert_at_begining("Mohamed")
    list.insert_after_value("Mamdouh","Adel")
    list.insert_at(0, "Saif")
    print(list.get_length())
    list.print()
    