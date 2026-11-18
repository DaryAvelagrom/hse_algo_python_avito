from homework_6.compare.algo import merge, partition


def mergesort(nums):
    values = list(nums)
    size = len(values)
    buffer = [None] * size
    width = 1
    while width < size:
        for left in range(0, size - width, 2 * width):
            middle = left + width
            right = min(left + 2 * width, size)
            merge(values, buffer, left, middle, right)
        width *= 2
    return values


def quicksort(nums):
    values = list(nums)
    stack = [(0, len(values))]
    while stack:
        left, right = stack.pop()
        while right - left > 1:
            pivot = partition(values, left, right)
            if pivot - left < right - pivot - 1:
                stack.append((pivot + 1, right))
                right = pivot
            else:
                stack.append((left, pivot))
                left = pivot + 1
    return values
