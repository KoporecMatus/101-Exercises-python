import string

List1 = []
List2 = []

for letter in string.ascii_lowercase:
    List1.append(letter)

List2.append(List1[::2])

List3 = zip(List1,List2)


print(List1)
print(List2)
print(List3)
#"C:/Users/kopor/OneDrive/Počítač/Python/101 Exercises/alphabet.txt"
