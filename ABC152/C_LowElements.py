cnt = int(input())
numli = list(map(int, input().split()))
ans = 0
for i in range(1, cnt+1):
  tmpli = numli[0:i]
  target = tmpli[len(tmpli) - 1]
  tmpmin = min(tmpli)
  if target == tmpmin:
    ans += 1
print(ans)
