from xml.dom.minidom import Element


class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            #collision handling
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, index):
        # h = self.get_hash(index)
        # return self.arr[h]
        arr_index = self.get_hash(index)
        for kv in self.arr[arr_index]:
            if kv[0] == index:
                return kv[1]

    def __delitem__(self, key):
        # h = self.get_hash(key)
        # self.arr[h] = None
        arr_index = self.get_hash(key)
        for idx, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", idx)
                del self.arr[arr_index][idx]

t = HashTable()
t["March 6"] = 310
t["March 7"] = 420
print(t["March 6"])