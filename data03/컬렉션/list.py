food = ['감자', '양파', '고구마']
food[2] = '국수'

print(food)
print('리스트의 개수', len(food))
print('요소, element', len(food[0]))

##################################

hobby = []
tour = list()
hobby.append('코딩')
hobby.append('등산')
hobby.append('독서')
hobby.append('글쓰기')
print(hobby)
print(len(hobby))

tour.append('제주도')
tour.append('울산')
tour.append('부산')
tour.append('강릉')
tour.append('강남')
print(tour)
print(len(tour))

del tour[0]
print(tour)
tour.insert(0, '신촌')
print(tour)

for x in tour: #리스트를 넣으면 for each
    print(x, end=' ')
print()
for i in range(len(tour)): #0~4
    print(tour[i], end=' ')
print()
###########################################
# buy = [] / wish = list()
# 사고싶은것 5개를 입력받아서 리스트에 넣으세요.!(for문 사용)
# 전체 프린트

buy = []
wish = list()

for _ in range(5): # 0~4
    data = input()
    buy.append(data) #buy.append(input())
    print(buy)

print()
# wish에 들어갈 입력을 다음과 같이 하나의 스트링으로 입력 받아서
# 리스트에 넣고 아래와 같이 출력!
# 입력: 프로그래머, 분석가, 기획가, 마케팅 전문가
# 나는 프로그래머가 되고 싶어요!
# 나는 분석가가 되고 싶어요!
# 나는 기획가가 되고 싶어요!
# 나는 마케팅전문가가 되고 싶어요!

data = input()
data2 = data.split(', ')
print(type(data2))
for x in data2:
    print('나는', x, '가 되고 싶어요!')
