* 문제상황이다.
    > While editing index.php file using vi editor in the current directory, a power outage caused the source code to disappear.
    Please help me recover.
* 대충 vi editor 사용하다가 정전되서, 파일이 날라갔는데 이걸 복구하려고 한다는 것이다.
* vi에서 swapfile이 생성된 경험을 해보았다면, 쉽게 풀 수 있다.
* index.php의 swap file은 .index.php.swp 이므로, 이를 uri에 넣어주면 swp file이 다운로드 된다.
* 일단 메모장에서 열어보면, 깨지더라도 끝에 flag가 있는 것을 알 수 있다.
* 이를 복구하기 위해서는 vi editor가 필요한데,, window라 없다는건 함정..
    * (복구법)[https://superuser.com/questions/204209/how-can-i-recover-the-original-file-from-a-swp-file]에서 해결책을 찾을 수 있다.