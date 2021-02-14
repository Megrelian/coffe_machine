# put your python code here
num_list = []
while True:
    i = int(input())
    if i > 100:
        break
    elif i < 10:
        continue
    else:
        num_list.append(i)
for i in num_list:
    print(i)