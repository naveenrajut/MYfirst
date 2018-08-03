
"""

from __future__ import print_function
from itertools import *

for i,j in groupby(map(int,list(raw_input()))):
    print(tuple([len(list(j)), i]) ,end = " ")

"""
from itertools import groupby
