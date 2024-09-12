class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        return True

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
        return None

    def keys(self):
        all_keys = []
        for i in self.data_map:
            if i:
                for j in i:
                    if j:
                        all_keys.append(j[0])
        return all_keys


my_table = HashTable()
my_table.set_item("bolts", 1400)
my_table.set_item("washers", 50)
my_table.set_item("lumber", 70)

print(my_table.keys())
