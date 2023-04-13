# 3-1)파이썬에서 띄어쓰기
print("Hello world!")
print("Hello  world!")
print("Hello"+"World")
print("Hello"+" "+"world")

# 3-2)디버깅 연습하기
# print("오늘은 파이썬 챌린지 3일차 입니다)
# print('디버깅 "+" 연습중입니다')
# print('내일은("금요일" + "입니다)')
# print(("그래서 챌린지가 없습니다"))
# 오류 SyntaxError: EOL while scanning string literal

print("오늘은 파이썬 챌린지 3일차 입니다.")
print('디버깅"+"연습중입니다.')
print('내일은(금요일"+"입니다)')
print("그래서 챌린지가 없습니다.야호")
# 따옴표 하나도 가능함

# 3-3)입력함수1
# 입력 input함수 사용

input('당신의 이름은 무엇입니까?')

print('나는'+' '+input('당신의 이름은 무엇입니까?')+' '+'입니다')

# 컨트롤+/ 주석

# 3-4)입력함수2
# 문자열의 길이를 알아볼때 len(s)

print(len(input('당신의 이름은 무엇입니까?')))

# 3-5)파이썬 변수1
# name이라는 변수에 입력값 할당하기

name = input("이름 입력하세요")
print(name)

#이름 입력받고 이름의 길이를 출력해보자
length = len(name)
print(length)

# 3-6)파이썬 변수2
# a와 b의 값을 입력받아서 서로 바꿔보기

a = input('a:')
b = input('b:')

c = a
a = b
b = c

print('a = ' +a)
print('b = ' +b)
# 와 신기


# 3-7)변수 이름 짓기
# 변수명 읽을 수 있고 기억하기 쉽게, 변수명 띄어쓰기ㄴ언더바 사용
# 문법이름은 변수명으로 지을 수 없다.

# 올바른 파이썬 코드는? ㄴ : a = 12

# 종합 챌린지 퀴즈

movie = input('좋아하는 영화를 입력하세요.')
name = input('영화의 주인공 이름을 입력하세요.')

print('현주가 좋아하는 영화는'+' '+movie+'이고, 주인공은'+' '+name+'이다.')