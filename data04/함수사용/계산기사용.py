from 함수정의.계산기 import *

data1 = int(input('숫자1>> '))
data2 = int(input('숫자1>> '))

result1 = add(data1, data2)
#변수에 넣거나, 프린트 할 수 있는경우는 return!
#print(add(data1, data2))

result2 = minus(data1, data2)
result3 = mul(data1, data2)
result4 = div(data1, data2)

print(data1, '+', data2, '=',  result1)
print(data1, '-', data2, '=',  result2)
print(data1, '*', data2, '=',  result3)
print(data1, '/', data2, '=',  result4)

#계산기에 프린트값이 출력 => 메인 추가시 미출력


