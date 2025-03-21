N, K, M = map(int, input("Введите N, K, M: ").split())
total_rides = 2 * N
sessions = (total_rides + K - 1) // K
min_time = sessions * M
print(min_time)