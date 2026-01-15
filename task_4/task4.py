import sys
"""
Для запуска одного из примеров следующие команды:
Пример 1: python3 task4.py test1.txt
Пример 2: python3 task4.py test2.txt
"""
test = sys.argv[1]

def read_test():
    arr = []
    with open(test, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            arr.append(int(line))
    return sorted(arr)


nums = read_test()
mediana = nums[len(nums) // 2]
min_moves = sum(abs(x - mediana) for x in nums)
if min_moves > 20:
    print("20 ходов недостаточно для приведения\n"
    "всех элементов массива к одному числу")
else:
    print(min_moves)