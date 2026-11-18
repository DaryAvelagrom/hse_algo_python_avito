from functools import wraps
from statistics import median
from time import perf_counter


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        return result, perf_counter() - start

    return wrapper


def merge(values, buffer, left, middle, right):
    i, j = left, middle
    for index in range(left, right):
        if i < middle and (j == right or values[i] <= values[j]):
            buffer[index] = values[i]
            i += 1
        else:
            buffer[index] = values[j]
            j += 1
    values[left:right] = buffer[left:right]


def partition(values, left, right):
    pivot = values[right - 1]
    boundary = left
    for index in range(left, right - 1):
        if values[index] < pivot:
            values[index], values[boundary] = values[boundary], values[index]
            boundary += 1
    values[boundary], values[right - 1] = values[right - 1], values[boundary]
    return boundary


def mergesort(nums):
    values = list(nums)
    buffer = [None] * len(values)

    def sort(left, right):
        if right - left <= 1:
            return
        middle = (left + right) // 2
        sort(left, middle)
        sort(middle, right)
        merge(values, buffer, left, middle, right)

    sort(0, len(values))
    return values


def quicksort(nums):
    values = list(nums)

    def sort(left, right):
        while right - left > 1:
            pivot = partition(values, left, right)
            if pivot - left < right - pivot - 1:
                sort(left, pivot)
                left = pivot + 1
            else:
                sort(pivot + 1, right)
                right = pivot

    sort(0, len(values))
    return values


def compare_times(nums, repeats=5):
    results = {}
    for sort in (mergesort, quicksort):
        timed_sort = measure_time(sort)
        results[sort.__name__] = median(timed_sort(nums)[1] for _ in range(repeats))
    return results


if __name__ == "__main__":
    cases = {
        "По возрастанию": list(range(1500)),
        "По убыванию": list(range(1500, 0, -1)),
        "Все элементы равны": [7] * 1500,
    }
    for label, nums in cases.items():
        print(label)
        for name, elapsed in compare_times(nums).items():
            print(f"  {name}: {elapsed * 1000:.3f} мс")
