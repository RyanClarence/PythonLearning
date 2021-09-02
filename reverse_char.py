#String characters reversing

String = input("Enter Your String : ")

#first way to reverse string
print(String)
print(String[::-1])
print("\n")

#Second way to reverse String
print(String)
print(''.join(list(reversed(String))))

print("\b")
#Thired Way to reverse Sttring
print(String)

reversedString = []
count = 0
string_length = len(String)
hold = int(string_length)
while count < string_length:
    hold = int(hold) - 1
    reversedString.append(String[hold])
    count = count + 1
print("".join(reversedString))
    

