from heapq import heapify, heapreplace

from homework_7.makeheap.algo import makeheap, sift_down


def kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")

    heap = makeheap(nums[:k])
    for index in range(k, len(nums)):
        value = nums[index]
        if heap[0] < value:
            heap[0] = value
            sift_down(heap, 0, k)
    return heap[0]


def kth_largest_heapq(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")

    heap = nums[:k]
    heapify(heap)
    for index in range(k, len(nums)):
        value = nums[index]
        if heap[0] < value:
            heapreplace(heap, value)
    return heap[0]
