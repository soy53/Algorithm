# 나의 풀이
s = input()
s_list = list(s.split())
 
print(len(s_list))

# 띄어쓰기 개수
s=input().strip()
if len(s):
  print(s.count(" ")+1)
else:
  print(0)
