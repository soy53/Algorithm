# 나의 풀이_index()
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
  if i in s:
    print(s.index(i), end=' ')
  else:
    print(-1, end=' ')

# find() 사용
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
	print(a.find(i), end=' ')
