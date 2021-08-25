from sys import argv

sum = 0
if len(argv) <= 0:
    print(sum)
elif len(argv) > 0:
    for data in argv[1:]:
        sum = sum + eval(data)
print(sum)