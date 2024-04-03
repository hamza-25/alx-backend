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

    def put(self, key, item):
        """add key value pair to cache_data dict
        """
        # if key is None or item is None:
        #     return

        # lfu_keys = OrderedDict()
        # if key not in self.cache_data:
        #     lfu_keys[key] = 0
        #     if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        #         list_v = [v for v in lfu_keys.values()]
        #         min_v = min(list_v)
        #         for k, v in lfu_keys.items():
        #             if min_v == v:
        #                 first_item_key = k
        #                 break
        #         # first_item_key, _ = list(self.cache_data.items())[0]
        #         print(f'DISCARD: {first_item_key}')
        #         del self.cache_data[first_item_key]
        #     self.cache_data[key] = item
        # else:
        #     lfu_keys[key] += 1
        #     self.cache_data[key] = item
        if key is None or item is None:
            return

        # Update usage frequency
        if key in self.usage_frequency:
            self.usage_frequency[key] += 1
        else:
            self.usage_frequency[key] = 1

        # Add or update item in cache_data
        self.cache_data[key] = item

        # If cache is full, discard least frequently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_key = min(self.usage_frequency, key=self.usage_frequency.get)
            print(f"DISCARD: {min_key}")
            del self.cache_data[min_key]
            del self.usage_frequency[min_key]

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
