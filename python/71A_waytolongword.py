q = int(input())

while q:
    q = q-1
    s = input()

    n = len(s)
    if n > 10:
        print("{}{}{}" .format(s[0], n-2, s[-1]))
    else:
        print(s)