import requests

headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    #'cookie': 'csv=1; edgebucket=6MvVNw5CfBo3oM51ff; G_ENABLED_IDPS=google; reddit_session=47813020886^%^2C2020-11-01T09^%^3A12^%^3A17^%^2C25280121d1c66701b3f7ea9a6fc25253345b5f9b; loid=00000000000lyqmz12.2.1511527890000.Z0FBQUFBQmZubnZ4VHdsMDRfN19CdnJ6OTNHQk9FbmU0Z2E3bVROeEpUbldZV040UjUweWd2bU1ONmFOelFXLXdYUF9IYWxlYmdQMVQ2Qk5qS256c05KbzFrN0NiZ21aQnAwaXlKM0RKODJycF9TTlBJTUtPQjlPS0J3WFZOcnRiejJKeXlUaXdIVng; d2_token=3.f2d340b669fc96b796f01af5b4b9b655a664d389906c9580713f4d639c2d4352.eyJhY2Nlc3NUb2tlbiI6IjQ3ODEzMDIwODg2LTBnVFhkLXF0STJ2enI1REV5MktrSExxcTFGayIsImV4cGlyZXMiOiIyMDIwLTExLTA4VDEwOjI4OjMyLjAwMFoiLCJsb2dnZWRPdXQiOmZhbHNlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19; pc=9z; show_announcements=no; USER=eyJwcmVmcyI6eyJsYXlvdXQiOiJjYXJkIiwiZ2xvYmFsVGhlbWUiOiJOSUdIVCJ9fQ==; gwyn2024_recentclicks2=t3_k8a89d^%^2Ct3_c1b5sf; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDczNDE5NjcsInN1YiI6IjQ3ODEzMDIwODg2LWRMNTBkSlJZSjlLakhqZmV0eWFIWTB2RFlOQSIsImxvZ2dlZEluIjp0cnVlLCJzY29wZXMiOlsiKiIsImVtYWlsIl19.tIyACJB0vm9zsOQvfUUr_jQ_pWboFAd59Ub8WOX8WyI; session=be3cf59db924b18504dc7ea13198c58f3116772egASVSQAAAAAAAABK9wnOX0dB1/OBKXrfgX2UjAdfY3NyZnRflIwoNTFiY2Y3NGVlMDM1MGNiOTM5M2NjMDU0NDgxN2NmMTNhZjAwYWZiOZRzh5Qu; recent_srs=t5_2qizd^%^2Ct5_2rfcw^%^2Ct5_2xd5g^%^2Ct5_2qlz9^%^2Ct5_2tisr^%^2Ct5_38jf0^%^2Ct5_3ph6l^%^2Ct5_3fsth^%^2Ct5_2qh3k^%^2Ct5_sfted; session_tracker=bledrolncflcrpflqi.0.1607338508472.Z0FBQUFBQmZ6Z29Ndjg3U0RnM1ZYZVFUcTZ5ajJYaGI3Q1lZNnpob1JRVVQ0N1QwMFhEN29RWE1IYTZ4NENlVnJybU5EQkUzamFmeEJxREdBUzZYd01aTVB1SGJkTnFIY0JsbUZHZHRvb3Q1ZU5PYWpjMnUwSmt5blNQOVUybHZvcWRMQmdmdGRyQkw',
}

def find_mod(subReddit):
    response = requests.get(f'https://www.reddit.com/r/{subReddit}/about/moderators/.json', headers=headers)
    json_response = response.json()
    mods = print([{'subreddit' : subReddit, 'mod' : item['name']} for item in json_response['data']['children'] if item['name'] != 'AutoModerator'])
    return mods

find_mod('SGExams')
print('ayoooo test')