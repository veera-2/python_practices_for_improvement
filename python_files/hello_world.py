patient_name = "john smith"
age = 20
new_patient = True

print("name: "+patient_name)
print("age: "+str(age))
print("new patient: "+str(new_patient))
print("hello world, " * 10) # print the string multiple times as you wish (*), you put it after the quote and write any amout of time you want it to print


number = 98
print(f"{number:d} Battery street")

number = 3.14159
print(f"Float: {number:.2f}")

str = "Holberton School"
print(str*3)
print(str[:9])

str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print("Welcome to {}!".format(str1))
print("welcome to "+str1+"!")

word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)

