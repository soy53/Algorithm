t = int(input())
for i in range(t):
  r, s = input().split()
  R = int(r)
  
  for j in s:
    print(j*R, end='')
  print()