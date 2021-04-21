# 선택1: 4인용 식탁세트 / 선택2: 네츄럴 / 선택3: 체어형(의자4개)

# person, color, type

text = '선택1: 4인용 식탁세트 / 선택2: 네츄럴 / 선택3: 체어형(의자4개)'

def get_person(text):

    if '4인용' in text:
        return 4
    elif '2인용' in text:
        return 2
    else:
        return 0

def get_color(text):
    if '네츄럴' in text:
        return '네츄럴'
    elif '브라운' in text:
        return '브라운'
    else:
        return '없음'

def get_type(text):
    text = '선택1: 4인용 식탁세트 / 선택2: 네츄럴 / 선택3: 체어형(의자4개)'
    if '체어형' in text:
        return '체어형'
    elif '벤치형' in text:
        return '벤치형'
    elif '심플형' in text:
        return '심플형'
    elif '쿠션형' in text:
        return '쿠션형'
    else:
        return '없음'

def get_sel_1(text):
    if '의자4개' in text:
        return '의자4개'
    elif '벤치2개' in text:
        return '벤치2개'
    elif '벤치1+의자2' in text:
        return '벤치1+의자2'
    elif '벤치1개 + 의자2개' in text:
        return '벤치1+의자2'
    elif '벤치1개+의자2개' in text:
        return '벤치1+의자2'
    else:
        return 0



# 인용, color, option

lines = []
with open('ff.txt') as f:
    lines = f.readlines()


for text in lines:
    use_persone = get_person(text)
    color = get_color(text)
    type1 = get_type(text)
    sel1 = get_sel_1(text)
    if sel1 != 0 and use_persone == 0:
        use_persone = 4

    r = {'origin':'', 'use_person':use_persone, 'color':color, 'type1':type1, 'sel1':sel1}
    print(text.replace('\n', ''))
    print(r)