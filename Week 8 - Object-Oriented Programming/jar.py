class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.count = 0

    def __str__(self):
        return self.count * "🍪"

    def deposit(self, n):
        self.count += n
        if self.count > self.capacity:
            self.count -= n
            raise ValueError

    def withdraw(self, n):
        self.count -= n
        if self.count < 0:
            self.count += n
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.count
