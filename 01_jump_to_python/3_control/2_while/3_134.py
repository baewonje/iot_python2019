#coding=cp949

coffee = 10
money = 0
coffee_price = 300

while True:
    money = int(input("���� �־��ּ���: "))
    if money >= coffee_price:
        print("�Ž����� %d���� �ְ� Ŀ�Ǹ� �ݴϴ�." %(money-300))
        coffee -=1
    else:
        print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.")

    print("���� Ŀ���� ���� %d�� �Դϴ�.\n"% coffee)
    if coffee == 0:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break