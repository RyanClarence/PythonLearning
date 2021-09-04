#Count vowels
vowels = ["a","A","e","E","i","I","o","O","u","U"]
string_holder = """A vowel is a letter that represents an open sound. 
                   There are six vowels in the English language: a, e, i, o, u and sometimes y.
                   Y is sometimes a vowel, as in the word story although it also sometimes acts as a consonant, as in the word yes. 
                   The vocal sounds represented by vowels are open and without friction."""
                   
vowels_from_string_holder =[]

number_of_vowels = 0
for char in string_holder:
    for vowel in vowels:
        if vowel == char:
            number_of_vowels += 1
            vowels_from_string_holder.append(char)
print("Number of vowels : {}".format(number_of_vowels))
[print(vow, end=" ") for vow in vowels_from_string_holder]
