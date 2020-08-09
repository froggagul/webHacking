* old-18의 심화된 버전이다.
```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 27</title>
</head>
<body>
<h1>SQL INJECTION</h1>
<form method=get action=index.php>
<input type=text name=no><input type=submit>
</form>
<?php
  if($_GET['no']){
  $db = dbconnect();
  if(preg_match("/#|select|\(| |limit|=|0x/i",$_GET['no'])) exit("no hack");
  $r=mysqli_fetch_array(mysqli_query($db,"select id from chall27 where id='guest' and no=({$_GET['no']})")) or die("query error");
  if($r['id']=="guest") echo("guest");
  if($r['id']=="admin") solve(27); // admin's no = 2
}
?>
<br><a href=?view_source=1>view-source</a>
</body>
</html>
```
* no=2임을 구분해야 하는데, '='을 못쓰니, 1 말고 2를 구분할 기호가 필요하다.
    * no=1 or no > 1
* 이떄, no=(query문) 꼴이므로, 내가 닫아주고 뒤에 있는 )는 주석으로 없애줘야 한다.
    * #이나 --를 사용해야 한다.
    * /**/도 가능하지만, 여기서는 닫아줘야 하는 값이 가장 끝에 있으므로, 쓰기 어려워 보인다.
    * no=1 or no > 1-- 
    * 뒤에 공백을 포함해줘야 하는 이유는 공식 문서를 통해 알 수 있다.
        > 9.6 Comment Syntax
        > MySQL Server supports three comment styles:
        > From a # character to the end of the line.
        > From a --  sequence to the end of the line. In MySQL, the --  (double-dash) <h3>**comment style requires the second dash to be followed by at least one whitespace or control character (such as a space, tab, newline, and so on)**</h3>. This syntax differs slightly from standard SQL comment syntax, as discussed in Section 1.7.2.4, “'--' as the Start of a Comment”.
        > From a /* sequence to the following */ sequence, as in the C programming language. This syntax enables a comment to extend over multiple lines because the beginning and closing sequences need not be on the same line.
    * space 관련 문제는 old-18에서 해결했듯이, tab에 해당하는 %09로 해결하자.
* answer query: 2%29%09or%09no>1--%09