* log injection이란 말 그대로 log를 실제로 login한것처럼 바꾸는 것이다.
* admin.php에 들어가보면 log를 그대로 볼 수 있는데, 이를 실제 admin이 로그인한 것 처럼 바꾸어야 한다.
```
IP: (입력한 기록)
```
* 같이 나와있는데, 처음에는 br 태그나 개행문자 등등 여러가지를 넣어보았으나, 실패했다.
* 그러다 input을 textarea로 바꾼 후, 직접 enter를 넣어주니, 해결할 수 있었다.

* 핵심: input -> textarea