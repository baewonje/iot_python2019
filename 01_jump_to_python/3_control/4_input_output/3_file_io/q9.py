print("안녕하세요. 저희 가게에 방문해 주세서 감사합니다.")

prompt = """
1. 주문
2. 종료
입력 : """

def input_ingredient(ingredient_list):
    ingredient_list =input("안녕하세요. 원하시는 재료를 입력하세요: ")
    if ingredient_list!= '종료':
        return ingredient_list
    else:
        pass
def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다.")
    print(ingredient_list[:], "추가합니다.""\n",end='')
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

    ㄴ