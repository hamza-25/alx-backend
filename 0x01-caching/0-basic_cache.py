#!/usr/bin/python3
"""Define Basic Cache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Define BasicCache with methods
    """
    def __init__(self):
        """init method that initializing from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """add key value pair to cache_data dict
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
