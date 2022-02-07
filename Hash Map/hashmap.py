class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t["March 6"] = 310
t["March 7"] = 420
print(t["March 6"])