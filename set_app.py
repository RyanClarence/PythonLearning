#Remove duplicates from in put and sum
message = "Enter List Of Number like [10,20,30] :  "
list_of_numbers = eval(input(message))
test = []
sum = 0
if type(test) == type(list_of_numbers):
    remove_duplicate = set(list_of_numbers)
    no_duplicate = list(remove_duplicate)
    for number in no_duplicate:
        sum = sum + number
else:
    print(message)
print("Sum is : ",sum)