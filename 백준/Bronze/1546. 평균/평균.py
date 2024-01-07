n = int(input())
 
n_list = list(map(int, input().split()))
m = max(n_list)
new_mean = 0
 
for i in n_list:
  new_score = i/m*100
  new_mean += new_score
 
print(new_mean/len(n_list))