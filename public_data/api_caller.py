import requests, json
import pandas as pd
import os

def call_api(key, date, prd_cd, limit=30000):
    url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    data = requests.get(url)
    jo = json.loads(data.content)
    body = jo['response']['body']
    total_cnt = body['totalCount']
    print('total_cnt:', total_cnt)
    # print(body)
    items = body['items']
    if items == '':
        return []
    return items['item']

def save_data(data, target_filename):
    #filename, path분리하기
    location, filename = os.path.split(target_filename)

    # dir이 없다면 생성합니다.
    print(os.path.isdir(location))
    if not os.path.isdir(location):
        os.makedirs(location)

    # file저장
    with open(target_filename, 'w+') as f:
        f.write(json.dumps(data))
        print(f'{target_filename} saved...')



if __name__ == '__main__':
    dr = pd.date_range(start='20210401', end='20210429')
    dates = dr.strftime('%Y%m%d').tolist()
    print(dates)

    for date in dates:
        key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
        r = call_api(key, date, '1202')
        save_data(r, f'./1202/{date}.json')
