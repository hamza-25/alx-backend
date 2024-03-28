#!/usr/bin/env python3
"""Define Pagination Module
"""
import csv
import math
from typing import List, Union, Optional


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """function named index_range that
    takes two integer arguments page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index = (start_index, end_index)
    return index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method named get_page that takes two integer arguments
        Return paginate items
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        data_set = self.dataset()
        total_pages = (len(data_set) + page_size - 1) // page_size
        start, end = index_range(page, page_size)
        if 1 <= page <= total_pages:
            page_data = data_set[start:end]
        else:
            return []
        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Hypermedia pagination method return
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        data_set = self.dataset()
        total_pages = (len(data_set) + page_size - 1) // page_size
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if end_index < len(data_set) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
