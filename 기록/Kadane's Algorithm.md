## Algorithm


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
