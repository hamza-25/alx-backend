# !/usr/bin/python3
"""Define LRU Cache Module
"""
from collections import OrderedDict
# BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get key from cache_data dict
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
