#기본 라이브러리
import math
import random

print(math.sqrt(9.0))
print(random.randint(1, 100))

# 연산자 : 산술, 대입, 비교, 논리
# 산술연산자
x = 100
y = 333
print(x + y)
print(x - y)
print(x * y)
print(x / y) #소수점 포함
print(x % y) #나머지
print(x // y) #소수점 제거(정수 부분만 추출!)

# 대입연산자(=할당연산자)
# 파이썬에서는 변수의 생성과 타입이 값을 대입할 떄 결정된다.
# auto-typing!

#비교 연산자 => 비교의 결과가 논리형
print(x == y)
print(x != y)

a = 10
a *= 10 # a = a * 10
print(a)

#논리 연산자 : and, or, not
id = 'root'
pw = '1234'

print(id == 'root' and pw == '1234')
print(id == 'root' or pw == '1234')

# 멤버쉽 연산자(파이썬만 적용) : in(~안에)
member = ['홍길동', '김길동', '송길동']
print('정길동' not in member) #not 미포함
print('정길동' in member)

#터미널에서 입력
#숫자1 : 333
#숫자2 : 222
#사칙 연산을 수행하고 프린트
num1 = 333
num2 = 222
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#터미널에서 입력
#입력1 : 홍길동
#입력2 : 200
#출력은 홍길동은 200세 입니다.
#100살보다 많으면 나이가 많으시군요! 적으면 아직 어리시군요!

name = '홍길동'
age = 200
print(name,'은', age, '세 입니다.')
if age > 100:
    print('나이가 많으시군요!')
else:
    print('아직 어리시군요!')

#변수에 대입
#hobby = '달리기'
#time = 10
#달리기를 10시간 했습니다.
#오늘 한 운동이 '달리기'이고, 시간이 10시간 이상이면 => 오늘 '달리기'는 충분
#오늘 한 운동이 '달리기'이거나, 시간이 10시간 이하이면 => 어떤 운동이는 시작하세요!!

hobby = '달리기'
time = 10
print(hobby,'를', time, '시간 했습니다.')
if hobby == '달리기' and time >= 10:
    print('오늘', hobby, '는 충분')
elif hobby == '달리기' or time < 10:
    print('어떤 운동이든 시작하세요!')