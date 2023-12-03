n_list = []
for i in range(9):
  a = int(input())
  n_list.append(a)

print(max(n_list))
print(n_list.index(max(n_list)) + 1)