def two_sum(arr, k):
    items_dict = {}
    for i, item in enumerate(arr):
        if k - item in items_dict:
            return items_dict[k - item], i
        items_dict[item] = i
    return -1, -1

if __name__ == "__main__":
    arr = [1, 3, 4, 10]
    k = 7
    print(two_sum(arr, k))

    arr = [5, 5, 1, 4]
    k = 10
    print(two_sum(arr, k))