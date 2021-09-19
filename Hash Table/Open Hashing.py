class OpenHash():
    def __init__(self, size):
        self.size = size
        self.hash_table = [0 for a in range(self.size)]
        
    def hashing(self, key):
        
        hash_address = (ord(key[0])) % self.size
        return hash_address
        
    def save(self, key, value):
        hash_address = self.hashing(key)
        if(self.hash_table[hash_address] != 0):
            for i in range(len(self.hash_table[hash_address])):
                if(self.hash_table[hash_address][i][0] == key):
                    self.hash_table[hash_address][i][1] = value
                    print("저장됨(이미 저장되어 있어 값 갱신)")
                    return True

            (self.hash_table[hash_address]).append([key, value])
            print("저장됨(이미 찬 공간에 중복 저장)")
            return True
                
        else:
            self.hash_table[hash_address] = [[key, value]]
            print("저장됨(빈 공간에 저장)")
            return True
        
    def read(self, key):
        hash_address = self.hashing(key)
        
        if(self.hash_table[hash_address] != 0):
            for i in range (len(self.hash_table[hash_address])):
                if(self.hash_table[hash_address][i][0] == key):
                    value = self.hash_table[hash_address][i][1]
                    print(str(key) + ", " + str(value))
                    return True
                    
            print("해당 값 없음")
            return False
        else:
            print("해당 값 없음")
            return False
        
    def delete(self, key):
        hash_address = self.hashing(key)
        
        if(self.hash_table[hash_address] != 0):
            for i in range(len(self.hash_table[hash_address])):
                if (self.hash_table[hash_address][i][0] == key):
                    if(len(self.hash_table[hash_address]) == 1):
                        print("삭제 완료 [" + str(key) + ", " + str(self.hash_table[hash_address][i][1]) + "]")
                        self.hash_table[hash_address] = 0
                        return True
                    else:
                        print("삭제 완료 [" + str(key) + ", " + str(self.hash_table[hash_address][i][1]) + "]")
                        del (self.hash_table[hash_address][i])
                        return True
                    
        else:
            print("삭제 불가(찾을 수 없음)")
            return False


a = OpenHash(10)

a.save('sirin', 'sky')               #저장됨(빈 공간에 저장)
a.save('serim', 'bradely')           #저장됨(이미 찬 공간에 중복 저장)
a.save('sirin', 'sky\'s library')    #저장됨(이미 저장되어 있어 값 갱신)
a.read('sirin')                      #sirin, sky's library

a.delete('sirin')                    #해당 값 없음
a.read('sirin')                     #해당 값 없음
a.read('serim')
