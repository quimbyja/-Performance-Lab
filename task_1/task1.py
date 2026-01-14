
"""
Тестыы на запуск в консоли:
python3 task1.py 4 2 6 4 -> 123414
python3 task1.py 6 3 5 4 -> 13514253
"""

import sys


def circular_arr(n, m):
    arr = []
    start_pos = 0

    while True:
        arr.append(str(start_pos + 1))
        start_pos = (start_pos + m - 1) % n
        if start_pos == 0:
            break

    return ''.join(arr)

def main():
    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    print(circular_arr(n1, m1) + circular_arr(n2, m2))


if __name__ == "__main__":
    main()


