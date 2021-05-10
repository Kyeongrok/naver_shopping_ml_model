import boto3

session = boto3.Session(profile_name='default')
s3 = session.client('s3', region_name='ap-northeast-2')
s3.upload_file('auction_price_onion_2020_2021.json', 'auction-prices', 'ffff.json')
