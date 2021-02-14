word = input()
new_string = ""
for i in range(len(word)):
    if i == 0 and word[0].isupper():
        new_string = new_string + word[0].lower()

    elif word[i].isupper():
        new_string = new_string + "_" + word[i].lower()
    else:
        new_string = new_string + word[i]
print(new_string)
