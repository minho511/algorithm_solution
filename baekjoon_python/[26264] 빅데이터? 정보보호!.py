# 문자열
# https://www.acmicpc.net/problem/26264
import sys; input=sys.stdin.readline
from collections import Counter
n = int(input())
count = Counter(input())
if count['s'] < count['b']:
    print("bigdata?")
elif count['s'] > count['b']:
    print("security!")
else:
    print("bigdata? security!")