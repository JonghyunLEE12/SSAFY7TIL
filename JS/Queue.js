// Queue
// First In First Out
// 선형 자료 구조


// 선형 Queue
// Array 로 표현하기
// Queue는 배열에서 사용하기 어려움
// 코테에서는 배열을 이용하여 구현할것
// shift 함수는 쓰지 말 것

class Queue {
    constructor() {
        this.queue = [];
        this.front = 0
        this.rear = 0
    }

    enqueue(value) {
        this.queue[this.rear++] = value
    }

    dequeue() {
        const value = this.queue[this.front]
        delete this.queue[this.front]
        this.front += 1
        return value
    }

    peek() {
        return this.queue[this.front]
    }

    size(){
        return this.rear - this.front
    }

}

const queue = new Queue()
console.log(queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)

console.log(queue.dequeue()) // 1

queue.enqueue(8)
console.log(queue.size())
console.log(queue.peek())
console.log(queue)
console.log(queue.dequeue())
console.log(queue)
console.log(queue.dequeue())

