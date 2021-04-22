#for문을 사용해보세요 #range
#range(20) print!
for x in range(1, 21, 1):
    print(x)

#1부터 100까지 프린트!
for y in range(1, 101, 1):
    print(y)

#0부터 200까지 프린트!
for z in range(201):
    print(z)

#1부터 100까지 중 2씩 점프해서 프린트!
for i in range(1, 101, 2):
    print(i)

#100부터 500까지 중 5씩 점프해서 프린트!
for i2 in range(100, 501, 5):
    print(i2)

#100부터 500까지 중 10씩 점프해서 모두 더해서 프린트!
sum2 = 0
for i3 in range(100, 501, 10):
    sum2 = sum2 + i3
    print(sum2)

#3부터 200까지 중 8씩 점프한 값을 모두 곱해서  프린트!
sum3 = 1
for i4 in range(3, 201, 8):
    sum3 = sum3 * i4
    print(sum3)

#food = ['감자', '고구마', '양파']를 다음과 같이 프린트!
# - 감자짱!
# - 고구마짱!
# - 양파짱!
# - 감자짱! 고구마짱! 양파짱!
food = ['감자', '고구마', '양파']
for f in food:
    print(f, '짱!')
for f in food:
    print(f, '짱!', end=" ")
#food2 = "감자 고구마 양파 스프 국수 라면"을 다음과 같이 프린트!
#감자 맛있어! 고구마 맛있어! 양파 맛있어! 스프 맛있어! 국수 맛있어! 라면 맛있어!
food2 = ['감자','고구마','양파','스프','국수','라면']
for f2 in food2:
        print(f2, '맛있어!', end=" ")

food3 = "감자 고구마 양파 스프 국수 라면"
food_list = food3.split()
for f3 in food_list:
    if f3 not in ['양파', '국수']:
        print(f3 + "맛있어! ", end=' ')