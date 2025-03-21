def blocks(N, M, K):
    if K % N == 0 and K // N <= M:
        return True
    if K % M == 0 and K // M <= N:
        return True
    return False

N, M = map(int, input("Введите размеры района: ").split('x'))
K = int(input("Введите количество кварталов: "))

if blocks(N, M, K):
    print("успешно")
else:
    print("неосуществимо")