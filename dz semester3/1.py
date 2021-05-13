n = int(input())
p = 21
a = []
maximum = 0
answ = [0, 0]

for i in range(n):
    a.append(int(input()))
    for j in a:
        if (a[i] % p == 0 or j % p == 0) and abs(a[i] - j) % 2 == 0:
            if maximum < a[i] + j:
                maximum = a[i] + j
                answ = [a[i], j]
print(answ[0], answ[1])
