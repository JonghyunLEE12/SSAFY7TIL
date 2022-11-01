// fill => 값을 채울 수 있음
console.log('# fill')

const arr5 = new Array(5).fill(5)

// console.log(arr5)


// from 함수 => 초기화 가능
// 첫번째 파라미터 -> 초기화할 배열
// 두번째 파라미터 -> 로직
//         = 첫번째 파라미터는 배열의 값
//         = 두번째는 배열의 인덱스를 나타냄
console.log('# from')

const arr6 = Array.from(Array(5), function(v,k){
    return k +1
})

console.log(arr6)

// 배열의 요소
// length
console.log('# length')

console.log(arr6.length)

// 배열의 편리한 함수
// join 배열을 문자열로 합쳐주는 기능
console.log('# join')

console.log(arr6.join(",")) // 1,2,3,4,5
console.log(arr6.join(" ")) // 12345

// reverse
// 한번 사용하면 원래 배열의 값도 뒤집어진다.
console.log('# reverse')

console.log(arr6.reverse()) // 5 4 3 2 1
console.log(arr6)  // 5 4 3 2 1

// 배열 합치기
// concat
console.log('# concat')
arr1 = [1,2,3,4,5]
arr2 = [6,7,8]

console.log(arr1.concat(arr2)) // 1,2,3,4,5,6,7,8,9


// 배열의 요소 추가 및 삭제
// push  ( 끝에 추가 ), pop( 끝에 삭제 )
console.log('# push & pop')
arr1.push(6)
console.log(arr1) // 6 이 추가 

arr1.push(7,8,9)
console.log(arr1) // 여러가지 수를 한번에 push 가능

arr1.pop() // 9 가 삭제
arr1.pop() // 8 이 삭제
console.log(arr1.pop()) // 7 마지막 값을 삭제 후 반환
console.log(arr1) // 1,2,3,4,5,6



// 배열의 첫번째 요소제어
// shift , unshift
// shift => 배열의 맨 앞의 요소 제거
// unshift => 배열의 맨 앞의 요소 추가

console.log('# shift , unshift')

arr1.shift() // 1 제거
console.log(arr1.shift()) // 2 제거 후 반환
console.log(arr1) // 3 , 4 , 5 ,6

arr1.unshift(10) // 배열의 맨 앞에 10 추가
console.log(arr1) // 10,3,4,5,6


console.log('# slice')
// slice
// 배열을 잘라 값을 출력
const arr = [1,2,3,4,5,6]
// slice는 두번째 파라미터의 인덱스값 바로 앞에서 잘린다
console.log(arr.slice(2,4)) // 3,4
console.log(arr) // slice 는 원래 배열에 영향을 주지 않음


// splice
// 중간의 배열값을 삭제
console.log('# splice')
console.log(arr) // 1,2,3,4,5,6
arr.splice(2,2) // 2번 인덱스부터 두개의 인덱스를 삭제한다.
console.log(arr) // 1,2,5,6


console.log('# 순회')
// 배열의 순회
const numbers = [1,2,3,4,5,6]

// for of 
// 기존 for문 과는 다르게 직관적으로 사용 가능
for ( const num of numbers) {
    console.log(num) 
}

// 배열의 객체와 타입이 동일하다.
numbers["key"] = "value"
console.log(numbers)
// [ 1, 2, 3, 4, 5, 6, key: 'value' ] 
console.log(numbers.length) // 6

// 배열은 자바스크립트에서 특수한 객체이기 때문에
// 배열의 값이 볂하지 않음, 추천하지는 않는다.
