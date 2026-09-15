def max_even_sum(a):
    result_sum = 0
    min_odd = 0

    for item in a:
        result_sum += item
        if item % 2 == 1:
            if min_odd == 0 or item < min_odd:
                min_odd = item

    if result_sum % 2 == 0:
        return result_sum
    else:
        return result_sum - min_odd


if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(max_even_sum(a))  
