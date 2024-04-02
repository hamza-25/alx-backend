#!/usr/bin/python3
"""Define FIFO Cache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        if len(self.cache_data.items()) >= super().MAX_ITEMS:
            new_dict = {}
            count = 0
            for key, item in self.cache_data.items():
                if count == 0:
                    key_to_delete = key
                    count += 1
                    continue
                new_dict[key] = item

            print(f'DISCARD: {key_to_delete}')
            self.cache_data = new_dict
        self.cache_data[key] = item

    def get(self, key):
        """get key from cache_data dict
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
