#!/usr/bin/env python3
""" 
  Takes two integer arguments page with default value 1 and
  page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple


class Server:
    """
      Server class to paginate a database of popular baby names.
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
        """ 
          Find the correct index to paginate dataset.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)
