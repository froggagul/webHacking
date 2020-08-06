* 소스
```php
extract($_SERVER);
  extract($_COOKIE);    // cookie를 extract해 변수화
  $ip = $REMOTE_ADDR;
  $agent = $HTTP_USER_AGENT;
  if($REMOTE_ADDR){
    $ip = htmlspecialchars($REMOTE_ADDR);
    $ip = str_replace("..",".",$ip);    //..을 .으로
    $ip = str_replace("12","",$ip);     //12를 지운다
    $ip = str_replace("7.","",$ip);     //7을 지운다
    $ip = str_replace("0.","",$ip);     //0.을 지운다
  }
  if($HTTP_USER_AGENT){
    $agent=htmlspecialchars($HTTP_USER_AGENT);
  }
  echo "<table border=1><tr><td>client ip</td><td>{$ip}</td></tr><tr><td>agent</td><td>{$agent}</td></tr></table>";
  if($ip=="127.0.0.1"){
    solve(24);
    exit();
  }
```
* cookie에 REMOTE_ADDR이 있는 경우 이를 사용하기 때문에
* REMOTE_ADDR 112277.12.00.12.00.12.1값을 넣어줘서 filtering을 피한다.