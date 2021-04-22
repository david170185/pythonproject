class Day:
    #실제값 변수 : 인스턴트 변수(동적변수)<->정적변수
    doing = None
    time = 0
    location = None

    def __init__(self, doing, time, location):
        self.doing = doing
        self.time = time
        self.location = location
        Day.count = 1 #1씩 증가
        print(str(Day.count) + '개 객체가 생성됨.')

    def study(self):
        return self.doing + '를' + str(self.time) + '시간 하다.'

    def where(self):
        return self.location + '에서' + self.doing + '를 하다.'

    def __str__(self):
        return self.doing + ' ' + str(self.time) + ' ' + self.location

if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    day2 = Day('자바공부', 11, '신촌')
    day3 = Day('db공부', 12, '종로')

    print(day1)
    print(day2)
    print(day3)

    print(day1.study())
    where_value = day1.where()
    print(where_value)