#!/usr/bin/python3
"""Define FIFO Cache Module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Define BasicCache with methods
    """
    def __init__(self):
        """init method that initializing from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add key value pair to cache_data dict
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_to_delete = next(iter(self.cache_data))  # Get the first key
            del self.cache_data[key_to_delete]
            print(f'DISCARD: {key_to_delete}')

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
