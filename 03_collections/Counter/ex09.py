from collections import Counter


def count_min_goals(stats: dict) -> Counter:
    # Инициализируем счетчик для хранения минимальных голов
    min_goals = Counter()

    # Проходим по всем годам и их статистике
    for year, players in stats.items():
        # Обновляем минимальные значения для каждого игрока
        for player, goals in players.items():
            if player not in min_goals:
                min_goals[player] = goals  # Если игрока нет, добавляем его
            else:
                min_goals[player] = min(min_goals[player], goals)  # Сравниваем и сохраняем минимум

    return min_goals



statistics = {
    2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
    2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
}

print(count_min_goals(statistics))