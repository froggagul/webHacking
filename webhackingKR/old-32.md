* 맨 밑에 내려보니 내 닉네임이 있는데, 이걸 아마 끝까지 위로 올려야 되나 싶다.
* cookie를 보니, vote_check에 값이 ok로 되어있는데, 이걸 지우면 클릭을 할 수 있다.
* 이때, cookie를 일일이 지우기 귀찮아서, edit this cookie에서 해당 쿠키를 금지시켰다.
* 그 다음에는 일일이 누르면 귀찮아진다.
* 일일이 누르기 귀찮아서 다음을 console에 넣었다.
```js
let i;
for(i=1;i<=100;i++) {
  fetch('https://webhacking.kr/challenge/code-5/?hit=froggagul');   // 투표하는 것과 같은 효과
}
```
* fetch에 시간이 걸리니 기다리자.