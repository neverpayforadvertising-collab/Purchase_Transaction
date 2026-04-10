import time

class MemoryCache:
    def __init__(self):
        self.store = {}

    def get(self, key):
        value = self.store.get(key)
        if not value:
            return None

        data, expiry = value
        if time.time() > expiry:
            del self.store[key]
            return None

        return data

    def set(self, key, value, ttl=3600):
        self.store[key] = (value, time.time() + ttl)