// 연결리스트
// 요소 추가나 삭제가 발생할 때,
// 연결리스트 의 특징
// 제한 없이 요소 추가 가능
// 탐색에 O(n)
// 추가와 제거에는 O(1)


// 단일연결리스트
// Singgly Linked List
// Head 에서 Tail까지 단방향으로 이어지는
// 연결리스트


// 이중연결리스트
// Doubly Linked List
// 양방향으로 이어지는 연결리스트

// 환영연결리스트
// Circular Linked List
// 리스트의 Tail이 Head로 연결되는 리스트


// class Node {
//     constructor(value){
//         this.value = value;
//         this.next = null
//     }
// }

// class SinglyLinkedList {
//     constructor(){
//         this.head = null
//         this.tail = null
//     }

//     find(value) {
//         let currNode = this.head
//         while ( currNode.value !== value) {
//             currNode = currNode.next
//         }
//         return currNode
//     }

//     apppend(newValue) {
//         const newNode = new Node(newValue)
//         if (this.head === null) {
//             this.head = newNode
//             this.tail = newNode
//         } else {
//             this.tail.next = newNode
//             this.tail = newNode
//         }
//     }
    
//     insert(node,newNode){
//         const newNode = new Node(newValue)
//         newNode.next = node.next
//         node.next = newNode
//     }

//     remove(value){
//         let prevNode = this.head
//         while ( prevNode.next.value !== value) {
//             prevNode = prevNode.next
//         }

//         if ( prevNode.next !== null ){
//             prevNode.next = prevNode.next.next
//         }
//     }

//     display() {
//         let currNode = this.head
//         let displayString = '['
//         while (currNode !== null) {
//             displayString += `${currNode.value}`
//             currNode = currNode.next
//         }
//         displayString = displayString.substr(0,displayString.length-2)
//         displayString += '] '
//         console.log(displayString)
//     }

// }
