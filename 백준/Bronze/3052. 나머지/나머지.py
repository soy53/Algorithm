N_list = []
for i in range(10):
  N = int(input())
  remain = N % 42
  if remain not in N_list:
    N_list.append(remain)

print(len(N_list))