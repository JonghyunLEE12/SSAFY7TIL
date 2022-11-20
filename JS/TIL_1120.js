stack = [ 1,2,3,4,5,6,7,8,9,0]

// forEach
stack.forEach((num,idx) => {
    // num 은 stack 배열의 원소
    // idx 는 num 의 index 출력 가능
    console.log(num,idx)
})


console.log('##################################')
// splice

// splice(indx) => Array[index] 값 이후로 출력됨
// splice(-index) => Array의 끝에서부터 index 개수 만큼 출력
// splice 는 원래 배열을 변화 시킨다.
console.log(stack.splice(-4))