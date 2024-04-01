#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Optional, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None
        self.total_items = len(self.indexed_dataset())

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination
        """
        dataset_length = len(self.dataset())
        assert index is None and 0 <= index < dataset_length

        if index is None:
            index = 0

        count = 0
        data = []
        for i, item in self.indexed_dataset().items():
            if i >= index and count < page_size:
                data.append(item)
                count += 1
                continue
            if page_size == count:
                next_index = i
                break

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
            # 'page_size': len(data),
        }
