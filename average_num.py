def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


# Тесты для функции average_num

def test_average_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    expected = 3.0
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_average_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected = -3.0
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_average_mixed_numbers():
    numbers = [1, -1, 2, -2, 3]
    expected = 0.6
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_invalid_values():
    numbers = [1, "a", 3]
    expected = "Bad request"
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_string_with_number():
    numbers = [1, "2", 3]
    expected = 2.0
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_average_decimal_numbers():
    numbers = [0.5, 1.5, 2.5, 3.5, 4.5]
    expected = 2.5
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


def test_average_large_numbers():
    numbers = [1000000, 2000000, 3000000]
    expected = 2000000.0
    assert average_num(numbers) == expected, f"Expected {expected}, got {average_num(numbers)}"


# Запуск тестов
if __name__ == "__main__":
    test_average_positive_numbers()
    test_average_negative_numbers()
    test_average_mixed_numbers()
    test_invalid_values()
    test_string_with_number()
    test_average_large_numbers()
    test_average_decimal_numbers()
    print("All tests passed!")
