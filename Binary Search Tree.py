class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    
    def __init__(self): #클래스 내 메소드(함수)에 첫 매개변수로 self를 넣는 것은 일종의 규칙이다 - 자세한건 구글링
        self.root = None
    
    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        if self.root is not None:
        	print("Inserted (" + str(data) + ")")
        else:
        	print("Can't Insert")
        
    def _insert_value(self, node, data):
    #'_' 가 앞에 붙으면 외부 사용자는 사용하지 말라는 권유의 문법.
    #외부에서 이 클래스를 import를 하면 '_' 가 앞에 붙어있는 변수나 메소드들은 호출되지 않음.
    #하지만 직접 호출한다면 사용이 가능하에 권'유의 문법'이라고 불림.
    #다른 언어의 private 비슷하다고 보면 되겠다 생각할수도 있지만 private는 외부 접근이 아예 불가능하니...
        
        #현 위치에 노드가 없다면
        if node is None:
            node = Node(data) #노드를 삽입한다
            
        else:
            #삽입하려는 데이타보다 현 위치의 노드의 데이터가 크거나 같으면
            if data <= node.data:
                #현 위치의 노드의 좌측 자식 노드에 함수를 재귀시킨다
                node.left = self._insert_value(node.left, data)
                
            #삽입하려는 데이타보다 현 위치의 노드의 데이터가 작으면
            else:
                #현 위치의 노드의 우측 자식 노드에 함수를 재귀시킨다
                node.right = self._insert_value(node.right, data)
                
        return node
        
    def find(self, key):
        
        #height라는 변수를 설정하여 key값이 어느 높이에 있는지 출력시킨다
        self.height = 0
        self._find_value(self.root, key)
    
    def _find_value(self, node, key):
        
        #현재 노드가 없다면 - 찾는 값이 없다라고 출력
        if node is None:
            print("Doesn't Exist.")
            
        else:
            self.height += 1
            
             #현재 노드가 찾는 값이라면
            if node.data == key:
                print("Exist. (Height " + str(self.height)+")")

            else:
                #찾는 값보다 현재 노드 데이터가 크다면 - 좌측 자식 노드로 재귀
                if key < node.data:
                    self._find_value(node.left, key)

                #현 노드 데이터가 찾는 값보다 작다면 - 우측 자식 노드로 재귀
                else:
                    self._find_value(node.right, key)
        
    
    def delete(self, key):
        self.root = self._delete_value(self.root, key)

    def _delete_value(self, node, key):
        
        #해당 노드가 없으면
        if node is None:
    
            print ("Can't Delete.(Key value does not Exist)")
            return node
        
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            
            # 삭제할 노드의 자식이 두개일 경우
            if node.left and node.right:
                
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                target, targetParent = node.right, node
                
                while target.left != None:
                    target, targetParent = target.left, target
                
                #target(node의 우측 서브 트리에서 가장 왼쪽에 있는 노드)의 좌측 자식에, 삭제할 노드(node)의 좌측 자식을 연결한다
                target.left = node.left
                
                #만약 target의 부모(targetParent)가 삭제할 노드가 아니라면 - [즉, target이 node의 우측 자식이 아니라면]
                if targetParent != node:
                    
                    #targetParent의 좌측 자식 위치(target이 있었던 위치)에, target의 우측 자식을 연결시킨다
                    targetParent.left = target.right
                    #target의 우측 자식에, 삭제하려는 노드의 우측 자식을 연결한다
                    target.right = node.right
                    
                node = target
                print("Deleted. (Replaced with " + str(node.data) + ")")
                
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                
                node = node.left or node.right
                print("Deleted. (Replaced with " + str(node.data) + ")")
                
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
                print("Deleted.")
        
        #삭제하려는 값이 해당 노드의 값보다 작다면
        elif key < node.data:
            
            #해당 노드의 좌측으로 함수를 재귀시킨다
            node.left = self._delete_value(node.left, key)
        
        #삭제하려는 값이 해당 노드의 값보다 크다면
        else:
            
            #해당 노드의 우측으로 함수를 재귀시킨다
            node.right = self._delete_value(node.right, key)
            
        return node
        
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()

for x in array:
    bst.insert(x)

# Find
bst.find(15) # Exsit (Height 5)
bst.find(17) # Doesn't Exist.
bst.find(55) #Exist (Height 3)

# Delete
bst.delete(55) # Deleted. (Replaced with 48)
bst.delete(14) # Deleted. (Replaced with 15)
bst.delete(11) # Can't Delete.(Key value does not Exist)

bst.find(55) # Doesn't Exist.
bst.find(14) # Doesn't Exist.
