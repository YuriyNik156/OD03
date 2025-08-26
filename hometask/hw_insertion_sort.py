def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def convert(item):
    """Попытка превратить строку в число, если получится"""
    try:
        return int(item)
    except ValueError:
        return item   # остаётся строкой


try:
    user_input = input("Введите слова, фразы или числа через запятую: ")

    # убирать пробелы и делить строку по запятым
    items = [i.strip() for i in user_input.split(",") if i.strip()]

    if not items:
        raise ValueError("Вы ничего не ввели!")

    # конвертировать числа
    items = [convert(i) for i in items]

    # делить на числа и слова
    numbers = [x for x in items if isinstance(x, int)]
    words = [x for x in items if isinstance(x, str)]

    # сортировать отдельно
    sorted_numbers = insert_sort(numbers)
    sorted_words = insert_sort(words)

    # склеивать: сначала числа, потом слова
    sorted_items = sorted_numbers + sorted_words

    print("Отсортированный список:", sorted_items)

except Exception as e:
    print("Произошла ошибка:", e)
