#coding=cp949

i = 0
num = 1

while True:
    odd = int(input("Ȧ���� �Է��ϼ���.(0 <- ����): "))
    if odd == 0:
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break
    if odd != 0:
        num = 1
        while num<=odd:
            print("{0:^30}".format(num*('*')))
            num+=2




