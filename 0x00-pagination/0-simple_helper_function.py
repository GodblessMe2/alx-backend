#!/usr/bin/env python3
'''
  Takes two integer arguments page and page_size.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
      Return a tuple containing a start and end
    '''
    return ((page - 1) * page_size, page * page_size)
