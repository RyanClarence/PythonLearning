#Reverse String words

string = "Learning python is easy"
string_list = []
reversed_string = []

for word in string.split():
    string_list.append(word)
number_of_strings = len(string_list)
for _ in string_list:
    number_of_strings-= 1
    reversed_string.append(string_list[number_of_strings])
print(string)
print(" ".join(reversed_string))


#reverses the each character in a string words
reversed_list_string = []

number_of_words = 0
count = 0
for word in string.split():
    reversed_list_string.append(word[::-1])


print("\n")
print(string)
print(" ".join(reversed_list_string))






