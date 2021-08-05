# algorithm_sol  
알고리즘 공부를 위한 저장소  

## 기록
#### 2021 08 05
  - baekjoon 15991 1,2,3 더하기 6 S1(다이나믹프로그래밍)
  - baekjoon 15992 1,2,3 더하기 7 S1(다이나믹프로그래밍)
  - baekjoon 15993 1,2,3 더하기 8 S1(다이나믹프로그래밍)
  - baekjoon 16195 1,2,3 더하기 9 S1(다이나믹프로그래밍)
  > 표를 그리고 규칙을 찾아 dp테이블을 만들어 푼다.


#### 2021 08 04
  - baekjoon 1464 뒤집기 3 G5(문자열 그리디)
    - 지금까지푼 G5문제중 가장어려웠던 문제
    - 단순하게 접근하면 메모리, 시간초과가 난다.

#### 2021 08 03
  - baekjoon 1543 문서 검색 S4(문자열 그리디 브루트포스)
    - 파이썬의 .count 로 쉽게 풀수있는 문제
  - baekjoon 2800 괄호 제거 G5(자료 구조 문자열 스택 재귀)
    - 중복제거를 하지 않아 오류발생

#### 2021 08 02
  - baekjoon 9019 DSLR G5(그래프 이론 그래프 탐색 너비 우선 탐색)
    - deque.rotate, 문자열로 R,L함수를 구현하려 하였으나 시간초과, 수식으로 해결
    - PyPy3로 정답처리
  - baekjoon 1068 트리 G5(그래프 이론 그래프 탐색 트리 깊이 우선 탐색)
    - dfs로 해결하였다.

#### 2021 07 31
  - baekjoon 1992 쿼드트리 S1(분할 정복 재귀)
  - baekjoon 14500 테트로미노 G5 (구현 브루트포스 알고리즘)
    - PyPy3 로 정답처리
    > **방문한 곳을 다시 방문**해야하는 경우 방문하여 정보를 얻은 후 visited를 다시 False로 돌려주는 작업필요
    - DFS를 사용하여 거꾸로 돌아가며 모든 경우의수를 고려하는 **백트래킹**을 구현

#### 2021 07 30
  - baekjoon 1021 회전하는 큐 S4(자료구조 덱)
    - deque.rotate를 사용하여 풀었다.  

#### 2021 07 29
  - baekjoon 1707 이분 그래프 G4(그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색)
    - 이분그래프 개념 공부 [참고](https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html)  
    <img src = "https://gmlwjd9405.github.io/images/data-structure-graph/bipartite-graph1.gif" width = "400" height = "160" >  
  - baekjoon 1374 강의실 G5(자료 구조 그리디 알고리즘 정렬 우선순위 큐)
  - baekjoon 7569 토마토 S1(그래프 이론 그래프 탐색 너비 우선 탐색)
    - PyPy3로는 정답처리 받았으나 Python3로는 시간 초과.. 다른 코드 참고  

#### 2021 07 28
  - baekjoon 6064 카잉 달력 S1(수학 정수론 중국인의 나머지 정리)
  - baekjoon 16968 차량 번호판 B1(수학 조합론)  
  - baekjoon 11728 배열 합치기 S5(정렬 두 포인터)
  - baekjoon 1015 수열 정렬 S4(정렬)  
  - baekjoon 4396 지뢰찾기 S5(구현 문자열 파싱)
    - bfs로 그래프 두개를 비교하면서 탐색
  - baekjoon 2004 조합 0의 개수 S2(수학 정수론)   

#### 2021 07 27
  - baekjoon 1389 케빈 베이컨의 6단계 법칙 S1(그래프 이론 그래프 탐색 너비 우선 탐색 플로이드–와샬)
    - 모든 노드 서로간의 최단거리를 구해야 하므로 플로이드 워셜 알고리즘으로 풀 수 있다.  
  - baekjoon 16928 뱀과 사다리게임 S1(그래프 이론 그래프 탐색 너비 우선 탐색)
    - bfs로 풀수있었다.


#### 2021 07 26
  - baekjoon 5430 AC G5(구현 자료 구조 문자열 파싱 덱)
  - baekjoon 1934 최소공배수 S5(수학 정수론 유클리드 호제법)
    - 유클리드 호제법으로 풀었다.
  - baekjoon 1037 약수 S5(수학 정수론)  

