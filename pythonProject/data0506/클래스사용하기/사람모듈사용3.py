from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class Student(Person, my.Day):
#파이썬 : 클래스간 다중 상속이 가능하다.
#자바 : 클래스간 단일 상속만 가능하다.
    def __init__(self, doing, time, location):
        my.Day.__init__(self, doing, time, location)

    def study(self):
        print('공부하다.!')

    def __str__(self):
        return self.doing + ', ' + str(self.time) + ', ' + self.location

if __name__ == '__main__':
    student_day1 = Student('진짜 놀기', 20, '마포구')
    student_day1.study()
    print(student_day1)

print('========================')

class Worker(Person, my.Day):

    def __init__(self, doing, time, location):
        my.Day.__init__(self, doing, time, location)

    def work(self):
        print('일하다.!')

    def __str__(self):
        return self.doing + ', ' + str(self.time) + ', ' + self.location

if __name__ == '__main__':
    worker_day1 = Worker('진짜 놀기', 20, '마포구')
    worker_day1.work()
    print(worker_day1)