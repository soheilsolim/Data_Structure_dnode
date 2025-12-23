class DNode:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        
    def ins_first(self, d):
        a = DNode(d)
        if self.head is None:
            self.head = a
            return
        a.next = self.head
        self.head.back = a
        self.head = a

    def ins_last(self, d):
        a = DNode(d)
        if self.head is None:
            self.head = a
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a
        a.back = temp
            
    def ins_after(self, x, d):
        if self.head is None:
            return
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        if temp is None:
            return
        a = DNode(d)
        if temp.next:
            a.next = temp.next
            temp.next.back = a
        temp.next = a
        a.back = temp

    def del_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            del(self.head)
            self.head = None
            return
        a = self.head
        self.head = self.head.next
        self.head.back = None
        del(a)

    def del_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            del(self.head)
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.back.next = None
        del(temp)

    def del_after(self, x):
        if self.head is None:
            return
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        if temp is None or temp.next is None:
            return
        a = temp.next
        temp.next = a.next
        if a.next:
            a.next.back = temp
        del(a)
            
    def delete(self, x):
        if self.head is None:
            return
        if self.head.data == x:
            a = self.head
            self.head = a.next
            if a.next:
                a.next.back = None
            del(a)
            return
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        if temp is None:
            return
        if temp.next:
            temp.back.next = temp.next
            temp.next.back = temp.back
        else:
            temp.back.next = None
        del(temp)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    dll = DLinkedList()
    dll.ins_first(10)
    dll.ins_first(20)
    dll.ins_last(30)
    dll.ins_after(20, 25)
    print("Doubly Linked List after additions:")
    dll.display()
    
    dll.del_first()
    print("Doubly Linked List after deleting first element:")
    dll.display()
    
    dll.del_last()
    print("Doubly Linked List after deleting last element:")
    dll.display()
    
    dll.del_after(20)
    print("Doubly Linked List after deleting element after 20:")
    dll.display()
    
    dll.delete(25)
    print("Doubly Linked List after deleting element 25:")
    dll.display()