#### 2021 07 25
  - baekjoon 9375 패션왕 신해빈 S3(수학 자료 구조 문자열 해시를 사용한 집합과 맵)
  - baekjjon 1541 잃어버린 괄호 S2(수학 문자열 그리디 알고리즘 파싱)
    - .lstrip('0')를 사용하여 문자열 앞의 0을 모두 제거할 수 있다.
    ```python
    >> s = '00204112300'
    >> s.lstrip('0')
    '204112300'
    >> s.rstrip('0')
    '002041123'
    >> s.strip('0')
    '2041123'
    ```
  - baekjoon 11286 절댓값 힙 S1(자료 구조 우선순위 큐)  
  - baekjoon 14888 연산자 끼워넣기 S1(브루트포스 백트래킹)
    - PyPy3로 정답처리
    - 백트래킹 [참고](https://namu.wiki/w/%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9)  
  - baekjoon 10026 적록색약 G5(그래프이론 그래프탐색 너비우선탐색 깊이우선탐색)
    - bfs를 사용하여 해결
    - 아이디어:
      1. bfs를 처음 처음 사용할때 RGB를 구분하여 영역을 세면서 RG / B 구분하여 방문처리를 한다.
      2. 1.에서 얻은 graph에 대하여 bfs를 사용하여 적록색약이 보는 영역을 센다.
  - baekjoon 1107 리모컨 G5(브루트포스)  


#### 2021 07 24
  - baekjoon 5525 IOIOI S2(문자열)
    - 디지털논리회로수업에서 배운 상태다이어그램을 그려서 해결  
  - baekjoon 1780 종이의 개수 S2(분할정복 재귀)
    - PyPy3로 정답처리
  - baekjoon 11659 구간 합 구하기 4 S3(누적합)
    - 누적합을 저장해놓는 prefix sum 리스트를 만들어놓고 연산하는 방법이 효율적
  - baekjoon 17219 비밀번호 찾기 S4(자료 구조 해시를 사용한 집합과 맵)


#### 2021 07 23
  - baekjoon 1074 Z S1(분할정복 재귀)
    - 수학으로 풀었다.
  - baekjoon 1697 숨바꼭질 S1(그래프이론 그래프탐색 너비우선탐색)
    - bfs로 풀었다.
  - baekjoon 11399 ATM S3(그리디 정렬)
  - baekjoon 2630 색종이 만들기 (재귀 분할정복)
  - [ ] zip  
#### 2021 07 22
  - baekjoon 17626 Four Squares S5(브루트포스 다이나믹프로그래밍)
    - PyPy3로 정답처리
  - baekjoon 1676 팩토리얼 0의 개수S4(수학)
  - baekjoon 1620 나는야 포켓몬 마스터 이다솜 S4(자료 구조 해시를 사용한 집합과 맵)
    |메서드|기능|
      |---|---|
      |(str).isdigit()| 숫자로만 구성된 문자열인지 판단 |
      |(str).isalpha()| 알파벳으로만 구성된 문자열인지 판단 |  
  - baekjoon 1764 듣보잡 S4(자료구조 문자열 정렬)
    - 이진탐색 알고리즘으로 풀었다.
    - collections.Counter 모듈을 사용한 코드가 더욱 빠르게 동작
  - baekjoon 7662 이중 우선순위 큐 S5(자료 구조 우선순위 큐 트리를 사용한 집합과 맵)
    - heapq를 이용하여 최대힙 최소힙을 동시에 구현하는 문제였는데 시간복잡도를 줄이기가 굉장히 어려웠다.
    - 파이썬의 heapq에서는 최소힙만 지원하기 때문에 최대힙을 사용하기 위해서 우선도에 -를 넣어 만든 리스트를 추가로 만들어줬다.
    - 최대힙에서 추출한 원소와 최소힙에서 추출한 원소를 동시에 서로의 리스트에 공유하기 위해서 visited 리스트에 방문여부를 저장하고
        최대힙 최소힙에서 원소를 추출하기 전에 그 원소가 이미 추출된 원소인지 검사하여 제거한다.
    - **`마지막으로 최댓값 최솟값을 꺼내기전에 두리스트에 남아있는 방문처리된 원소를 제거하는 과정이 필요했다.`**
  - baekjoon 11279 최대힙 S2(자료구조 우선순위 큐)
  - baekjoon 1927 최소힙 S1(자료구조 우선순위 큐)
  - baekjoon 11724 연결 요소의 개수 S2(그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색)
    - bfs로 풀었지만 서로소 집합 자료구조로도 해결할 수 있었다.

#### 2021 07 21
  - baekjoon 18111 마인크래프트 S3(구현 브루트포스)
  - baekjoon 1990 소수인팰린드롬 G5(수학 구현 문자열 정수론 소수 판정 에라토스테네스의 체)
    - 팰린드롬수를 검사할 때
      ```python
      def is_palindrome(n):
        return str(n) == str(n)[::-1]
      ```
      보다 양쪽에서 한문자씩 검사하여 중간에라도 팰린드롬수가 아닌것을 알았을 때 False처리해주는것이 더 빠르게 동작
      ```python
      def is_palindrome(n):
        s_string = str(n)
        l = len(s_string)
        for k in range(l//2):
          if s_string[k] != s_string[-k-1]:
            return False
        return True
      ```
  - baekjoon 11723 집합 S5(구현 비트마스킹)
  
#### 2021 07 20
  - baekjoon 9009 피보나치 S1(수학 그리디)
  - baekjoon 1041 주사위 S1(수학 그리디)
  - join
  ```python
  >> array = ['a', 'b', 'c']
  >> "".join(array)
  'abc'
  >> ", ".join(array) # 구분자 활용
  'a, b, c'
  ```
  - baekjoon 14425 문자열 집합 S3(자료 구조 문자열 트리를 사용한 집합과 맵)
    - in 문을 사용하였을 때 시간효율이 매우 안좋았다.
    - dict 자료형으로 원소가 있는지 없는지를 1 0 으로 등록하는 방식으로 풀었을때 빠르게 동작하였다.
    ```python
    >>> x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    >>> x.get('a')
    10
    >>> x.get('z', 0)
    0
    ```  

#### 2021 07 19
  - baekjoon 1388 바닥장식 S5(그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색)
    - bfs를 사용하여 풀었으나 굳이 bfs를 사용하지 않아도 간단히 풀 수 있는 문제
  - baekjoon 7576 토마토 S1(그래프 이론 그래프 탐색 너비 우선 탐색)
    - bfs를 문제조건에 맞게 변형
  - baekjoon 4963 섬의 개수 S2(그래프 이론 그래프 탐색 너비 우선 탐색)
  - baekjoon 2644 촌수 계산 S2(그래프 이론 그래프 탐색 너비 우선 탐색)
    - bfs로 깊이를 계산
    - 플로이드-워셜 풀이가 더 간단하지만 메모리효율이 좋지 않음
  - baekjoon 11403 경로찾기 S1(그래프이론 플로이드워셜)
    - 플로이드워셜로 풀었으나 시간효율이 좋지 않음
    - DFS/BFS로 다시 풀어봄  


#### 2021 07 18
  - baekjoon 17298 오큰수 G4(자료구조 스택)
    - 지금까지 자료구조 문제중에 제일 어려웠다. 다른사람 아이디어 참고  

#### 2021 07 17
  - baekjoon 2617 구슬 찾기 G5(그래프이론 그래프탐색 깊이우선탐색 플로이드–와샬)
    - 플로이드-워셜 / DFS 두가지 방식으로 풀었다.. DFS가 더 효율적이었다.
  - baekjoon 18870 좌표 압축 S2(정렬 값/좌표압축)
    - 시간초과가 계속되었다.
    > array.index보다 디셔너리에 인덱스와 함께 저장하여 꺼내는것이 더 빠르게 동작하였다.  
  - baekjoon 15649 N과 M (1) S3(백트래킹)
  - baekjoon 15650 N과 M (2) S3(백트래킹)
  - baekjoon 15651 N과 M (3) S3(백트래킹)
  - baekjoon 15652 N과 M (4) S3(백트래킹)
    - N과 M 1~4 문제는 모두 itertools의 순열과 조합을 다루는 클래스로 간단하게 해결할 수 있었다.    

      |클래스|기능|
      |---|---|
      |permutations(data, r)| 순열 계산 |
      |combinations(data, r)| 조합 계산 |
      |product(data, repeat=r)| 원소를 중복해서 뽑는 순열 계산 |
      |combinations_with_replacement| 원소를 중복해서 뽑는 조합 계산 |  
  - baekjoon 18258 큐2 S4(자료구조 큐)


  - 계획  
    - [ ] .join  
    - [ ] map  
    
#### 2021 07 16
  - baekjoon 1931 회의실 배정 S2(그리디 정렬)
    - 정렬을 두번 수행해야 했던 문제
    - 원소가 두개인 튜플이 담긴 배열을 정렬할 때, 튜플의 첫번째 원소에 대하여 오름차순 정렬 후 두번째 원소에
      대하여 오름차순 정렬 하고싶을때 아래와 같이 할 수 있다.
    ```python
    array.sort(key=lambda data:(data[1], data[0])
    ```  
    위 코드는 아래와 같이 동작한다.
    ```python
    array.sort()
    array.sort(key=lambda data:data[1])
    ```  
  - baekjoon 7568 덩치 S5(구현 브루트포스)  
  - baekjoon 4949 균형잡힌 세상 S4(자료구조 문자열 스택)  
  - baekjoon 10773 제로 S4(구현 자료구조 문자열 스택)  
  - baekjoon 1584 게임 G5(그래프 이론 그래프 탐색 너비우선탐색 누적합 다익스트라 0-1너비우선탐색)
    - 보통의 다익스트라 알고리즘 문제와 다르게 좌표평면을 탐색하며 최소비용을 찾는 방식으로 풀었다.
  - baekjoon 2805 나무 자르기 S3(이분탐색)
    - 전형적인 이분탐색 문제였지만 python3로 채점받을때 계속 시간초과가 났다  
    해결) collections.Counter 모듈을 사용 [(참고)](https://docs.python.org/3/library/collections.html#collections.Counter)
    ```python
    tree = Counter(map(int, input().split()))
    
            (중간생략)
            
    for i, cnt in tree.items():
    if i>=h:
        get += (i-h)*cnt
    ```
    위와 같이 같은 높이의 나무를 한번에 처리함으로써 연산 횟수를 줄일 수 있다.  
  - baekjoon 15829 Hashing B2(문자열 해싱)  
      
#### 2021 07 15
  - baekjoon 14496 그대, 그머가 되어 (그래프이론 그래프탐색 너비우선탐색 다익스트라)
  - baekjoon 1753 최단경로 (그래프이론 다익스트라)  
  - baekjoon 5972 택배배송 (그래프이론 다익스트라)  
#### 2021 07 14
  - baekjoon 2609 최대공약수와 최소공배수 (수학 정수론 유클리드 호제법)
    - 유클리드 호제법 [(위키백과)](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95)
  - baekjoon 11050 이항 계수 1 (수학 구현 조합론)
  - baekjoon 10814 나이순 정렬 (정렬)
    - 실수  
    ```python
    age, name = map(str, input().split())
    ```  
    위와같이 age와 name을 입력 받고 age를 str형으로 사용해서 정렬할때 문제가 생겼다.  
  - baekjoon 2164 카드2 (자료구조 큐)
  - baekjoon 9012 괄호 (자료구조 문자열 스택)
  - baekjoon 2798 블랙잭 (브루트포스)
  - baekjoon 1018 체스판 다시 칠하기 (브루트포스)
  - baekjoon 2108 통계학 (구현 정렬)
    - print()를 여러번 호출하지 않고 seq="\n"을 활용하여 한번 호출로 출력
    ```python
    print(a, b, c, sep="\n")
    ```  
  - baekjoon 11651 좌표 정렬하기 2 (정렬)  
  
#### 2021 07 13
  - baekjoon 10866 덱 (자료구조 덱)
    - collections.deque 모듈 사용 (https://wikidocs.net/104977)  
  - baekjoon 1259 팰린드롬수 (구현 문자열)
  - baekjoon 1874 스택 수열 (자료구조 스택)
  - baekjoon 1436 영화감독 숌 (브루트포스)
  - baekjoon 1966 프린터 큐 (구현 자료구조 시뮬레이션 큐)
    - collections.deque 모듈 사용
    - 조건을 꼼꼼히 읽지 않아서 계속 틀렸다.
  - baekjoon 11866 요세푸스 문제 0 (자료구조 큐)  
  - baekjoon 1309 동물원 (다이나믹 프로그래밍)
    - 직접 세어 보면서 규칙을 찾고 수열을 만들어 풀었다.
    - 다른 풀이: 
    > 타일문제처럼 i번째 칸을 추가하면서 생길 수 있는 경우의 수에 대하여 DP테이블을 만든다.  
    
     이 문제에서 타일을 추가할때 마다 생각해야하는 경우의 수는 i-1번째 칸이
     1) 비어있는 경우
     2) 왼쪽에 사자가 있는 경우
     3) 오른쪽에 사자가 있는 경우  

     세가지 였으므로 리스트 세개를 만들어 풀 수 있었다.  
  - baekjoon 10845 큐 (자료구조 큐)

