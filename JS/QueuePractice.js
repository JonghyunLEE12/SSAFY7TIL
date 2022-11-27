arr = [1,2,3,4,5,6]
// const sum = arr.reduce((a,b) => a+b , 0)

// console.log(Math.max(...arr))

// const sum = arr.reduce((a,b) => a+b,0)
// console.log(sum)


// class Queue {
//     constructor() {
//         this.queue = []
//         this.front = 0
//         this.rear = 0
//     }

//     enqueue(value){
//         this.queue[this.rear++] = value
//     }

//     dequeue(){
//         const value = this.queue[this.front]
//         delete this.queue[this.front]
//         this.front += 1
//         return value
//     }

//     peek(){
//         return this.queue[this.front]
//     }
//     size(){
//         return this.rear - this.front
//     }
// }


// const queue = new Queue()
// console.log(queue)
// queue.enqueue(1)
// console.log(queue)
// console.log(queue.size())
// console.log(queue.peek())
// queue.enqueue(2)
// queue.enqueue(3)
// console.log(queue)
// console.log(queue)
// console.log(queue.size())
// console.log(queue.peek())

// console.log('################################################')
// console.log(queue.dequeue())
// console.log(queue.dequeue())
// console.log(queue.dequeue())
// console.log(queue.size())
// console.log(queue.peek())

// console.log(queue.enqueue(7))
// console.log(queue)
// console.log(queue.peek())
// console.log(queue.size())


class Queue {
    // constructor(){
    //     this.queue = []
    //     this.front = 0
    //     this.rear = 0
    // }

    #queue = []
    #front = 0
    #rear = 0
    enqueue(value) {
        this.#queue[this.#rear++] = value
    }

    dequeue(){
        const value = this.#queue[this.#front]
        delete this.#queue[this.#front]
        this.#front += 1
        return value
    }
    peek(){
        return this.#queue[this.#front]
    }
    size(){
        return this.#rear - this.#front
    }
}

const queue = new Queue()
console.log(queue)
queue.enqueue(1)
console.log(queue)
console.log(queue.size())
console.log(queue.peek())
queue.enqueue(2)
queue.enqueue(3)
console.log(queue.size())
console.log(queue.peek())

console.log('################################################')
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.dequeue())
console.log(queue.size())
console.log(queue.peek())

console.log(queue.enqueue(7))
console.log(queue)
console.log(queue.peek())
console.log(queue.size())
console.log('hi')