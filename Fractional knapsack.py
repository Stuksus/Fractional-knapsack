# coding: utf-8


import heapq


def knapsack(array, capacity):
    array = [(-p / w, w) for p, w in array]
    heapq.heapify(array)
    total_income = 0
    while array and capacity:
        p, w = heapq.heappop(array)
        total_weight = min(w, capacity)
        total_income -= p * total_weight
        capacity -= total_weight
    return total_income


def main():
    print(
        ''' Введите через пробел количество товаров и доступный объем рюкзака.
        ''')
    n, capacity = map(int, input("Введите: ").split())
    print(
        '''Введите через пробел параметры товаров(-а). Сначала цену, потом вес
     ''')
    values = [tuple(map(int, input('Введите параметры товара № ' + str(i + 1) + ": ").split())) for i in range(n)]
    total = knapsack(values, capacity)
    print('Максимальный доход: ', total)


if __name__ == '__main__':
    main()
