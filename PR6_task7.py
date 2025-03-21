def order_sushi(K):
    for b in range(K // 7 + 1):
        if (K - 7 * b) % 5 == 0:
            return True
    return False

K = int(input("Введите количество суши: "))
if order_sushi(K):
    print("Можно заказать.")
else:
    print("Нельзя заказать.")