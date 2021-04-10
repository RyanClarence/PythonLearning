#!/usr/bin/env python3

# use list comprehesion to manipulate each element in 3x3 D array
 
num = [[1,2,3,4,5],[6,7,8],[9,10,11,12]]

print("Result One\n")
result = [ 2 ** num[row][col] for row in range(len(num)) for col in range(len(num[row]))]
print(result)
print("Result Two\n")
result = [ 2 ** num[row][col] for row in range(len(num)) for col in range(len(num[row])) if num[row][col] % 2 == 0]
print(result)