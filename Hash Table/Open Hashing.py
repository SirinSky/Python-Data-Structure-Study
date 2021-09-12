# open hashing
class OpenHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
    
    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    
    def save(self, key, value):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    self.hash_table[hash_address][a][1] = value
                    return
            self.hash_table[hash_address].append([key, value])
        else:
            self.hash_table[hash_address] = [[key, value]]
            
    def read(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    return self.hash_table[hash_address][a][0]
            return False
        else:
            return False
    
    def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    if len(self.hash_table[hash_address]) == 1:
                        self.hash_table[hash_address] = 0
                    else:
                        del self.hash_table[hash_address][a]
                    return
            return False
        else:
            return False
            
            
#Test Code
h_table = OpenHash(8)

h_table.save('aa', '1111')
h_table.read('aa')

data1 = 'aa'
data2 = 'ad'

print(ord(data1[0]))
print(ord(data2[0]))

h_table.save('ad', '2222')
print(h_table.hash_table)

h_table.read('aa')
h_table.read('ad')

h_table.delete('aa')
print(h_table.hash_table)
print(h_table.delete('Data'))
h_table.delete('ad')
print(h_table.hash_table)
