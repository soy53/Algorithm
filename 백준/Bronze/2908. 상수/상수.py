a, b = input().split()
 
a_re = int(a[::-1])
b_re = int(b[::-1])
 
if a_re > b_re:
  print(a_re)
else:
  print(b_re)