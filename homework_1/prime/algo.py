def count_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i * i < n:
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1

    return sum(is_prime)

if __name__ == "__main__":
    n = int(input())
    print(count_primes(n))