#coding=cp949

num = 1
while True:
    odd = int(input("Ȧ���� �Է��ϼ���.(0 <- ����): "))
    max = int(odd/2)

    if odd == 0:
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break

    if odd != 0:
        print(' '+odd * "-"+' ')
        for star in range(0,max+1):
            print('|'+' '*(max-star) +'*'*((star*2)+1)+' '*(max-star)+'|')

    if odd != 0:
        for star in range(max-1, -1,-1):
            print('|'+' ' * (max - star)+ '*' * ((star * 2) + 1)+ ' ' * (max - star)+ '|')

    print(' '+ odd * "-"+ ' ')