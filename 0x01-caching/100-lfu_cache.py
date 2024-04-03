#!/usr/bin/python3
"""Define LFU Cache Module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Define LFUCache with methods
    """
    def __init__(self):
        """init method that initializing from BaseCaching
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = {}
        self.access_time = 0

    def put(self, key, item):
        """add key value pair to cache_data dict
        """
        if key is None or item is None:
            return

        if key in self.usage_frequency:
            self.usage_frequency[key] += 1
        else:
            self.usage_frequency[key] = 0

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_key = min(self.usage_frequency,
                              key=self.usage_frequency.get)
                print(f'DISCARD: {min_key}')
                del self.cache_data[min_key]
                del self.usage_frequency[min_key]
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
