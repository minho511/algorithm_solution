## Algorithm & data structure


### Kadane's Algorithm(카데인 알고리즘)
2021.12.27
___
- Dynamic Programming 기법 중 하나
- 최대 부분 합을 구할때 유용한 알고리즘
- O(n)의 시간복잡도
___

```python
local_max[i] = max(A[i] + local_max[i-1], A[i])
```
[참고](https://www.youtube.com/watch?v=86CQq3pKSUw)
___


### Linked List
2021.12.28
___
- 데이터 요소의 선형 집합
- 데이터 순서가 메모리에 물리적인 순서대로 저장되지 않는다.
- 다양한 추상 자료형의 기반이 된다.  
- 장점
    - 동적으로 새로운 노드 삽입-제거 용이, 관리가 쉽다 (O(1) 시간 복잡도)
    
- 단점
    - 특정 인덱스 접근시 전체를 순서대로 읽어야함 (O(n) 시간 복잡도)
    
- 참고 코드
```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def AtBegining(self, newdata):
        NewNode = Node(newdata)

        NewNode.nextval = self.headval
        self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2

e2.nextval = e3

list.AtBegining("Sun")
list.listprint()

# Sun
# Mon
# Tue
# Wed
```
___
### Deque
2021.12.28
___
- 양방향 큐(queue)
- container의 양 끝 요소에 접근하여 삽입-제거하는 하는데 빠르게 동작. (O(1))
- 코드
```python
from collections import deque
deq = deque()
deq.appendleft(1)
deq.append(2)
deq.popleft() # 1
deq.pop() # 2
```
- 추가적으로 rotate() 메서드가 있다.
```python
deq = deque([1,2,3,4])
deq.rotate(1)  # [4,1,2,3]
de.rotate(-2)  # [2,3,4,1]
```
___
### 연결 리스트를 이용한 스택 ADT구현
2022.1.2  
ADT : Abstract Data Type (스택 추상 자료형)
```python
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
```

