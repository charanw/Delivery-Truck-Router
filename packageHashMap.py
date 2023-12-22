class PackageHashMap:
    def __init__(self, size):
        self.list = []
        for i in range(size):
            self.list.append([])

    def _hash_function(self, data):
        return hash(data) % len(self.list)

    def add_package(self, package):
        key = package.id
        sublist_index = self._hash_function(key)
        self.list[sublist_index].append([key, package])
        return

    def get_all_packages(self):
        all_packages = []
        for sublist in self.list:
            all_packages.append(sublist[0][1])
        return all_packages

    def get_package(self, key):
        sublist_index = self._hash_function(key)
        for sublist in self.list[sublist_index]:
            if sublist[0] == key:
                return sublist[1]
        else:
            return False

    def delete_package(self, key):
        sublist_index = self._hash_function(key)
        for sublist in self.list[sublist_index]:
            if sublist[0] == key:
                self.list.remove(self.list[sublist_index])
                print("Package ID #{id} removed".format(id=key))
                return True
        else:
            print("Package ID #{id} not found in hashmap.".format(id=key))
            return False

    def resize_hashmap(self, new_size):
        old_list = self.list
        self.list = []
        for i in range(new_size):
            self.list.append([])
        for sublist in old_list:
            self.add_package(sublist[0][1])
        return True

    def __str__(self):
        hashmap_str = ""
        for list in self.list:
            for sublist in list:
                hashmap_str += "Key: " + str(sublist[0]) + "\t Value: " + str(sublist[1]) + "\n"
        return hashmap_str
