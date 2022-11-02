// stack
// Last In First Out
// 선형 자료 구조

// 넣을 떈 push
// 꺼낼 땐 pop

// stack 은 배열로 표시가 가능하다.

const stack = []

// Push
stack.push(1)
stack.push(2)
stack.push(3)


// Pop
stack.pop()
console.log(stack)


// Get Top
console.log(stack[stack.length-1])
