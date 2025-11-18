from src.memory.memory_bank import MemoryBank

class LoggerAgent:
    def __init__(self):
        self.memory = MemoryBank()

    def save(self, key, value):
        self.memory.store(key, value)
