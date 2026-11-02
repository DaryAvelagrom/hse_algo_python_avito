from homework_5.tracer.algo import tracer


def permutations(nums):
    result = []
    used = [False] * len(nums)
    path = []

    @tracer
    def backtrack(prefix):
        if len(prefix) == len(nums):
            result.append(prefix.copy())
            return

        for index, value in enumerate(nums):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            backtrack(path)
            path.pop()
            used[index] = False

    backtrack(path)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
