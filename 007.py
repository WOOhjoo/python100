#다중 연속 if문
#롤러코스터 매표기 만들기
#120cm이상 탈 수 있다.
#나이가 18세 이상이면 12,000원, 미만이면 7,000원
#경로우대할인으로 65세이상 70이하는 3,000원

# print('롤러코스터')

# height = int(input('당신의 키는 몇cm입니까?'))
# bill = 0


# if height>=120:
#    print('표를 예매해주세요') 
#    age = int(input('나이를 입력해주세요'))
#    if age < 12:
#       bill = 0  
#       print('무료입니다.') 
#    elif age >= 18 and age < 65:
#       bill = 12000
#       print('12,000원입니다')  
#    elif age >= 65 and age <= 70:
#       bill = 3000
#       print('경로우대 할인되어 3,000원 입니다.')   
#    else:
#       bill = 7000
#       print('7,000원 입니다.')
     

# else:
#    print('120cm미만은 탈 수 없습니다.')


# photo = input("사진 찍? Yes(Y) , No(N)")  
# if photo == 'Y':
#    bill += 1000 
# else:
#    bill += 0

# print(f'총 금액은 {bill}')


#피자를 주문하는 자판기 만들기
#피자 사이즈 s,m,l 각 금액 15, 20, 30,
# 페페로니 추가 2, 치즈추가 3,000
# 총 지불할 금액은? 

# print('피자 자판기')

# size = input('피자 사이즈를 정해 (S) or (M) or(L)')
# bill = 0

# if size=='S':
#    bill = 15000
#    print('15,000원 입니다.')

# elif size=='M':
#    bill = 20000
#    print('20,000원 입니다.')

# elif size=='L':
#    bill = 30000
#    print('30,000원 입니다.')

# add = input('추가? 치즈 C 페퍼로니 P 안할거면 n')
# if add == 'C':
#    bill += 3000
# elif add =='P':
#    bill += 2000
# else:
#    bill += 0

# print(f'총 금액은 {bill}입니다')


# .lower()는 대문자를 소문자로 바꿈
# .count() 괄호 안에 있는 특정 알파벳의 개수를 셀 수 있음
# print('영단어 두개 입력하세')
# word1 = input('영어단어1 : ')
# word2 = input('영어단어2 : ')

# english_word = word1 +' '+ word2
# lower_word = english_word.lower()
# count_word = lower_word.count('a') 

# print(count_word)
# print(lower_word)


# print(''' 
#              ,;;;.
#              |-,-:
#             _'._,'_
#          ,-' \\-// `-.
#          |`. {|} ,'|
#          | |`_.._-'| |
#          | |(,'\_).'-|
#          `.__,-'-.__,',
#            |==='===| _/`,
#           / +`. __.'\,-\
#           |+ |`'\ | 영형
#           | ++ `--'+|
#           |__+_+_|__|
#          ,'| | \ \
#         '-')__( |__|
#            [||] [||]
#            | | | |
#       _,.--|__|''|__''--.._
#    ,-' _,-'; | _| ,\ _,-'`-.
#   (_,-' (__/-' '.__)' _,-')
#   |`-._ _,-' _,-' _,-'_,-'|
#    `-._`'---..'......'--''_,-'
#      | `'---.........---''|
#      | | | | | |
#      | | | | | |
#      | | | | | |
#      | | | | | |
#      | | '-' | |
#      | | | |
#      '-' | | ''')

# print('보물찾기 게임')
# 갈림길에서 왼/오 선택 오른쪽 죽음
# 왼쪽은 호수로 감
# 호수에서 기다릴지 수영할지 고름
# 수영하면 주금
# 마지막으로 빨노파 문 나타남
# 노란색 문안에 보물
# 빨문 불구덩이 파문 바다에 빠짐


# name = input('닉네임을 입력하세요')

# print(f'{name}은 갈림길에 도착했습니다.')
# choice1 = input('오른쪽으로 갈 지 왼쪽으로 갈 지 선택하세요 (R)or(L)')
# if choice1 == 'L':
#    print(f'{name}은(는) 호수에 도착했습니다')
#    choice2 = input('호수에서 수영을 하시겠습니까? (Y)or(N)')
#    if choice2 == 'N':
#       print(f'수영을 마치고 세개의 문 앞에 도착했습니다')
#       choice3 = input('빨간색 문(R) 노란색 문(Y) 파란색 문(B)')
#       if choice3 == 'Y':
#          print(f'{name}은(는) 보물을 발견했습니다!')
#       elif choice2 =='R':
#          print(f'{name}은(는) 불구덩이에 빠졌습니다\ngame over')
#       else:
#          print(f'{name}은(는) 바다에 빠졌습니다\ngame over')   
#    else:
#       print('물에 빠졌습니다\ngame over')   
# else:
#    print('game over')


#난수생성
#ranmdon
#.randint(,)

# import random
# random_int = random.randint(1,10) #1과 10사이의 수를 랜덤으로 추출함
# print(random_int)


#모듈만들기
# import random
# import module #모듈 불러오기 파일명

# print(module.pi) #파일명,변수명 



#부동소수점 난수생성
random_float = random.random() #0~1 소수점출려ㅓㄱ
print(random_float)

random_float = random.random()*5 # 0~4.99999사이의 소수점출력
print(random_float)


#로또번호를 생성해보자

import random

print('번호 6개 선택하세요')

num1 = int(input('1~45 중 첫번째 번호를 입력하세요'))
num2 = int(input('1~45 중 두번째 번호를 입력하세요'))
num3 = int(input('1~45 중 세번째 번호를 입력하세요'))
num4 = int(input('1~45 중 네번째 번호를 입력하세요'))
num5 = int(input('1~45 중 다섯번째 번호를 입력하세요'))
num6 = int(input('1~45 중 여섯번째 번호를 입력하세요'))

my_num = [num1,num2,num3,num4,num5,num6]
my_num.sort() #오름차순 정렬
print(f'내가 고른 번호{my_num}')

#컴퓨터가 고른 번호

lotto = list(range(1,46))
random.shuffle(lotto)
select_num = lotto[:6]
select_num.sort()
print(f'이번주 당첨 번호는 {select_num}')

if select_num == my_num:
    print('당첨입니다.')
else:
    print('꽝')

