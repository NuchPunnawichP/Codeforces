ans = 0

q = int(input())

while q:
    q = q - 1
    x = input()
    
    if x[0] == '-' or x[-1] == '-':
        ans = ans - 1
    if x[0] == '+' or x[-1] == '+':
        ans = ans + 1

print(ans)