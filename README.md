# Algorithm_Sol

2022-06
___
- 2022-06-22
    - [(BOJ 1759) 암호 만들기](https://github.com/minho511/algorithm_solution/blob/master/baekjoon_python/%5B1759%5D%20%EC%95%94%ED%98%B8%20%EB%A7%8C%EB%93%A4%EA%B8%B0.py) G5(수학 브루트포스 알고리즘 조합론 백트래킹)
    - [(BOJ 14622) 소수 게임](https://github.com/minho511/algorithm_solution/blob/master/baekjoon_python/%5B14622%5D%20%EC%86%8C%EC%88%98%20%EA%B2%8C%EC%9E%84.py) G4(수학 구현 자료구조 정수론 우선순위큐 소수판정 에라토스테네스의 체)  
    - [(BOJ 1091) 카드 섞기](https://github.com/minho511/algorithm_solution/blob/master/baekjoon_python/%5B1091%5D%EC%B9%B4%EB%93%9C%20%EC%84%9E%EA%B8%B0.py) G5(구현 시뮬레이션)


    
- 2022-06-12
    - [(BOJ 10815) 숫자 카드](https://github.com/minho511/algorithm_solution/blob/master/baekjoon_python/%5B10815%5D%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C.py) S5(자료구조 정렬 이분 탐색)
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

    </br>

    - [(LeetCode 200) Number of Islands](https://leetcode.com/problems/number-of-islands/) (그래프이론 bfs dfs)
        - 아주 기초적인 DFS, BFS 문제
        - [LeetCode 풀이 업로드](https://github.com/minho511/algorithm_solution/blob/master/leetcode/200_Number%20of%20Islands.ipynb)
