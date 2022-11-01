// 객체 생성
const obj1 = new Object()
const obj2 = {}

console.log(obj1)
console.log(obj2)

// 객체의 값 추가 및 삭제
console.log('# 객체의 값 추가')
obj1["email"] = "dlwhdgus@naver.com" // Key,Value 
obj1.phone = "01022222222"  // . 을 이용한 방식
console.log(obj1)

console.log('# 객체의 요소 삭제')
// delete
delete obj1.phone
console.log(obj1)

// in Operator
console.log('# in Operator')
console.log('email' in obj1) // true
console.log('phone' in obj1) // false

// key 와 value 집합 구하기
console.log('# key 와 value 집합 구하기')
console.log('Object.keys()')
console.log(Object.keys(obj1))
// ['email'] 배열 형태로 값 반환


console.log('Object.values()')
console.log(Object.values(obj1))
// [ 'dlwhdgus@naver.com' ] 배열 형태로 값 반환

// for in 순회
// 객체의 key 값을 순회 가능하다.
console.log('# for in ')
for (const key in obj1) {
    console.log(key , obj1[key])
}



