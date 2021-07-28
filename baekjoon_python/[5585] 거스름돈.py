# 2021 07 07 그리디
n = int(input())
exchange = 1000-n
c_500 = exchange // 500
c_100 = exchange%500 // 100
c_50 = exchange%100 // 50
c_10 = exchange%50 // 10
c_5 = exchange%10 // 5
c_1 = exchange%5
print(c_1+c_5+c_10+c_50+c_100+c_500)


