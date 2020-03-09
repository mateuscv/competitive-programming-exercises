from math import ceil
queries = int(input())

for i in range(queries):
    number_of_goods = int(input())
    goods_prices = [int(x) for x in input().split()]
    sum_of_prices = sum(goods_prices)
    new_price = ceil(sum_of_prices/number_of_goods)
    print(new_price)