firstNumber = input("Enter First Number : ")
secondNumber = input("Enter Second Number : ")

sum = int(firstNumber) + int(secondNumber)
print(sum)

firstNumber = int(input("Enter First Number : "))
secondNumber =int(input("Enter Second Number : "))

sum = firstNumber + secondNumber
print(sum)

sum = 0
hold = input("Enter 3 numbers, with comma separation : ")
for i in hold.split(","):
    sum = sum + eval(i)
print(sum)


