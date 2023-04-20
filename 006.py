# age=input('당신의 나이는 몇살입니까?')

# print(type(age))

# age=int(age)

# print(type(age))

# year = 90 - age
# month = year * 12
# week = year * 52
# day = year * 365

# #print(f'당신이 죽기까지 {day}일, {week}주, {month}달, {year}년이 남았습니다.')

# message= f'당신이 죽기까지 {day}일, {week}주, {month}달, {year}년이 남았습니다.'

# print(message)

# a = int("5")/int(2.7)
# print(type(a))


#팁 계산기 만들기

# 1.총 주문금액 입력받기
# 2.팁 몇프로 줄 지
# 3.총 지불해야하는 금액 출력
# 4.몇명이 나눠 낼지 입력받기
# 5.인당 지불해야할 금액 출력하기

# order=float(input('총 결제해야 할 금액은 얼마입니까?'))
# tip=int(input('팁을 얼마나 주시겠습니까?, 10, 12, 15 ?'))
# people=int(input('몇명이서 나눠 내시겠습니까?')) 
# #input으로 입력받은 값은 문자라는 걸 잊지말기


# tip = tip / 100
# total_tip = order * tip
# total_order = order + total_tip
# bill_person = total_order / people

# final_bill = round(bill_person,2)

# print(f'인당 내야하는 금액은{final_bill}')

#----------

#롤러코스터 매표기 만들기
#120cm이상 탈 수 있다.
#나이가 18세 이상이면 12,000원, 미만이면 7,000원

# print('롤러코스터')

# height = int(input('당신의 키는 몇cm입니까?'))

# if height>=120:
#    print('표를 예매해주세요') 
#    age = int(input('나이를 입력해주세요'))
#    if age < 12:
#       print('무료입니다.') 
#    elif age <= 18:
#       print('12,000원입니다')  
#    else:
#       print('7,000원 입니다.')
# else:
#    print('120cm미만은 탈 수 없습니다.')

 
#bmi지수 구하기
#BMI 계산기 BMI지수= 몸무게(kg) ÷ (신장(m) × 신장(m))
#저체중, 정상, 과체중, 비만 출력하기
#키 입력받
#몸무게 입력받
#25이상 비만 23~25과체중 18.5~23정상 18.5밑 저체중

height = float(input('키를 입력하세요 (m)'))
weight = float(input('몸무게 입력하세요 (kg)'))

bmi = round(weight / (height*height),2)




if bmi >= 25:
    print(f'당신의 bmi지수는 {bmi}로 비만입니다.')

elif bmi < 25 and bmi >= 23:
    print(f'당신의 bmi지수는 {bmi}로 과체중입니다.')

elif bmi <23 and bmi >= 18.5:
    print(f'당신의 bmi지수는 {bmi}로 정상체중입니다.')

else:
    print(f'당신의 bmi지수는 {bmi}로 저체중입니다.')

