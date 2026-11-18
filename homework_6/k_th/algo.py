from random import randrange


def kth_largest(nums, k):
    values = list(nums)
    if not 1 <= k <= len(values):
        raise ValueError("k должно быть от 1 до длины массива")

    target = len(values) - k
    left, right = 0, len(values)
    while True:
        pivot = values[randrange(left, right)]
        lower, index, upper = left, left, right
        while index < upper:
            if values[index] < pivot:
                values[lower], values[index] = values[index], values[lower]
                lower += 1
                index += 1
            elif values[index] > pivot:
                upper -= 1
                values[index], values[upper] = values[upper], values[index]
            else:
                index += 1

        if target < lower:
            right = lower
        elif target >= upper:
            left = upper
        else:
            return pivot
