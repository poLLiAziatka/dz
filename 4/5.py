from sys import stdin

lst = [list(map(int, l.split())) for l in stdin]

res = sum(lst[0])

if all([sum(x) == res for x in lst]) and all([sum(x) == res for x in list(zip(*lst))]):
    print('YES')
else:
    print('NO')