#### 2021 07 12
  - baekjoon 2512 예산 (이분탐색)
  - baekjoon 1010 다리 놓기 (수학 다이나믹 프로그래밍 조합론)  
    - DP Table 팩토리얼
  - baekjoon 9657 돌 게임 3 (다이나믹 프로그래밍 게임이론)
    - 1과 0의 state를 이용해 상태표를 만들어서 식을 간단하게 만들었다.   
      -> 코드가 훨씬 간결해졌다.
  -  baekjoon 2920 음계 (구현)  
  -  baekjoon 2231 분해합 (브루트포스)  
     - 어떤 수의 각 자릿수의 합을 구하기위한 코드를 짤때 아래와 같이 작성하는 것이 정석이지만
     ```python
     def n_sum(num):
       temp = 0
       while num > 0:
           temp += num % 10
           num //= 10
       return temp
     ```  
       파이썬의 장점을 살려 다음과 같이 코드를 작성할 수도 있다.
     ```python
     num = sum(map(int, str(num)))
     ```  
  - baekjoon 9656 돌 게임 2 (다이나믹 프로그래밍 게임이론)
    - 다이나믹프로그래밍 / 규칙을 찾아 수식으로 정리 두가지 방법으로 풀 수 있다.  
  - baekjoon 10826 피보나치 수 4 (다이나믹 프로그래밍 임의 정밀도 / 큰 수 연산)  
    - **`baekjoon 1699 제곱수의 합`**(수학 다이나믹 프로그래밍 정수론)
      - 최근 문제들 중 가장 어려웠던 문제  
  - baekjoon 11727 2xn 타일링 2 (다이나믹 프로그래밍)


