import numpy
status = True
count = 0
index = 0
list_of_lists = []
rows = None
columns = None

while status:
    num = input()
    if num == "":
        status = False
    elif count == 0:
         rows , columns = num.split(" ")
         for row in range(int(rows)):
             list_of_lists.append([])
         count = count + 1
    else:
        for column in num.split(" "):
            list_of_lists[index].append(int(column))
        index = index + 1
my_array = numpy.array(list_of_lists)
print(numpy.transpose(my_array))
print(my_array.flatten())