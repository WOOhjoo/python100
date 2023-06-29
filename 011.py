# List indexing을 이용한 slicing
# list1 = [1,2,3,4,5,6,11,'a','b']
# list2 = [11,12,13]
# list12 = list1+list2
# print(list12, len(list12))
# print(list12[:]) #전체범위
# print(list12[::2]) #처음 시작부터 2의 간격으로 출력댐

# List 대체하고 지우기
# list1 = [1,2,3,4,5,6,11,'a','b']
# list2 = [11,12,13]
# list12 = list1+list2

# list12[0:3] = ['one','two','three'] #0:3 자리에 원투쓰리 넣기
# print(list12)
# list12[0:3] = [] #0:3 부분 지우기
# print(list12)

# del list12[-1] #인덱스로 지우기..
# print(list12)
# del list12[::2] #첫 인덱스부터 2의 간격에 잇는 인덱스들 삭제
# print(list12)
# del list12[:] #전체범위 삭제
# print(list12) # []

# #list 자체 삭제하기
# del list12
# print(list12) # 아예 삭제되어 에러

#.sort 오름차순 정렬하기
# 원본 내용을 바꾸지 않고, 정렬한 값을 반환한다.
# List, tuple, Dictionary, str에 모두 사용 가능하다.
# key 를 통하여 정렬할 기준을 정할 수 있다.
# reverse 가 True이면 내림차순, False이면 오름차순으로 정렬된다.

# numbers = [7,2,5,4,3,6,1,9,8,15,11]
# numbers.sort(reverse=True) #내림차순으로 정렬하기 [15, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(numbers)
# numbers.reverse() #순서 바꾸기 [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15]
# print(numbers)

#list 정렬하기
# string = 'How is the weather today?'
# string = string.split() #.split 단어별로 나누기

# print(string, type(string)) #['How', 'is', 'the', 'weather', 'today?']

# string.sort(key=len) #길이로 정렬하기
# print(string, type(string)) #['is', 'How', 'the', 'today?', 'weather']
# string1 = sorted(string)
# print(string1)

#sort와 sorted의 차이
# sort() 함수는 리스트를 제자리에서(in-place) 수정함
# sorted() 함수는 새로운 정렬된 리스트를 만들어줌

# 제자리에서 수정한다는 말은 쉽게 말해 원본 리스트 자체를 수정하지만, 그 결과를 반환해주진 않는다(None)는 뜻임
# sort() 함수는 원본 리스트가 변경되어버리지만 sorted() 함수의 경우 원본에는 영향 없이, 새로운 정렬된 리스트를 반환해줌

# numbers = [7,2,5,4,3,6,1,9,8,15,11]
# string = 'How is the weather today?'
# string = string.split()

# print(12 in numbers) # numbers에 12가 잇냐?는 뜻.. 있으면 True 없으면 False
# print(12 not in numbers) #numbers에 12가 업냐?는 뜻... 없으면 True 있으면 False
# print('How' in string) #대소문자 구별함

#.insert()
# string = 'How is the weather today?'
# string = string.split()
# string.insert(4, 'here') #0,1,2,3,4번째 자리에 here 끼워넣기
# print(string) #['How', 'is', 'the', 'weather', 'here', 'today?']

#.append()  /  remove()
# string = 'How is the weather today?'
# string = string.split()
# string.append('Maybe') #마지막에 추가
# print(string)
# string.remove('today?') #특정 요소 삭제하기
# print(string)

#.extend() 하나 이상의 요소를 더하기
# string = 'How is the weather today?'
# string = string.split()

# string.extend(['It','is','going','to','rain','soon'])
# #extend 대신에 + 연산자를 써서
# #print(a_string+(['It','is','going','to','rain','soon'])) 해도됨
# print(string)

#.clear() 지우기
# string = 'How is the weather today?'
# string = string.split()
# string.clear() #리스트에 있는 요소 지우기
# print(string) #[]

#.copy()
# numbers = [7,2,5,4,3,6,1,9,8,15,11]
# print(numbers)
# copied = numbers.copy() # copied = umbers[:]
# print(copied)
# print(numbers.copy()) #이렇게 해두댐


#다양한 방법으로 같은 결과..
#range(시작, 끝, 증가값)

