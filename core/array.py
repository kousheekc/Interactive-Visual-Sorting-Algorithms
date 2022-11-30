import random

class Array:
    def __init__(self):
        self.n = 0

    def reset(self, n):
        self.set_len(n)
        self.array = random.sample(range(600), self.n)

    def set_len(self, n):
        self.n = n

    def get_len(self):
        return self.n

    def __len__(self):
        return self.n

    def get_i(self, i):
        return self.array[i]

    def set_i(self, i, val):
        self.array[i] = val

    def __getitem__(self, i):
        return self.array[i]

    def __setitem__(self, i, val):
        self.array[i] = val