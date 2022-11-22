// stack = [ 1,2,3,4,5,6,7,8,9,0]

// // forEach
// stack.forEach((num,idx) => {
//     // num 은 stack 배열의 원소
//     // idx 는 num 의 index 출력 가능
//     console.log(num,idx)
// })


// console.log('##################################')
// // splice

// // splice(indx) => Array[index] 값 이후로 출력됨
// // splice(-index) => Array의 끝에서부터 index 개수 만큼 출력
// // splice 는 원래 배열을 변화 시킨다.
// // console.log(stack.splice(-4))

// // ################################

const topping = [1,1,1,1,1,4,5,6]
console.log(solution(topping))
function solution(topping){
    let answer = 0
    
    const right = new Map()
    const left = new Set()
    
    
    for (let idx = 0 ; idx < topping.length ; idx ++) {
        const key = topping[idx]
        if (right.has(key)){
            const value = right.get(key)
            right.set(key,value+1)
        } else {
            right.set(key,1)
        }
    }
    
    for (let index = 0 ; index < topping.length ; index ++) {
        const targetTopping = topping[index]
        
        left.add(targetTopping)
        
        const value = right.get(targetTopping)
        if(value === 1) {
            right.delete(targetTopping)
        } else {
            right.set(targetTopping, value - 1)
        }
        
        if (left.size === right.size) {
            answer ++
        }
    }
    console.log(left)
    console.log(right)
    return answer
}