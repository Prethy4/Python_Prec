# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 23:17:59 2022

@author: hp
"""

import random
print(random.randrange(2, 6))

x = int(55.97)
print(x)

a = "what to do"
print(a[8])

for x in "luck":
    print(x)
    
x = "donno what to write"
print("donno what" in x) #will show boolean result(true/false)

def myfunc(n):
  return lambda a : a * n