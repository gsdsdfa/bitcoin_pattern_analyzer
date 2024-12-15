import numpy as np


def validate_prices(prices):
    """
    Проверяет, что prices является одномерным массивом.

    :param prices: Входные данные для проверки.
    :raises ValueError: Если prices не является одномерным массивом.
    """
    prices = np.array(prices)
    if prices.ndim != 1:
        raise ValueError("prices должен быть одномерным массивом")
    return prices


def find_double_bottom(prices, threshold=0.05):
    """
    Находит паттерны двойного дна в массиве цен.

    :param prices: Одномерный массив цен.
    :param threshold: Допустимое отклонение для определения дна.
    :return: Список индексов и значений двойных днёв.
    """
    prices = validate_prices(prices)
    patterns = []

    for i in range(1, len(prices) - 1):
        # Проверяем, что текущая цена ниже предыдущей и следующей
        if prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
            # Проверяем, что цена на уровне дна (с учетом порога)
            if (abs(prices[i] - prices[i - 1]) < threshold * prices[i - 1] and
                    abs(prices[i] - prices[i + 1]) < threshold * prices[i + 1]):
                patterns.append((i, prices[i]))  # Сохраняем индекс и цену дна
    return patterns


def find_head_and_shoulders(prices):
    head_and_shoulders = []
    n = len(prices)

    for i in range(1, n - 1):  # Начинаем с 1 и заканчиваем на n-1
        # Проверяем, что индексы не выходят за пределы массива
        if (i + 1 < n and i + 2 < n and i - 1 >= 0 and
            prices[i] > prices[i - 1] and
            prices[i] > prices[i + 1] and
            prices[i + 1] < prices[i + 2]):
            head_and_shoulders.append((i - 1, i, i + 1, i + 2))  # Сохраняем индексы паттерна

    return head_and_shoulders


def find_patterns(prices):
    """
    Находит все паттерны в массиве цен.

    :param prices: Одномерный массив цен.
    :return: Словарь с найденными паттернами.
    """
    prices = validate_prices(prices)  # Проверяем и валидируем входные данные
    double_bottoms = find_double_bottom(prices)
    head_and_shoulders = find_head_and_shoulders(prices)

    return {
        "double_bottoms": double_bottoms,
        "head_and_shoulders": head_and_shoulders
    }