# put your python code here
x = int(input())
y = int(input())
summ = 0
total = 0

for i in range(x, y + 1):
    if i % 3 == 0:
        summ = summ + i
        total += 1
print(summ / total)
