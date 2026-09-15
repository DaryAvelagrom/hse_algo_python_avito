def is_palindrome(n):
    max_pow = 0
    while 10 ** max_pow <= n:
        max_pow += 1

    for i in range(max_pow // 2 + 1):
        if (n // 10 ** i) % 10 != (n // 10 ** (max_pow - i - 1)) % 10:
            return False
    return True

def is_palindrome_2(n):
    reversed_n = 0
    copy_n = n
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n == copy_n

if __name__ == "__main__":
    n = int(input())
    print(is_palindrome(n))
    print(is_palindrome_2(n))