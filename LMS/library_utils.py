import os,json,re
from abc import ABC, abstractmethod
from itertools import groupby, combinations

class BookNotFoundError(Exception):
    pass

class InvalidISBNError(Exception):
    pass

class DuplicateBookError(Exception):
    pass