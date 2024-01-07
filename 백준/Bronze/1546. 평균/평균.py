# 나의 풀이
n = int(input())
 
n_list = list(map(int, input().split()))
m = max(n_list)
new_sum = 0
 
for i in n_list:
  new_score = i/m*100
  new_sum += new_score
 
print(new_sum/len(n_list))

# 더 짧고 간단한 풀이
n = int(input())
n_list = list(map(int,input().split()))
print(sum(n_list)/max(n_list)*100/n)
