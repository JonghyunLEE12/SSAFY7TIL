const arr = [1,2,3,4,5,5,5,5,5,5]

const arr_map = arr.map((a) => {
    return a * 10
})

console.log(arr)
console.log(arr_map)

console.log('################################')

const right = new Map()
const left = new Set()
console.log(right)

let count = 0
for (let i = 0 ; i < arr.length ; i ++) {
    const key = arr[i]
    if (right.has(key)) {
        const value = right.get(arr[i])
        right.set(arr[i], value + 1)

    } else {
        right.set(arr[i],1)
    }
}

for (let i =0 ; i < arr.length ; i ++) {
    const targetTopping = arr[i]

    left.add(targetTopping)

    const value = right.get(targetTopping)
    if (value === 1 ) {
        right.delete(targetTopping)
    } else {
        right.set(targetTopping , value -1 )
    }

    if (left.size === right.size) {
        count += 1
    }
}

console.log(count) 