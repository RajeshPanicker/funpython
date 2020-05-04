#!/usr/bin/env python

from itertools import permutations 

# Three Sum cannot be Easier 
def find_sum_of_three(List, Sum):
  perm = permutations(List, 3) 
    
  for i in list(perm): 
    if int(i[0]) + int(i[1]) + int(i[2]) == Sum:
      return True 
  return False

import unittest

class TestStringMethods(unittest.TestCase):
    def test_find_sum_of_three_1(self):
        self.assertEqual(find_sum_of_three([3, 7, 1, 2, 8, 4, 5],20), True)

    def test_find_sum_of_three_2(self):
        self.assertEqual(find_sum_of_three([3, 7, 1, 2, 8, 4, 5],10), True)

    def test_find_sum_of_three_3(self):
        self.assertEqual(find_sum_of_three([3, 7, 1, 2, 8, 4, 5],21), False)

unittest.main(exit=False)
