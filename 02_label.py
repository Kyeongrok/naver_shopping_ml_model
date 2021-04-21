# 선택1: 4인용 식탁세트 / 선택2: 네츄럴 / 선택3: 체어형(의자4개)

# person, color, type

text = '선택1: 4인용 식탁세트 / 선택2: 네츄럴 / 선택3: 체어형(의자4개)'

def get_person(text):

    if '4인용' in text:
        return 4
    elif '4인 식탁세트' in text:
        return 4
    elif '2인용' in text:
        return 2
    else:
        return None

def get_color(text):
    if '네츄럴' in text:
        return 0
    elif '브라운' in text:
        return 1
    else:
        return None

def get_type(text):
    if '체어형' in text:
        return 0
    elif '벤치형' in text:
        return 1
    elif '심플형' in text:
        return 2
    elif '쿠션형' in text:
        return 3
    else:
        return None

def get_sel_1(text):
    if '의자4개' in text:
        return 0
    elif '벤치2개' in text:
        return 1
    elif '벤치1+의자2' in text:
        return 2
    elif '벤치1개 + 의자2개' in text:
        return 2
    elif '벤치1개+의자2개' in text:
        return 2
    elif '2인테이블+의자2개' in text:
        return 3
    elif '테이블+의자2개' in text:
        return 3
    # 4는 의자4개
    else:
        return None



# 인용, color, option

lines = []
with open('ff.txt') as f:
    lines = f.readlines()

print('인용','색상', '타입', '선택1')
for text in lines:
    use_persone = get_person(text)
    color = get_color(text)
    type1 = get_type(text)
    sel1 = get_sel_1(text)
    if sel1 != None and use_persone == None:
        use_persone = 4
    if use_persone == 4 and type1 == 1 and sel1 == None:
        sel1 = 2

    r = {'origin':'', 'use_person':use_persone, 'color':color, 'type1':type1, 'sel1':sel1}
    r2 = [use_persone, color, type1, sel1]
    # print(text.replace('\n', ''))
    if None in r2:
        print(text.replace('\n', ''))
    print(r2)