# list1 = list(range(0, 10, 2))
# # 0부터 9까지 숫자 중에서 2씩 증가
# # list() 함수를 사용하여 해당 범위의 숫자들을 리스트로 변환
# print(list1) #[0,2,4,6,8]

# list2 = [ i for i in range(0,10,2)]
# # 0부터 9까지의 숫자 중에서 2씩 증가하는 숫자들을 리스트로 생성
# print(list2) #[0,2,4,6,8]


# list3 = [i for i in range(0,10) if i%2 != 0]
# # 0부터 9까지의 숫자 중에서 홀수인 숫자들만 리스트로 생성
# # if 문을 사용하여 i % 2 != 0인 조건을 만족하는 경우에만 리스트에 추가됨
# print(list3) #[1, 3, 5, 7, 9]


# string = 'How is the weather today?'
# string = string.split()
# list_op = [i**2 for i in range(0, 10, 2)] #i의 2승.. 0부터 9까지의 숫자 중에서 2씩 증가하는 숫자들을 제곱하여 리스트로 생성
# print(list_op) #[0, 4, 16, 36, 64]
# list_up = [i.upper() for i in string] #.upper() 문자열 메소드로, 문자열을 대문자로 변환
# print(list_up) #['HOW', 'IS', 'THE', 'WEATHER', 'TODAY?']

# list_gen = (i**2 for i in range(10) if i % 2 == 0) 
# #range(10)은 0부터 9까지의 숫자를 생성
# #if i % 2 == 0 조건은 숫자가 짝수인 경우
# #i**2는 선택된 숫자의 제곱 값을 의미
# #0부터 9까지의 짝수를 제곱한 값들을 생성

# print(list_gen)
# list_gen1 = [i+4 for i in list_gen] 
# print(list_gen1)

#--------------------------------------------------------------

# list3 = list(range(0, 25)) #range() 함  0부터 24까지의 숫자 생성
# print(list3)
# def is_multiple3(x):
#     return x % 3 == 0 
# # x가 3의 배수인지 확인하고 결과를 반환
# # x % 3 == 0은 x를 3으로 나누었을 때 나머지가 0인지를 확인
# # 반환값은 x가 3의 배수일 경우 True, 아니면 False



# list4 = list(filter(is_multiple3, list3))
# # filter() 함수를 사용하여 list3의 요소들 중에서 is_multiple3 함수의 조건에 맞는 요소들만 필터링하여 리스트로 만듦
# # filter() 함수는 첫 번째 인자로 필터링할 함수를, 두 번째 인자로는 필터링 대상이 되는 시퀀스를 받음 
# # list4에는 list3에서 3의 배수인 요소들로 이루어진 리스트가 생성

# print(list4) #[0, 3, 6, 9, 12, 15, 18, 21, 24]

#------lambda로 더 간단하게 코딩하기
# list3 = list(range(0, 25))
# print(list3)

# list4 = list(filter(lambda x: x % 3 == 0 , list3 ))
# print(list4)

#-------
list3 = list(range(0, 25))
print(list3)
list4 = list(filter(lambda x: x % 3 == 0 , list3 ))
print(list4)
# map도 맞춰서 생성하는거고 lazy evaluation 이라고도 부릅니다.
# 빵틀만 만들어놓고 여러 빵을 찍어낼 수 있다.
# 추후 필요에따라서 할 수 있는거 lazy evaluation
print(list(map(lambda x: x**2, list4)))
print([i**2 for i in list4])

print('-----------------------------------')

list3 = list(range(0, 25))
print(list3)
list4 = list(map(lambda x: x**2, filter(lambda x: x % 3 == 0, list3)))
print(list4)

print('-----------------------------------')
#----
list3 = list(range(0, 25))
print(list3)
list4 = [x**2 for x in list3 if x % 3 == 0]
print(list4)

print('-----------------------------------')
car = ['abc', 'defg', 'ZZZ', 'awesdf', 'sonata' , 'Excel', 'Mini' ]
car.sort(key=len)
print(car)
print(sorted(car))
print(min(car),max(car))
# 아스키 코드값 min, max
car2 = max(car, key=lambda i : i.lower())
# 대문자 먼저, 소문자 나중에라서 lower
print(car2)

print('-----------------------------------')

player = ['A', 'B' , 'c' ,'d', 'efg']; goals = [7,20,15,7 ]
for last_name, goal in zip(player, goals):
    print(f'{last_name}: {goal}')

