#coding=cp949

age = 0
age1 = "����"
age2 = "���"
age3 = "û�ҳ�"
age4 = "����"
age5 = "����"
money= "����"
money1=2000
money2=3000
money3=5000

while True:
    age=int(input("���̸� �Է��ϼ���. "))
    if 0 <= age <= 3:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age1,money))
        break
    elif 4 <= age <= 13:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age2,money1))
        break
    elif  14 <= age <= 18:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age3,money2))
        break
    elif  19 <= age <= 65:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age4,money3))
        break
    elif age > 65:
        print("���ϴ� %s����̸� ����� %s�Դϴ�."%(age5,money))
        break
    else:
        print("�ٽ� �Է��ϼ���.")
