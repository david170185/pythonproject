# 문제1 : exam01()
def login(id, name):
    print('아이디가' + id + '인' + name + '님이 로그인 되었습니다.')
# 문제2 : exam02()
def cal(x, y):
    print('-----------------')
    print('두수의 합은', x + y)
    print('두수의 차는', x - y)
    print('두수의 곱은', x * y)
    print('두수의 나눗셈은', x / y)
    print('두수의 나머지는', x % y)
# 문제3 : exam03()
def age(name2, age):
    age2 = int(age) + 10
    print(name2 + '의 10년후의 나이는' + str(age2) + '세 입니다.')
# 문제4 : exam04()
def allowance(money):
    if money >= 10000:
        print('엄마 용돈이 너무 많아요.')
    else:
        print('엄마 용돈이 너무 적어요.')
# 문제5 : exam05()
def ood_even(num):
    if num % 2 != 0:
        print('홀수 입니다.')
    else:
        print('짝수 입니다.')
# 문제6 : exam06()
def sales_recourds(target):
    if target >= 1000:
        print('축하합니다. 실적을 달성 하셨습니다.')
        print('당신의 이번달 보너스는' + str(int(target * 0.2)) + '만원 입니다.')
# 문제7 : exam07()
def missile(name3, start, move):
    print('-----------------------------------')
    num2 = start + move
    print(name3 + '미사일의' + str(num2) + '로 이동 되었습니다.')
# 문제8 : exam08()
def receipt(money2, buy):
    print('받은돈', money2)
    print('상품의 총액', buy)
    print('부가세', int(buy * 0.1))
    print('잔돈', money2 - buy)
# 문제9 : exam09()
def star():
    for _ in range(1000):
        print('*', end='')
