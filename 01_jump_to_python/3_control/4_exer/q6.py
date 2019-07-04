#coding=cp949

age = []
money = 0
choice = 0
ticket = 5
year = 3
count = 0
count1 = 0
age1 = ["유아","어린이","청소년","성인","노인"]
money1= ["무료",2000,3000,5000]

prompt="""
1. 현금
2. 공원 전용 신용 카드
"""
while True:
    age=int(input("나이를 입력하세요. "))
    if 0 <= age <= 3:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age1[0],money1[0]))
        print("티켓을 발행합니다.")
        continue
    elif 4 <= age <= 13:
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1[1],money1[1]))
    elif  14 <= age <= 18:    
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1[2],money1[2]))
    elif  19 <= age <= 65:
        print("귀하는 %s등급이며 요금은 %d입니다."%(age1[3],money1[3]))
    elif age > 65:
        print("귀하는 %s등급이며 요금은 %s입니다."%(age1[4],money1[0]))
        print("티켓을 발행합니다.")
        continue
            
    choice = int(input(prompt))
    if choice == 1:
            money=int(input("요금을 입력하세요. "))
            if 4 <= age <= 13 == money>=money1[1]:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(money1[1])))
            else:
                print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((money1[1])-money,money))
            elif 14 <= age <= 18 == money>=money1[2]:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(money1[2])))
            else:
                print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((money1[2])-money,money))
            elif 19 <= age <= 65 == money>=money1[3]:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."%(money-(money1[3])))
            else:
                print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다."%((money1[3])-money,money))
    elif choice == 2:
            result = [money2*0.9 for money2 in money1]
            if age >= 60:
                print("%d원이 결제 되었습니다. 티켓을 발행합니다." %(((money1[3])*0.9)*0.95))
            elif age>= 4:
                print("%d원이 결제 되었습니다. 티켓을 발행합니다." %((money1[3])*0.9))

    if 4<=age<=65:
            count +=1
            if count % 7 == 0 :
                if ticket >0:
                    print("축하합니다. 1주년 이벤트에 당첨 되었습니다. 여기 무료티켓을 발행합니다. 잔여 무료티켓 %d장"%(ticket-1))
                    ticket -=1
            elif count % 4 == 0:
                if year >0:
                    print("축하합니다. 연간 회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여티켓 %d장"%(year-1))
                    year-=1


