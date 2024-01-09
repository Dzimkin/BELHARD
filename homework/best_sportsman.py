def search_best(self):
    best_result = results[0][0]
    best_sportsman = 1
    best_attempt = 1

    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j] > best_result:
                best_result = results[i][j]
                best_sportsman = i + 1
                best_attempt = j + 1

    return best_sportsman, best_attempt


results = [
    [5.6, 5.9, 6.2],
    [5.7, 6.1, 6.4],
    [5.8, 6.2, 6.5],
    [5.9, 5.9, 6.1],
    [6.0, 6.0, 6.3]
]
best_sportsman, best_attempt = search_best(results)

print(f"Лучший спортсмен: {best_sportsman}")
print(f"Лучшая попытка: {best_attempt}")
