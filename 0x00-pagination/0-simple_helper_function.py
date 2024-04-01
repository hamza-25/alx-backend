#!/usr/bin/env python3
"""Define Pagination Module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function named index_range that
    takes two integer arguments page and page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index = (start_index, end_index)
    return index
