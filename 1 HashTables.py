

class HashTable:
    def __init__(self, size = 7):
        # Prime number increases the amount of randomness
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i ,":" ,val)

    # Adding key value pair to the HashTable
    def set(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    # Get the value for the given key
    def get(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][0][i] == key:
                    return self.data_map[index][i][1]

    # Keys method is used to get all keys on hash table
    # and store the all keys in the list
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


    # Interview question
    # In 2 list , checl any common number present or not

my_hash_table = HashTable()
my_hash_table.set("Naruto",1000)
my_hash_table.set("Kurama",2500)
my_hash_table.set("Sasuke",1000)
my_hash_table.print_table()
print(my_hash_table.get("Kurama"))
print(my_hash_table.get("Rin"))
print(my_hash_table.keys())


def items_in_common( list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True

    for j in list2:
        if j in dict:
            return True
    return False

list1 = [1,2,3]
list2 = [3,4,5]
print(items_in_common(list1, list2))