#### 2021 07 11
  - baekjoon 1072 게임 (이분탐색 수학)
    - 배열 없이 대소 관계 만을 비교하며 적정값을 찾을때에도 이분탐색을 사용할 수 있음
    ```python
    x = 1000000111
    y = 470000333
    100*x/y  # 212.76583031697555
    x/y*100  # 212.76583031697552
    ```
    - "100*x/y"은 정답처리를 받았으나  "x/y*100"로 계산하였을때는 오답처리를 받았다.
  - baekjoon 2417 정수 제곱근 (이분탐색 수학)
  - baekjoon 2428 표절 (정렬 이분 탐색 슬라이딩 윈도우)


#### 2021 07 10
  - baekjoon 1427 소트인사이드 (문자열 정렬)
    - 파이썬의 장점을 살린 코드 참고
    ```python
    print(''.join(sorted(input())[::-1]))
    # 입력: 54236 출력: 65432
    ```
  - baekjoon 2752 세수정렬 (정렬)
  - baekjoon 2238 경매 (구현 정렬)
    - 데이터의 크기가 제한되어 정수 형태로 표현할 수 있음 => 계수정렬을 활용
  - baekjoon 2246 콘도선정 (구현 브루트포스 정렬)
    - 패턴이 보이지 않을때는 우선 문제의 조건을 코드로 옮기고 최적화
  - baekjoon 1448 삼각형 만들기 (수학 정렬)  
  - baekjoon 2693 N번째 큰 수 (구현 정렬)  
  - baekjoon 11650 좌표 정렬하기 (정렬)
  - baekjoon 1487 물건팔기 (정렬 브루트포스)  
  - baekjoon 2910 빈도정렬 (구현 자료 구조 정렬 트리를 사용한 집합과 맵)  
    - (a,b)로 이루어진 원소들을 a에 대해서만 정렬해야 했다.
    ```python
    def setting(data):
      return data[0]
    array.sort(reverse=True, key=setting) # data[0]에 대해서만 정렬할 수 있다.
    ```  
    lambda 활용
    ```python
    array.sort(reverse=True, key = lambda data: data[0])
     ```
