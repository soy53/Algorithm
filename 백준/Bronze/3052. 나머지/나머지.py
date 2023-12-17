# 나의 풀이
N_list = []
for i in range(10):
  N = int(input())
  remain = N % 42
  if remain not in N_list:
    N_list.append(remain)

print(len(N_list))

# set() 이용하기
s = set()
for _ in range(10):
    s.add(int(input())%42)
print(len(s))
