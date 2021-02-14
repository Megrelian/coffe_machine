x = int(input())


if x >= 6769:
    if x // 6769 == 1:
        print("1 sheep")
    else:
        print(str(x // 6769) + " sheep")
elif x >= 3848:
    if x // 3848 == 1:
        print("1 cow")
    else:
        print(str(x // 3848) + " cows")
elif x >= 1296:
    if x // 1296 == 1:
        print("1 pig")
    else:
        print(str(x // 1296) + " pigs")
elif x >= 678:
    if x // 678 == 1:
        print("1 goat")
    else:
        print(str(x // 678) + " goats")
elif x >= 23:
    if x // 23 == 1:
        print("1 chicken")
    else:
        print(str(x // 23) + " chickens")
else:
    print("None")
