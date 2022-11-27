/*
그래프의 특징
- 정점은 여러 개의 간선을 가질 수 있다
- 크게  방향 그래프와 무방향 그래프로 나눌 수 있다.
- 간선은 가중치를 가질 수 있다.
- 사이클이 발생할 수 있다.
*/


// 입접 행렬

const graph = Array.from(
    Array(5),
    () => Array(5).fill(0)
)

console.log(graph)