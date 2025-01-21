ans = 0

q = int(input())

while q:
    ch = 0
    q = q - 1
    a = [int(x) for x in input().split()]

    for i in range(0, 3):
        if a[i] != 0:
            ch = ch + 1

    if ch > 1:
        ans = ans + 1
print(ans)