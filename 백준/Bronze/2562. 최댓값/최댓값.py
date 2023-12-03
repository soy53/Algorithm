# 내가 푼 방법
n_list = []
for i in range(9):
  a = int(input())
  n_list.append(a)

print(max(n_list))
print(n_list.index(max(n_list)) + 1)


# 리스트로 한 줄에 쓰는 방법
a = [int(input()) for i in range(9)]

print(max(a))
print(a.index(max(a)) + 1)
