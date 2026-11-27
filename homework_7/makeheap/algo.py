def _less(first, second):
    return first < second


def sift_down(arr, index, size, precedes=_less):
    while 2 * index + 1 < size:
        child = 2 * index + 1
        right = child + 1
        if right < size and precedes(arr[right], arr[child]):
            child = right
        if not precedes(arr[child], arr[index]):
            break
        arr[index], arr[child] = arr[child], arr[index]
        index = child


def build_heap(arr, precedes=_less):
    size = len(arr)
    for index in range(size // 2 - 1, -1, -1):
        sift_down(arr, index, size, precedes)


def makeheap(arr):
    build_heap(arr)
    return arr


def makeheap_n_log_n(arr):
    for index in range(1, len(arr)):
        while index > 0:
            parent = (index - 1) // 2
            if not arr[index] < arr[parent]:
                break
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
    return arr
