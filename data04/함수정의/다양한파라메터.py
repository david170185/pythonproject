def list_p(x):
    for index in range(len(x)):
        print(index, x[index])

def set_p(x): #x는 set 컬렉션
    for data in x:
        print(data)

def dic_p(x):
    for data in x.values(): #키만 찍고 싶으면 x
        print('값', data)
        print('--------------------------')
        print(x) #딕셔너리 전체 print
        for key in x:
            print('키', key, ':', '값', x[key])

def tuple_p(x):
    for data in x:
        print(data)