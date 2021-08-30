class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree:
    
    #함수 해석: 초기화 함수. 처음 인스턴스될 때 루트 노드를 None으로 설정한다
    def __init__(self): #클래스 내 메소드(함수)에 첫 매개변수로 self를 넣는 것은 일종의 규칙이다 - 자세한건 구글링
        self.root = None
    
    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        #return self.root is not None
        
    def _insert_value(self, node, data):
    #'_' 가 앞에 붙으면 외부 사용자는 사용하지 말라는 권유의 문법.
    #외부에서 이 클래스를 import를 하면 '_' 가 앞에 붙어있는 변수나 메소드들은 호출되지 않음.
    #하지만 직접 호출한다면 사용이 가능하에 권'유의 문법'이라고 불림.
    #다른 언어의 private 비슷하다고 보면 되겠다 생각할수도 있지만 private는 외부 접근이 아예 불가능하니...
    
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
                
        return node
        
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
        
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()

for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
        
