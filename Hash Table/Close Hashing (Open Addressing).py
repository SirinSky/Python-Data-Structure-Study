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
            for a in range(hash_address, len(self.hash_table)):
                if self.hash_table[a] == 0:
                    self.hash_table[a] = [key, value]
                    print("저장됨 [" + str(key) + " ," + str(value) + "]")
                    return True
                elif self.hash_table[a][0] == key:
                    self.hash_table[a] = [key, value]
                    print("저장됨 [" + str(key) + " ," + str(value) + "]")
                    return True
                
                elif(a == (len(self.hash_table) - 1)):
                    print("저장 불가(주소 값 끝까지 찾았음에도 넣을 공간 없음)")
                    #만약 주소값 끝까지 찾았음에도 넣을 수가 없다면
                    return False
                    
            print("저장할 수 없음!")
            return False
        else:
            self.hash_table[hash_address] = [key, value]
            
    def read(self, key):
        hash_address = self.hashing(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if(self.hash_table[a] != 0):
                if self.hash_table[a][0] == key:
                    print("값을 찾음 [" + str(self.hash_table[a][0]) + " ," + str(self.hash_table[a][1]) + "]")
                    return True
        
        print("값을 찾을 수 없음!")
        return False
        
    def delete(self, key):
        hash_address = self.hashing(key)
        
        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a] == 0:
                continue
            if self.hash_table[a][0] == key:
                self.hash_table[a] = 0
                return
        return False
        
        
#Test Code
h_table = CloseHash(8)

data1 = 'ad'
data2 = 'aa'
print(ord(data1[0]), ord(data2[0]))

h_table.save('ga', '3333')
h_table.save('gd', '9999')
print(h_table.hash_table)

h_table.read('ga')
h_table.read('ad')

h_table.delete('aa')
print(h_table.hash_table)

h_table.delete('ad')
print(h_table.hash_table)
