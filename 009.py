# for문 기본구조
# for 변수 in 리스트(또는 튜플, 문자열)
# for item in list_of_items:
# for문과 list 함께 사용하면 리스트의 각 항목을 대상으로 작업을 검토할 수 있다.

# fruits = ['사과','복숭아','배']
# #리스트 생성

# for fruit in fruits:
#     print(fruit)
# #for문을 사용해서 리스트 안에 있는 항목을 하나씩 출력
#     print(fruit + '파이')
#     print(fruits) #들여쓰기(반복문 내부,외부) 햇을때랑 결과가 ㄷ라므


#-------------------------------------
#평균키 구하기
#우리반 학생의 키 리스트 = [180, 154, 165, 173, 180, 169, 146]
#모든사람의 키를 더하고 학생수로 나누고, 정수를 반올림해서 평균을 구하기

# student_heights = input("학생들 키 리스트를 입력하세요! 입력시 띄어쓰기로 값 구분하기").split()

# student_num = len(student_heights)
# print(student_num)


# # 매개변수가 한개이면 0부터 매개변수-1까지
# # 두개이면 앞에잇는거 시작값으로 사용 뒤에잇는거-1까지
# # 세개면 시작값,증가,마지막깢

# # 0부터 student_num-1까지 반복 input으로 입력한거 int로 바꿔주기
# for n in range(0, student_num):
#     student_heights[n] = int(student_heights[n])

# #평균구하기
# height_avg = sum(student_heights)/student_num

# print(round(height_avg))

#---------------------------------------------------------------
#또 다른 평균키 구하는방법
# student_heights = input("학생들 키 리스트를 입력하세요! 입력시 띄어쓰기로 값 구분하기").split()

# student_num = len(student_heights)
# print(student_num)

# for n in range(0, student_num):
#     student_heights[n] = int(student_heights[n])

# #for 변수 in 리스트(또는 튜플, 문자열)

# total_height = 0
# for height in student_heights:
#     total_height = total_height + height
#     #total_height += height

# print(total_height)

# num_of_students = len(student_heights)
# height_avg = round(total_height/num_of_students)
# print(height_avg)


# #---------------------------------------------
# #또 다른 방벙
# student_heights = input("학생들 키 리스트를 입력하세요! 입력시 띄어쓰기로 값 구분하기").split()

# student_num = len(student_heights)
# print(student_num)

# for n in range(0, student_num):
#     student_heights[n] = int(student_heights[n])


# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# num_of_students = 0
# for student in student_heights:
#     num_of_students += 1
# print(num_of_students)

# height_avg = round(total_height/num_of_students)
# print(height_avg)

#----------------------------------------------------------

#리스트에서 가장 높은 값 구하기
#학생들 점수 중 가장 높은 점수 구해보자

# student_scores = input("점수 입력(스페이스로 구분하세요)").split()
# #student_scores = [78 65 89 86 55 91 64 89]

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# high_score = 0
# for score in student_scores:
#     if score > high_score:
#         high_score = score
# print(f'가장 높은 점수는 : {high_score}요')

#---------------------------------------------------------

#for반복문과 range()함수
# for number in range(1,11):  #number변수에 1부터 11까지(11포함안됨) 저장하라는 ㄷ뜻
#     print(number)

# for number in range(1,10,3): #3 간격으로
#     print(number)


# 1부터 100까지 더하기
#total = 0
# for number in range(1,101):
#     total = total + number
# print(total)

#짝수 더하기 1~100까지
#첫번째 방법
# for number in range(2,101,2):
#     total = total + number
# print(total)

#두번째 방법
# for number in range(1,101):
#     if number % 2 == 0:
#        total = total + number
# print(total)

#--------------------------------------------
#Fizzbuzz게임
#1 2 피지 4 버즈 피지 7 8 피지 버즈 11 피지 13 14 피지버즈
# 3피지 6피지 9피지 12피지 15피지 3의 배수
# 5버즈 10버즈 15버즈 5의 배수
# 둘이 겹칠때 피지버즈

# for number in range(1,30):
#     if number % 3 == 0 and number % 5 == 0:
#        print('피지버즈')
#     elif number % 5 == 0:
#        print('버즈')
#     elif number % 3 == 0:
#        print('피지')
#     else:
#        print(number)



#--------------------------------------
#비밀번호 생성기
#문자를 몇개 넣을까요?
#기호는 몇개 넣을까요?
#숫자는 몇개 넣을까요?
#생성된 비번

import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("안전한 비밀번호 생성기입니다!")
ct_letter= int(input("몇자리의 비밀번호를 원하십니까?\n ")) 
ct_symbol = int(input(f"기호는 몇개를 넣을까요?\n "))
ct_number = int(input(f"숫자는 몇개를 넣을까요?\n "))


random.shuffle(letter)
select_let = letter[:ct_letter]
#print(select_let)

random.shuffle(number)
select_num = number[:ct_number]
#print(select_num)

random.shuffle(symbol)
select_sym = symbol[:ct_symbol]
#print(select_sym)

# sum = [select_sym,select_let,select_num] 이렇게 했다가 안됨..지피티한테 물어봄
# print(sum) .extend()로 넣어야댐
sum = []
sum.extend(select_sym)
sum.extend(select_let)
sum.extend(select_num)
print(sum)

random.shuffle(sum)

password = ''.join(sum)
#join() 문자열과 리스트의 요소를 결합해서 새로운 문자열 생성
# ''는 요소들 사이에 아무런 문자도 추가하지 않는다는 것을 의미합니다. 
# 따라서 join() 메소드에 의해 반환된 결과는 모든 요소들이 이어진 하나의 문자열입니다.


print(f'생성된 비밀번호는 {password} 입니다')