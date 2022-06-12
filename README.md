# Algorithm_Sol

2022-06
___
- 2022-06-12
    - [(10815) 숫자 카드](https://github.com/minho511/algorithm_solution/blob/master/baekjoon_python/%5B10815%5D%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C.py) S5(자료구조 정렬 이분 탐색)
        > 이진 검색 모듈 bisect을 활용한 풀이
        ```python
        def bin_search(data, target):
            idx = bisect_left(data , target)
            if idx < len(data) and data[idx] == target:
                return 1
            else:
                return 0
        ```
        > in을 사용하여 원소 포함 여부를 확인하려 하였으나 `시간초과`
        ```python
        N = int(input())
        cards = set(map(int, input().split()))
        M = int(input())
        for card in list(map(int, input().split())):
            print(int(card in cards), end=' ')
        ```
        `cards를 담을 때 set()을 사용하여 중복값을 제거하여 시간 초과 해결`