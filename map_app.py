list_of_numbers1 = [1,2,3,4,5,6,7,8,9,10]
list_of_numbers2 = [1,2,3,4,5,6,7,8,9,10]
list_of_numbers3 = [1,2,3,4,5,6,7,8,9,10]

list_of_sum = list(map(lambda number1,number2,number3: number1+ number2+ number3,list_of_numbers1,list_of_numbers2,list_of_numbers3))
print(list_of_sum)