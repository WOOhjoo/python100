#Data Types : String / Integer / Float / Boolean

#4-1 글자수 세기
print(len("hello"))
print(len(12345))
print("hello"[0])
print("hello"[4])
print("hello"[2])
print("hello"[1])
print(len("12345"))

# 퀴즈 4-1)
# 1. b 문자열
print(type(932)) #<class 'int'>
print(type("false")) #<class 'str'>
print(type(857.25)) #<class 'float'>
print(type("523")) #<class 'str'>

# 2. d 실수
mystery = 734_529.678
print(type(mystery)) #<class 'float'>

# 3. 영2
street_name = "동산면 영서로 1290-31"
print(street_name[4] + street_name[9])

#4-2 type()함수 데이터 형식 확인

#데이터 유형 바꾸기 첫번째 방법

num_char = len(input("당신의 이름은 무엇입니까?"))
print(num_char) 


# 괄호 안에 문자열로 변환하려는 변수 값을 넣고 새변수 만들기
new_num_char = str(num_char)
print(type(new_num_char))

print(new_num_char)
print("당신의 이름은 " + new_num_char+ " characters.")


#데이터 유형 바꾸기 두번째 방법

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))


#퀴즈 4-2)
a=input("2자리의 숫자입력:")

print(a[0]+a[1]) #더하기가 안됨,,,,,,,,,,,

print(int(a[0])+int(a[1])) #호진이한테 물어봐서 햇습니다



# 4-3) 파이썬의 수학연산 (+,-,*,/)
#단 같은 라인에 연산을 할때 
# 괄호 안에 있는거 먼저, 
# 그 다음에 지수, 
# 곱셈, 
# 나눗셈, 
# 더하기, 
# 빼기 순


#4-4)BMI 계산기 BMI지수= 몸무게(kg) ÷ (신장(m) × 신장(m))
height = input("키를 입력하세요(m) : ")
weight = input("몸무게를 입력하세요(kg) : ")

bmi = float(weight) / (float(height)*float(height))

print(int(bmi)) #너무 길게 소수점이 나오니까 정수로 변경



#4-5) 파이썬의 숫자처리 및 F-string
# round() 반올림함수
# floor // 소수점 뒤에 숫자 다 버림
# (f"{}") F-string 서로 다른 데이터 유형을 문자열로 처리하는 것

print(8/3)
print(8//3)
print(int(8/3))
print(float(8/2))
print(round(8/3)) #반올림
print(round(8/3,2)) #소수점 두번째자리에서 반올림
print(round(3.4153435,1))



score = 0 #정수
height = 1.8 #실수
earth = True #Boolean

print(f"스코어는 {score},키는 {height},지구인?{earth}")

