class Test {
    #number = 10
    
    addNumber(){
        this.#number = 0
        return this.#number++
    }

    minusNumber(){
        return this.#number--
    }
}

const test = new Test()
console.log(test.addNumber()) // 0
console.log(test.minusNumber()) // 1
