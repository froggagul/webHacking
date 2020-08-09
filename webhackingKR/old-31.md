* 코드를 보아 하니, socket 통신이다. 일단 통신을 해보자. 근데, 포트 번호가 랜덤이네..?
* 여기서 두가지 경로가 존재한다.
* fsockopen vulnerability에, port를 내가 지정해 줄 수 있는 취약점이 존재한다.
    > The PHP language offers the fsockopen() function which is used to open a socket. For example: fsockopen("192.168.1.1", 80, [...]);

    > However, the following syntax is also accepted:
      fsockopen("192.168.1.1:81", 80, [...]);  
    > In this case, the connection is done on the port 81 instead of 80.

* 내가 갖고 있는 heroku 서버인 api.armply.com:80에 통신을 보내고 로그를 보았다.. ㅋㅋㅋㅋㅋㅋ
```
2020-08-07T08:09:20.078931+00:00 heroku[router]: at=info method=GET path="**/FLAG{i_have_a_big_and_beautiful_server}**" host=api.armply.com request_id=9b817a62-513d-41fa-a982-0bb0d25a0626 fwd="202.182.106.159" dyno=web.1 connect=1ms service=23ms status=404 bytes=530 protocol=http
```
* 답: **/FLAG{i_have_a_big_and_beautiful_server}**