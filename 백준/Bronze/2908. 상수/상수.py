# 나의 풀이
a, b = input().split()
 
a_re = int(a[::-1])
b_re = int(b[::-1])
 
if a_re > b_re:
  print(a_re)
else:
  print(b_re)

# 위의 코드를 한 줄로 정리
print(max(input()[::-1].split()))
