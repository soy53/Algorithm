n, m = map(int, input().split())

basket = [0]*n

for i in range(m):
  a, b, c = map(int, input().split())
  for j in range(a, b+1):
    basket[j-1] = c

for k in basket:
  print(k, end=" ")