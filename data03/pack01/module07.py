# 반복문 while
# 조건에 맞으면 여러번 반복(한정적)
# 한정적 횟수만큼 반복하고자 하는 경우는
# 시작값, 증가값, 종료값
start = 1
end = 10
plus = 1

# while start <= end: # 조건이 True
#     print(start)
#     start = start + plus

# 조건에 맞는동안 계속 반복(무한반복)


# 반복문 for
for _ in range(start, end+1, plus): # _ : 범위만큼만 반복
    print('내가 반복됨')

for _ in range(1, 11, 1): #(1, 11, 1) 카운트 용도
    print('나도 반복됨.')

for x in range(1, 11, 1):
    print(x)

sum2 = 0
for x in range(1, 11): #1 2, 3, 4, 5,
    sum2 = sum2 + x

print(sum2)

r = [1,2,3,4,5,6,7,8,9,10]
for x2 in r:
    print(x2)

names = ['홍길동', '김길동','박길동']
for n in names:
    print(n)

r2 = [100, 200, 300, 400, 500]
for x3 in r2:
    print('해당값>>', x3)
    if x3 == 300:
        print('300을 찾음')
        break #continue

for x4 in range(5): #default 값 0번부터 시작 1씩 증가
    print(x4)

