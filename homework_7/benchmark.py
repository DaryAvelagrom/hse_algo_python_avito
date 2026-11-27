from random import Random
from statistics import median

from homework_6.compare.algo import measure_time, mergesort
from homework_7.heapsort.algo import heapsort
from homework_7.makeheap.algo import makeheap, makeheap_n_log_n


def compare(algorithms, cases, repeats=7):
    print("| N | Вход | " + " | ".join(sort.__name__ for sort in algorithms) + " |")
    print("| " + " | ".join(["---"] * (2 + len(algorithms))) + " |")
    timed = [measure_time(algorithm) for algorithm in algorithms]

    for label, nums in cases:
        timings = []
        for run in timed:
            elapsed = [run(nums.copy())[1] for _ in range(repeats)]
            timings.append(f"{1000 * median(elapsed):.3f}")
        print(f"| {len(nums)} | {label} | " + " | ".join(timings) + " |")


def main():
    cases = []
    rng = Random(7)
    for size in (10_000, 40_000, 160_000):
        descending = list(range(size, 0, -1))
        shuffled = descending.copy()
        rng.shuffle(shuffled)
        cases.extend([("по убыванию", descending), ("перемешанный", shuffled)])

    print("Makeheap, мс")
    compare((makeheap_n_log_n, makeheap), cases)
    print()
    print("Heapsort, мс")
    compare((heapsort, sorted, mergesort), cases)


if __name__ == "__main__":
    main()