#### 2021 07 09
  - baekjoon 1251 단어 나누기 (구현 문자열 브루트포스 정렬)
    - 문자열 뒤집기
    ```python
    s = "Hello World"
    s[::-1]
    # 'dlroW olleH'
    ```
  - baekjoon 1292 쉽게푸는 문제 (수학 구현)
    - 반복문을 최대한 줄이는 방법을 생각
    ```python
    array = []
    for i in range(1,46):   # 이중반복문
        for j in range(i):
           array.append(i)
    # 보다 효율적
    for i in range(1, 46):  # 단일반복문
        array += [i] * i
    #>> array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, , , ,]
    ```
  - baekjoon 1012 유기농 배추 (그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색)
    - DFS로 해결
    - PyPy3로 제출했을 때는 정답처리 받았으나 Python3로 제출시 RecursionError
    > BOJ 채점 서버에서 재귀 깊이를 1000으로 정해두었기 때문에 발생하는 오류
    ```python
    sys.setrecursionlimit(1000000)
    ```
    위 코드를 추가하여 해결  
  - baekjoon 16173 점프왕 쩰리 (구현 그래프이론 그래프탐색 브루트포스 BFS/DFS)
    - BFS로 해결 : 시작 지점에서 가까운 노드부터 탐색할 때 효과적
  - baekjoon 1325 효율적인 해킹 (그래프 이론 그래프 탐색 너비 우선 탐색 깊이 우선 탐색)
    - 메모리와 시간제한이 까다로워서 시간이 오래걸렸다.
    - PyPy3로 정답처리 받았다. python3로는 정답처리를 받지 못했다.
    - DFS로 작성하였을때 시간초과가 계속발생하여 BFS로 해결
    - 출력양식을 구현하는 것이 오래걸렸다. (반복문, 배열 최소로 사용)
