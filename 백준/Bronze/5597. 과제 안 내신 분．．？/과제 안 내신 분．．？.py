n_list = [0]*30

for _ in range(28):
  n = int(input())
  n_list[n-1] = n

for i in range(2):
  idx = n_list.index(0)
  print(idx+1)
  n_list[idx] = -1