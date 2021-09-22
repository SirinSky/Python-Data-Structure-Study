# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
# Singly linked list 클래스 선언
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
 
    # Add new node at the end of the linked list
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
 
    # return first index of data in the linked list
    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1
 
    # Add new node at the given index
    def insertNodeAtIndex(self, idx, node):
        """
        A node can be added in three ways
        1) At the front of the linked list
        2) At a given index.
        3) At the end of the linked list.
        """
        curn = self.head
        prevn = None
        cur_i = 0
 
        # (1) Add 0 index
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            # (2) Add at given index &
            # (3) At the end of the linked list
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1
 
    # Add new node before the given data
    def insertNodeAtData(self, data, node):
        index = self.getdataIndex(data)
        if 0 <= index:
            self.insertNodeAtIndex(index, node)
        else:
            return -1
 
    # Delete data at given index.
    def deleteAtIndex(self, idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1
 
    # Empty linked list
    def clear(self):
        self.head = None
 
    # 출력
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)
 
 
if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    sl.print()
    print(sl.getdataIndex(1))
    print(sl.getdataIndex(2))
    print(sl.getdataIndex(3))
    print(sl.getdataIndex(4))
    print(sl.getdataIndex(5))
    sl.insertNodeAtData(1, Node(0))
    sl.print()
