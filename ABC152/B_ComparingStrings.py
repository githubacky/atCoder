a, b = map(int, input().split())
numab = str(a) * b
numba = str(b) * a
numli = [numab, numba]
numli.sort()
print(numli[0])
