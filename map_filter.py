#!/usr/bin/env python3

#use map and filter functinal functions

numbers = [1,2,3,4,5,6,7,8,9]
def add(x): return 2 ** x

result = list(map(add,numbers))
print(result)

result = list(filter((lambda x: x % 2 == 0), numbers))
print(result)