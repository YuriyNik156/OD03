def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = [i for i in s if i < element]
    center = [i for i in s if i == element]
    right = [i for i in s if i > element]

    return quick_sort(left) + center + quick_sort(right)


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
    sorted_numbers = quick_sort(numbers)
    sorted_words = quick_sort(words)

    # склеивать: сначала числа, потом слова
    sorted_items = sorted_numbers + sorted_words

    print("Отсортированный список:", sorted_items)

except Exception as e:
    print("Произошла ошибка:", e)
