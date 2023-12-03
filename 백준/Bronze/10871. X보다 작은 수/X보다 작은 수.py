N, X = map(int, input().split())
n = list(map(int, input().split()))

for i in n:
  if i < X:
    print(i, end=" ")