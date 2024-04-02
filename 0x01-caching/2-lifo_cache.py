#!/usr/bin/python3
"""Define LIFO Cache Module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        if key not in self.cache_data.keys():
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the last key
                last_item_key, _ = list(self.cache_data.items())[-1]
                print(f'DISCARD: {last_item_key}')
                del self.cache_data[last_item_key]
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
