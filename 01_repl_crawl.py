import requests
import json
import os, time
from threading import Thread

class Crawler:
    '''
    replay수집기
    :parameter merchant_no : 상점 id
    :parameter origin_product_no : 상품 id
    '''
    origin_product_no = '000000'

    def __init__(self, merchant_no, origin_product_no):
        self.merchant_no = merchant_no
        self.origin_product_no = origin_product_no

    def get_repl(self, pageNo):

        # url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page={str(pageNo)}&pageSize={itemsPerPage}&merchantNo={merchantNo}&originProductNo={originProductNo}&sortType=REVIEW_CREATE_DATE_DESC'
        url = f'https://smartstore.naver.com/i/v1/reviews/paged-reviews?page={str(pageNo)}&pageSize=30&merchantNo={self.merchant_no}&originProductNo={self.origin_product_no}&sortType=REVIEW_CREATE_DATE_DESC'
        print(url)
        data = requests.get(url)

        s = data.content
        print(s[:1000])
        jo = json.loads(s)
        return jo

    def fn(self, page_no, results):
        results[page_no] = self.get_repl(page_no)['contents']
        print(f'{page_no} finished...')


    def save(self, list):

        target_path = f'./{self.origin_product_no}/'
        # origin product no로 dir만들기
        print(target_path)
        if not os.path.isdir(target_path):
            os.makedirs(target_path)

        with open(f'./{self.origin_product_no}/r.json', 'w+') as f:
            f.write(json.dumps(list))

    # # https://smartstore.naver.com/i/v1/reviews/paged-reviews?page=2&pageSize=20&merchantNo=500038401&originProductNo=328054674&sortType=REVIEW_RANKING
    # for i in range(1666, 1693):

    def crawl(self):
        # total page만큼 array생성
        # 그 만큼 thread생성
        total_pages = cr.get_repl(1)['totalPages']
        print(f'start crawl {total_pages} pages...')

        threads = [None] * total_pages
        results = [None] * total_pages

        for i in range(1, total_pages):
            threads[i] = Thread(target=self.fn, args=(i, results)).start()
            time.sleep(0.01)

        # results에 None이 몇개인지 check해서 다 안되었으면 시간을 늘린다.
        time.sleep(total_pages / 20)

        result = {'contents':[]}
        for i in range(1, len(results)):
            result['contents'] += results[i]

        self.save(result)
        print(f'completed {len(result)}...')



#'500038401', '328054674')
# 상점 id와 상품 id를 넣으면 모든 리뷰를 수집해서 .json으로 저장 해줍니다.
# 상품의 url을 넣으면 상점id, 상품id 수집하는 기능 추가하면 좋을 것 같네요.
cr = Crawler('500038401', '328054674')
cr.crawl()


