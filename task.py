import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:  # Базовий випадок: якщо масив із 1 або 0 елементів, він вже відсортований
        return arr

    mid = len(arr) // 2  # Знаходимо середину масиву
    left_half = arr[:mid]  # Ліва частина
    right_half = arr[mid:]  # Права частина

    # Рекурсивно сортуємо обидві частини та з'єднуємо їх
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []  # Результуючий масив
    left_index = 0  # Індекс для лівого масиву
    right_index = 0  # Індекс для правого масиву

    # Порівнюємо елементи з обох масивів і додаємо менший у результуючий
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з лівого масиву (якщо є)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Додаємо залишкові елементи з правого масиву (якщо є)
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Поточний елемент для вставки
        j = i - 1
        # Зсув елементів, більших за ключ, вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Вставка ключа на його позицію
    return arr

# Порівняння алгоритмів
def compare_sorts():
    setup_code = "from __main__ import merge_sort, insertion_sort; import random"
    num_elements = [10, 100, 1000, 10000]  # Кількість елементів для тестування

    for n in num_elements:
        test_data = [random.randint(0, 10000) for _ in range(n)]  # Генерація тестових даних
        test_code_merge = f"merge_sort({test_data})"  # Тестовий виклик для merge_sort
        test_code_insertion = f"insertion_sort({test_data})"  # Тестовий виклик для insertion_sort
        test_code_sorted = f"sorted({test_data})"  # Тестовий виклик для вбудованого sorted
        test_code_sort = f"{test_data}.sort()"  # Виклик .sort() на самому списку

        print(f"Number of elements: {n}")  # Вивід кількості елементів
        print(
            "Merge Sort: ",
            timeit.timeit(stmt=test_code_merge, setup=setup_code, number=10),  # Замір часу для merge_sort
        )
        print(
            "Insertion Sort: ",
            timeit.timeit(stmt=test_code_insertion, setup=setup_code, number=10),  # Замір часу для insertion_sort
        )
        print(
            "Timsort (sorted): ",
            timeit.timeit(stmt=test_code_sorted, setup=setup_code, number=10),  # Замір часу для sorted
        )
        print(
            "Timsort (sort): ",
            timeit.timeit(stmt=test_code_sort, setup=setup_code, number=10),  # Замір часу для .sort()
        )
        print()

# Запуск порівняння
compare_sorts()