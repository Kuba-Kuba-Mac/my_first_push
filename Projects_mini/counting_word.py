#
text = ["hi i am kuba, i am a second grade student in technical student"]
name = input("Enter your text :")
result = name.count(" ")
print(result+1)

#       outputs
# Enter your text :hi i am kuba, i am a second grade student in technical student
# 13

name = input("Enter your text: ")

words = name.split()
print(len(words))


# split() is really need thing


name = input("Enter text: ").lower()
words = name.split()
unique = set(words)
print(len(unique))