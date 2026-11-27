from homework_7.makeheap.algo import build_heap, sift_down


def _greater(first, second):
    return second < first


def heapsort(arr):
    build_heap(arr, _greater)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end, _greater)
    return arr
