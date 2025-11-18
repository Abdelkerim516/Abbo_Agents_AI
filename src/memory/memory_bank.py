class MemoryBank:
    def __init__(self):
        self.long_term = {}

    def store(self, key, value):
        self.long_term[key] = value

    def retrieve(self, key):
        return self.long_term.get(key)
