#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with deletion-resilient pagination info
        """
        indexed_data = self.indexed_dataset()

        # Verify that index is in valid range
        assert index is not None
        assert isinstance(index, int)
        assert 0 <= index < len(indexed_data)

        data = []
        current_index = index

        # Collect page_size items starting from index
        while len(data) < page_size and current_index in indexed_data:
            data.append(indexed_data[current_index])
            current_index += 1

        # Find next valid index (skip deleted items)
        next_index = current_index
        while next_index in indexed_data and next_index < max(indexed_data.keys()):
            next_index += 1

        # If we've reached the end, next_index should be None or the next valid index
        if next_index > max(indexed_data.keys()):
            next_index = None
        elif next_index not in indexed_data:
            # Find the next existing index
            while next_index <= max(indexed_data.keys()) and next_index not in indexed_data:
                next_index += 1
            if next_index > max(indexed_data.keys()):
                next_index = None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
