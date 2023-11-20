from math import ceil

n = int(input())
lst = list(map(int, input().split()))
divisor = min(lst)
a, b = map(int, input().split())

i = 0
a -= 1
b -= 1
while i < len(lst):
    if a <= i <= b:
        lst[i] = format(lst[i]/divisor, '.1f')
    i += 1

for i in lst:
    print(i, end=" ")
