#coding=cp949

prompt="""
1. �Է�
2. ����
    �Է�: """
ingredint_list=[]

def input_ingredint():
    while True:
        input_list=input("�ȳ��ϼ���. ���Ͻô� ��Ḧ �־��ּ���.: ")
        if input_list == '����':
            return
        else:
            ingredint_list[:] += [input_list]

def make_sandwiches():
    print("������ġ�� ����ϴ�.")
    for i in ingredint_list[:]:
        print(f"{i}  �߰��մϴ�.")
    print("���� �ֹ��Ͻ� ������ġ ��������ϴ�. ���ְ� �弼��.")

while True:
    choice = int(input(prompt))
    if choice == 1:
        input_ingredint()
        make_sandwiches()
        break
    elif choice == 2:
        print("���α׷��� �����մϴ�.")
        break
    else:
        print("�߸��� ��ȣ�� �Է��ϼ̽��ϴ�.")
        continue

