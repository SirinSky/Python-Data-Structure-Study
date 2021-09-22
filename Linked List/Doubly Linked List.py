# Node
class Node(object):
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
 
class DoublyLinked_list(object):
    def __init__(self):
        self.head = None
 
    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next:
                curn = curn.next
            curn.next = node
            node.prev = curn
        else:
            self.head = node
 
    def insertNodeAtIndex(self, idx, node):
        prevn = None
        nextn = None
 
        # 맨 앞에 추가
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
                nextn.prev = self.head
            else:
                self.head = node
 
        # 중간과 맨 끝에 추가
        else:
            cur_i = 0
            curn = self.head
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.prev = prevn
                node.next = curn
                prevn.next = node
                if curn:
                    curn.prev = node
            else:
                print(-1)
                return -1
 
    def getDataIndex(self, data):
        curn = self.head
        cur_i = 0
 
        while curn:
            if curn.data == data:
                return cur_i
            curn = curn.next
            cur_i += 1
        print(-1)
        return -1
 
    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            # print(-1)
            return -1
 
    def deleteAtIndex(self, idx):
        nextn = None
        prevn = None
        cur_i = 0
 
        if idx == 0:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            else:
                print(-1)
                return -1
        curn = self.head
 
        while cur_i < idx:
            if curn.next:
                prevn = curn
                curn = curn.next
                nextn = curn.next
            else:
                break
            cur_i += 1
        if cur_i == idx:
            if nextn:
                nextn.prev = prevn
            prevn.next = nextn
        else:
            print(-1)
            return -1
 
    def print(self):
        curn = self.head
        string = ''
        prevn = None
        while curn:
            string += str(curn.data)
            if curn.next and curn.prev == prevn:
                string += '<->'
            prevn = curn
            curn = curn.next
        print(string)
 
 
if __name__ == "__main__":
    dl = DoublyLinked_list()
    dl.append(Node(1))
    dl.append(Node(2))
    dl.append(Node(3))
    dl.append(Node(4))
    dl.append(Node(6))
    dl.print()
    dl.insertNodeAtIndex(5,Node(7))
    dl.print()
    dl.insertNodeAtData(6, Node(5))
    dl.print()
    dl.deleteAtIndex(6)
    dl.print()
 
 
