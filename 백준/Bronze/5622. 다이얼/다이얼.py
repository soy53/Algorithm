# 나의 풀이
s = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

seconds = 0
for i in s:
  for j in dial:
    if i in j:
      seconds += (dial.index(j) + 3)

print(seconds)

# 아스키 코드 이용
dial = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
seconds = 0

s = input()

for i in range(len(s)): 
  seconds += dial[ord(s[i])-ord('A')]
  # dial -> [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
  # dial[ord(s[i])-ord('A')]는 dial에서 해당 알파벳의 인덱스를 나타냄

print(seconds)
