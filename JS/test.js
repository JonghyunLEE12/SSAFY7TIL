// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// console.log(input)



const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line) => {
  // 입력받은 값을 별도의 변수에 저장
}).on('close', () => {
  // 입력받은 값을 담고 있는 변수를 사용하여 계산한 뒤에 결과값 출력
});