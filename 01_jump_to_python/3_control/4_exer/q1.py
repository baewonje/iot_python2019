#coding=cp949

age = 0
age1 = 2000
age2 = 3000
age3 = 4000
age4 = 5000
age5 = "����"


age= int(input("���̸� �Է��ϼ���. "))

if 0<= age <= 3:
    print("����� %s�Դϴ�."%age5)
elif 4 <= age <= 13:
    print("����� %d���Դϴ�."%age2)
elif  14 <= age <= 18:
    print("����� %d���Դϴ�."%age3)
elif  19 <= age <= 65:
    print("����� %d���Դϴ�."%age4)
elif age > 65:
    print("����� %s�Դϴ�."%age5)