<br>  

#### 2021 07 08
  - baekjoon 1009 분산처리 (구현 수학)
    - 처음에 사용하려고 만든 리스트 원소값을 잘못줘서 시간이 오래걸림
  - baekjoon 1205 등수구하기 (구현 정렬)
  - baekjoon 1212 8진수 2진수 (구현 수학 문자열)
    - 파이썬 2, 8 16 진수 (참고)
    ```python
    format(0b1011011, 'd')  # '91'
    format(91,'b')          # '1011011'
    format(91, 'o')         # '133'
    int("1011011",2)        # 91
    int("314",8)            # 204
    ```
#### 2021 07 07
  - baekjoon 5585 거스름돈 (그리디)
  - baekjoon 15881 Pen Pineapple Apple Pen (그리디 문자열 다이나믹프로그래밍)
    - 파이썬 문자열 함수 count()로 간단하게 작성
  - baekjoon 16756 Pismo (구현 그리디)
  - baekjoon 16770 The BucketList (구현 그리디 정렬 시뮬레이션)  
  - baekjoon 18238 ZOAC 2 (구현 문자열 그리디)  
    - 좀 더 정리할 수 있었다
  - baekjoon 1417 국회의원 선거 (구현 자료 구조 그리디 시뮬레이션 우선순위 큐)
    - heapq 모듈을 이용해 우선순위 큐 자료구조로 풀었다.
    - 최소 힙을 최대 힙처럼 사용하기 위하여 우선순위 값에 -를 붙여 넣는 방식을 사용
    ```python
    heapq.heappush(q, (-m, m))
    ```
  - baekjoon 1343 폴리오미노 (그리디)
    - 파이썬의 in 연산자와 replace 함수로 쉽게 풀 수 있다.  
  - baekjoon 1439 뒤집기 (그리디)
  - baekjoon 1789 수들의 합 (그리디 수학)
  - baekjoon 4796 캠핑 (그리디 수학)
    - enumerate를 활용한 풀이가 더 효율적 
    > 테스트케이스를 셀 때 루프마다 +연산을 하는것보다 입력받은 여러줄을 리스트로 만들어 enumerate를 활용 
    ```python
    cases = sys.stdin.read().splitlines()
    for i, case in enumerate(cases):
                       ~
                       ~
        print("Case {}: {}".format(i+1, result)
    ```  
