s = input()
alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

seconds = 0
for i in s:
  for j in alpha_list:
    if i in j:
      seconds += (alpha_list.index(j) + 3)

print(seconds)