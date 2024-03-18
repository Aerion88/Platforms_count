"""
Yandex-Практикум, Python-разработчик,
финальное задание: служба доставки
ID: 108220709 27 фев 2024, 13:00:20
53ms 4.14Mb
"""


def main():
    'Определение количества платформ, необходимого для задачи'
    with open('input.txt', 'r') as f:
        robots_str = f.readline().rstrip().split()
        robot_array = sorted([int(i) for i in robots_str])
        # отсоритрованный список роботов
        limit = int(f.readline().rstrip())
        # максимальный вес который может перевезти платформа
    left_index = 0
    right_index = len(robot_array) - 1
    platform_count = 0
    # Переменная для хранения резултата работы
    while left_index <= right_index:
        temp_sum = robot_array[left_index] + robot_array[right_index]
        if temp_sum <= limit:
            left_index += 1
        platform_count += 1
        right_index -= 1
    print(platform_count)


if __name__ == '__main__':
    main()
