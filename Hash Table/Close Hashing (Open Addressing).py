class CloseHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def hashing(self, key):
        hash_address = (ord(key[0])) % self.size
        return hash_address
    
    def save(self, key, value):
        hash_address = self.hashing(key)
        
        if self.hash_table[hash_address] != 0:
            for i in range(hash_address, len(self.hash_table)):
                if self.hash_table[i] == 0:
                    self.hash_table[i] = [key, value]
                    #print("Saved! [" + str(key) + " ," + str(value) + "]")
                    return True
                elif self.hash_table[i][0] == key:
                    self.hash_table[i] = [key, value]
                    #print("Saved! [" + str(key) + " ," + str(value) + "]")
                    return True
                
                   
            #만약 주소값 끝까지 찾았음에도 넣을 수가 없없다면 주소를 위가 아닌 아래로도 찾아본다
            for j in reversed(range(0, hash_address)):
                    
                if self.hash_table[j] == 0:
                    self.hash_table[j] = [key, value]
                    #print("Saved! [" + str(key) + " ," + str(value) + "]")
                    return True
                elif self.hash_table[j][0] == key:
                    self.hash_table[j] = [key, value]
                    #print("Saved! [" + str(key) + " ," + str(value) + "]")
                    return True
            
            #주소값 위 아래로도 공간이 없다면
            print("Can't Save!(Not Enough Space)")
            return False
        else:
            #print("Saved! [" + str(key) + " ," + str(value) + "]")
            self.hash_table[hash_address] = [key, value]
            return True
            
    def read(self, key):
        hash_address = self.hashing(key)
        
        for i in range(hash_address, len(self.hash_table)):
            if(self.hash_table[i] != 0):
                if self.hash_table[i][0] == key:
                    print("Data Found! [" + str(self.hash_table[i][0]) + " ," + str(self.hash_table[i][1]) + "]")
                    return True
        
        for j in reversed(range(0, hash_address)):
            if(self.hash_table[j] != 0):
                if self.hash_table[j][0] == key:
                    print("Data Found! [" + str(self.hash_table[j][0]) + " ," + str(self.hash_table[j][1]) + "]")
                    return True
            
        print("Data Missing! ( " + key + " )")
        return False
        
    def delete(self, key):
        hash_address = self.hashing(key)
        
        for i in range(hash_address, len(self.hash_table)):
            if self.hash_table[i] == 0:
                continue
            
            if self.hash_table[i][0] == key:
                print("Deleted! ( "+ key + " )")
                self.hash_table[i] = 0
                return True
                
        for j in reversed(range(0, hash_address)):
            if self.hash_table[j] == 0:
                continue
            
            if self.hash_table[j][0] == key:
                print("Deleted! ( "+ key + " )")
                self.hash_table[j] = 0
                return True
        
        print("Can't Delete!")
        return False
        
        
#Test Code
h_table = CloseHash(8) #hash_table size는 8

data1 = 'e1'
data2 = 'e2'
print('e1: ' + str(ord(data1[0])) + ', e2: ' + str(ord(data2[0]))) #e1과 e2는 앞글자가 서로 같기에 해시화를 진행해도 같은 값이 나옴

h_table.save('e1', '1111')
h_table.save('e2', '2222')
h_table.save('e3', '3333')
h_table.save('e4', '4444')
h_table.save('e5', '5555')
h_table.save('e6', '6666')
h_table.save('e7', '7777')
h_table.save('e8', '8888')

h_table.save('e9', '9999') #Can't Save! (Not Enough Space) - hash_table size를 8로 설정하였기에

print(h_table.hash_table)

h_table.read('e2') #Data Found! [e2, 2222]
h_table.read('e8') #Data Found! [e8, 8888]
h_table.read('e4') #Data Found! [e4, 4444]

h_table.delete('e2') #Deleted! ( e2 )
h_table.delete('e8') #Deleted! ( e8 )
h_table.delete('e4') #Deleted! ( e4 )
print(h_table.hash_table)
