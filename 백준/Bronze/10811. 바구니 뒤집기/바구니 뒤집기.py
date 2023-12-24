n, m = map(int, input().split())
 
basket = [i for i in range(1, n+1)]
 
for _ in range(m):
  i, j = map(int, input().split())
  basket[i-1:j] = reversed(basket[i-1:j])
 
for k in basket:
  print(k, end=" ")
#print(*basket)
# * 리스트 안에 있는 수들을 풀어서 써주는 역할
