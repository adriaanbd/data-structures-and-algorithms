class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, init_size=10):
        self.array_of_buckets = [None for _ in range(init_size)]
        self.coefficient = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_hash_code(key)
        node = HashNode(key, value)
        head = self.array_of_buckets[bucket_index]

        while head is not None:
            if head.key == key:
                head.value = value  # replace value
                return
            head = head.next  # traverse til tail

        # no key found
        head = self.array_of_buckets[bucket_index]
        node.next = head
        self.array_of_buckets[bucket_index] = node
        self.num_entries += 1

        # check load factor

        current_load_factor = self.num_entries / len(self.array_of_buckets)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.array_of_buckets[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_hash_code(self, key: str) -> int:
        key = str(key)
        amount_of_buckets = len(self.array_of_buckets)
        hash_code = 0
        value = 37
        coefficient = 1
        for char in key:
            hash_code = ord(char) * coefficient
            hash_code %= amount_of_buckets
            coefficient *= value
            coefficient %= amount_of_buckets
        return hash_code % amount_of_buckets

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_amount_of_buckets = len(self.array_of_buckets)
        old_array_of_buckets = self.array_of_buckets
        amount_of_buckets = 2 * old_amount_of_buckets
        self.array_of_buckets = [None for _ in range(amount_of_buckets)]

        for head in old_array_of_buckets:
            while head is not None:
                self.put(head.key, head.value)
                head = head.next

    def delete(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.array_of_buckets[bucket_index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.array_of_buckets[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries += 1
                return
            else:
                previous = head
                head = head.next


hash_map = HashMap()
hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))  # 4


print("one: {}".format(hash_map.get("one")))  # 1
print("neo: {}".format(hash_map.get("neo")))  # 11
print("three: {}".format(hash_map.get("three")))  # 3
print("size: {}".format(hash_map.size()))  # 4

hash_map.delete("one")

print(hash_map.get("one"))
print(hash_map.size())