/*

힙의 특징
- 우선 순위가 높은 요소가 먼저 나가는 특징을 가진다
- 루트가 가장 큰 값이 되는 최대 힙 (Max Heap) 과 루트가 가장 작은 값이 되는 최소 힙 (Min Heap)이 있다.
- 아쉽게도 자바 스크립트 에서는 직접 궇현해서 사용해야 한다.

*/

/*
 * 힙 요소 추가 알고리즘
요소가 추가 될 떄는 트리의 가장 마지막 정점에 위치한다.
추가 후 부모 정점보다 우선순위가 높다면 부모 정점 과 순서를 바꾼다.
이 과정을 반복하면 결국 가장 우선순위가 높은 정점이 루트가 된다
완전 이진 트리의 높이는 log N이기에 힙의 요소 추가 알고리즘은 O(logN) 시간 복잡도를 가진다
*/

/**
 * 힙 요소 제거 알고리즘
 요소 제거는 루트 정점만 가능하다.
 루트 정점이 제거된 후 가장 마지막 정점이 루트에 위치한다
 루트 정점의 두 자식 정점 중 우선순위가 높은 정점과 바꾼다.
 두 자식 정점이 우선순위가 더 낮을 때 까지 반복한다
 완전 이진 트리의 높이는 logN 이기에 힙의 요소 제거 알고리즘은 O(logN) 시간 복잡도를 가진다
 */
class MaxHeap {
    constructor (
        heap = [null]
    )

    push(value){
        this.heap.push(value)
        let currentIndex = this.heap.length - 1
        let parentIndex = Math.floor(currentIndex / 2)

        while ( parentIndex !== 0 && this.heap[parentIndex] < value) {
            const temp = this.heap[parentIndex]
            this.heap[parentIndex] = value
            this.heap[currentIndex] = temp

            currentIndex = parentIndex
            parentIndex - Math.floor(currentIndex / 2)
        }
    }
}

const heap = new MaxHeap()
console.log(heap)
heap.push(45)
heap.push(35)
console.log(heap)