data = input()
result = []
value = 0

for i in data:
  if i.isalpha():
    result.append(i) # 알파벳인 경우 result 리스트에 넣기
  else:
    value += int(i) # 숫자인 경우 value에 더하기

result.sort() # result 오름차순 정렬

if value != 0:
  print(''.join(result) + str(value))
        # value가 0이 아니라면 result 문자열로 변경 + value