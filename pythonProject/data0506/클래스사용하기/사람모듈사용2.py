from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day):
#파이썬 : 클래스간 다중 상속이 가능하다.
#자바 : 클래스간 단일 상속만 가능하다.
    def __init__(self, doing, time, location):
        my.Day.__init__(self, doing, time, location)
        #단일 상속인 경우 super.__init(self, 파라메터값 나열)
    def free(self):
        print('쉬다.!')

    def __str__(self):
        return self.doing + ', ' + str(self.time) + ', ' + self.location

if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 20, '마포구')
    woman_day1.free()
    woman_day1.eat()
    print(woman_day1)