#### 2021 07 06
  - baekjoon 2720 세탁소 사장 동혁 (그리디)
    - 전형적인 거스름돈 문제
  - baekjoon 11034 캠거루 세마리2 (그리디 수학)
    - 종료 조건없이 여러개의 테스트 케이스로 이루어진 문제
      - `try-except` 문 또는 `sys 모듈`을 사용한다.  
  - baekjoon 1434 책정리 (그리디 수학 사칙연산)
  - baekjoon 2810 컵홀더 (그리디 문자열 구현)
  
  |함수|기능|
   |---|---|
   |eval(string)| str형태의 계산식을 계산하여 반환한다. |  
  
#### 2021 07 05
  - 최소신장트리 크루스칼(Kruskal) 알고리즘 개념
  - 서로소 집합 자료구조 개념
  - 위상정렬(Topology Sort) 알고리즘 개념
  - baekjoon 1564 팩토리얼5 (수학)
    - DP테이블을 쓸 필요가 없었다
    - 다른 사람 코드에서 .zfill()함수를 보았다.  
 
   |함수|기능|
   |---|---|
   |(문자열)`.zfill`(width)| width 만큼의 길이가 되도록 앞을 0으로 채운다.|
   |(문자열)`.rjust`(width, "문자열")| width 만큼의 길이가 되도록 앞을 특정 문자열로 채운다.|
   
#### 2021 07 04
  - baekjoon 13900 순서쌍의 곱의 합 (수학)
    - 메모리와 시간 제한이 까다로웠다.
    - 반복문을 한번 사용하여 풀수 있도록 수식을 정리
  - baekjoon 4948 베르트랑 공준 (수학 정수론 소수판정 에라토스테네스의 체)
    - [에라토스테네스의 체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)  
    <img src = "https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif" width = "300" height = "250" >  
  - baekjoon 1024 수열의 합 (수학)  
  - baekjoon 9045 골드바흐의 추측 (수학 정수론 소수판정 에라토스테네스의 체)
    - 출력값이 주어진 짝수를 2로 나눈 값에서 같은 간격에 있음을 발견하여 이중반복문을 사용하지 않아도 됐다.
    - 수학 문제는 식을 간결하게 정리하고 시작할 것  
  - baekjoon 11729 하노이 탑 이동 순서
    - 생각나는 방식을 코드로 구현하기가 어려웠다.
    - 재귀함수 문제 더 풀어볼것  

#### 2021 07 03
  - baekjoon 2309 일곱 난쟁이
    - 브루트포스 알고리즘이 무엇인지
    - 비교적 짧고 빨랐던 다른 코드 참고
    - n개의 정수를 입력받을 때 
    - 리스트원소합
  ```python 
  array = [int(input()) for i in range(n)]
  array_sorted = sorted(int(input())for i in range(n))
  ```
  ```python
  A = [1,5,3]
  print(sum(A)) # >> 9
  ```
  - baekjoon 10162 전자레인지 (수학 구현 그리디)
    - 매우쉬움
  - baekjoon 14221 편의점 (다익스트라 그래프)
    - 기존 문제들과 다르게 함수를 여러번 호출 해야했다.  
i*j번 함수를 호출 할 필요없이 j반복문 밖에서 함수가 반환하는 배열을 변수에 할당하여
함수를 불러오는 횟수를 줄일 수 있었다.
  ```python
  for i in home:
    check_array = dijkstra(i)
    for j in store:
        if check_array[j] < min_dist:
            min_index = i
            min_dist = check_array[j]
  ```
  - baekjoon 17608 막대기
    - 자료구조 공부 필요
  - 서로소 집합 알고리즘 개념


#### 2021 07 02
  - 최단경로 알고리즘 다익스트라/플로이드 워셜 문제 풀이
  - baekjoon 18352 특정거리의 도시 찾기 (다익스트라)
  - baekjoon 1446 지름길 (다익스트라, 다이나믹 프로그래밍, 그래프 이론)
  - chap.10 그래프 이론 공부
  
#### 2021 07 01
  - 최단경로 알고리즘 다익스트라/플로이드 워셜 공부
  - baekjoon 13305 주유소 (그리디)
