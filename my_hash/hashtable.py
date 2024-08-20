#!/usr/bin/env python3
# hashstable.py

BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is BLANK:
            raise KeyError(key)
        return self.values[index]

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

