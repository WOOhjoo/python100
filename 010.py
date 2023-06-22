#파이썬은 데이터를 처리를 위한 언어
#데이터를 저장하고 다루는 방법..
# list / tuples / dictionary, set 4가지

#-------------------------------------------------------
#### 1.list ####
#리스트 생성하는 방법은 element를 []대괄호 사용해서 감싸는 것
#리스트 안의 값은 elements 또는 item 이라고 부른다
#리스트안에 리스트를 넣을 수 있음..중첩리스트라고 함

# list1 = [1, 2, 3,4,5, 6, 11, 'a', 'b' ] #리스트는 띄어쓰기 알아서댐
# print(type(list1), list1)


# #인덱스 예시
# print(list1[1], list1[7])
# print(list1[2:5]) #2부터 5까지 0부터 시작..근디 5는 포함 안댐
# print(list1[:7]) #숫자 지정 안하면 처음부터
# print(list1[4:]) #숫자지정 안하면 끝까지임
# print(list1[-1]) #-1 뒤부터
# print(list1[-4:]) # 뒤에서 4번째까지
# print(list1[1+2:])

# #리스트 추가
# list1[6] = 'c' #기존에 list1[6]에 잇던 값 업서지고 c가 들어감
# print(list1)

# print(len(list1))


# list2 = [] #비워둬도댐
# for item in range (11, 14, 1):
#     list2 = list2 + [item]
# print(list2)


# #string
# list3 = []
# list3 = list3 + 'Python'
# print(list, len(list3))

# list3 = list3 + ('S','t','u','d','y')
# print(list3, len(list3))

#리스트 연결하기
# list1 = [1,2,3,4,5,6,11,'a','b']
# list2 = [11,12,13]
# list12 = list1 + list2
# print(list12)

# #인덱스와 엘리먼트 동시에 찍기
# for i in range(len(list12)):
#     print(f'({i},{list12[i]})', end = '')



#-----------------------------------------------------
#### 2.tuples ####
#수정이 불가능, 메모리를 적게 차지한다
#()괄호 사용, 콤마로 값이 나누어짐
#element를 하나 가진 튜플을 생성하기 위해 마지막에 콤마를 추가해야한다
# tu1 = ('a')
# print(type(tu1)) # class 'str'

# tu2 = ('a',)
# print(type(tu2)) #class 'tuple'


t1 = 10, 20, 30, 'Jhon'
t1 = t1 + (40,50)
print(type(t1))



# t3 = 'A', 'B', 'C', [90, 80, 70]
# print(len(t3))

t4 = (('A', 'B', 'C'),[90, 80, 70])
print(len(t4))

grade, number = t4
print(grade, number, type(grade), type(number))

#모든 배열 언패킹 가능하다
num1, num2, num3 = number
print(num1,num2,num3)

#문자열도 가넝한
first, second, third, fourth = 'WIFI'
print(first, second, third, fourth)