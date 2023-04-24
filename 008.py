
#list 순서가 중요
#리스트에 하나만 추가할 때 .append()함수 사용
#여러개 추가할 때, .extend()함수 사용

# student = ['현주','선아']
# student.append('세희')
# print(student)

# student.extend(['아라','호진'])
# print(student)

# print(student[0])
# print(student[-3]) #뒤부터 세기


# len()함수로 리스트안에 몇개가 있는지 알 수 잇
#split() 문자열을 특정 기호에 따라 구분
#아이스크림 내기하기
#참여할사람 이름 입력받기
#몇명인지 확인하기
#명수 구한후 랜덤으로 n번째에 있는사람이 아이스키림 쏘기

# import random

# name = input('아이스크림 내기 참여할 사람들 이름을 입력, 쉽표를 사용해서 이름을 구분해')

# names = name.split(',')

# num = len(names)

# choice = random.randint(0,num-1)

# icecream = names[choice]
# print(f'{icecream}(이)가 아이스크림 쏘기')




#중첩리스트=[리스트1,리스트2]
#nct멤버 구분하기
# member = ['마크','태일','해찬','도영','천러','제노','재민','재현','유타','런쥔','태용']

# nct127 = ['마크','태일','도영','재현','유타','태용']
# nctdream = ['해찬','천러','제노','재민','런쥔']

# nct = [nct127,nctdream]
# print(nct[0][1]) #nct127에서 2번째 값
# print(len(member))



#가위바위보 게임

# import random

# rock = '''
#        ,--.--._
# ------" _, \___)
#         / _/____)
#         \//(____)
# ------\ (__)
#        `-----"

# '''

# scissors = '''
#    ____
#   / __ \
#  ( (__) |___ ___
#   \________,' """""---- .....____
#    _______< () dd ____----'
#   / __ __`.___-----""""
#  ( (__) |
#   \____/

# '''

# paper = '''
#         __________      
#       _(_____ `---  
#      (______ VK
#     (_______            
#     (__________         
#           (_______.---  
# '''

# img = [scissors, rock, paper]


# my_choice = int(input('무엇을 내시겠습니까? 가위(0) or 바위(1) or 보(2)'))

# if my_choice >= 3 or my_choice < 0:
#    print('잘못입력했습니다.')

# else:
#    print('나의 선택은')
#    print(f'{img[my_choice]}')

#    computer = random.randint(0,2)
#    print('컴퓨터의 선택은')
#    print(img[computer])

# # 가위0 바위1 보2
# # 0 = 0, 0 < 1, 0 > 2
# # 1 > 0, 1 = 1, 1 < 2
# # 2 < 0, 2 > 1, 2 = 2 

#    if my_choice == computer:
#       print('비겼다')
#    elif my_choice == 2 and computer==0:
#       print('컴퓨터가 이김')
#    elif my_choice == 0 and computer==2:
#       print('내가 이김')     
      
#    elif my_choice > computer:
#       print('내가 이김') 
#    elif my_choice < computer:
#       print('컴퓨터가 이김')
         

   