# 내가 푼 방법_리스트 중 0인 부분 찾기
n_list = [0]*30
for _ in range(28):
  n = int(input())
  n_list[n-1] = n

for i in range(30):
  if n_list[i] == 0:
    print(i+1)

# 다른 사람이 푼 방법_remove
x=list(map(int,range(1,31)))
for i in range(28):
    x.remove(int(input()))
for j in x:
    print(j)

# 길이도 시간도 가장 짧은 코드_*, ^(대칭차집합), set 이용
print(*{*map(int,open(0))}^{*range(1,31)})
