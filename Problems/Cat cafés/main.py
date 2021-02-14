maximum = 0
new_string = ""

while True:
    cats = input()
    if cats != "MEOW":
        cat_list = cats.split()
        num = int(cat_list[1])
        if num > maximum:
            maximum = num
            new_string = cat_list[0]
    else:
        print(new_string)
        break
