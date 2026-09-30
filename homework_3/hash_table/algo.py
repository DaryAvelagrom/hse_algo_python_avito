class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                value = pair[1]
                bucket.pop(i)
                self.size -= 1
                return value

        raise KeyError(key)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.size
