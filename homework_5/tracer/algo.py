from functools import wraps


def tracer(func):
    depth = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        arguments = [repr(arg) for arg in args]
        arguments.extend(f"{key}={value!r}" for key, value in kwargs.items())
        indent = "  " * depth
        print(f"{indent}-> {func.__name__}({', '.join(arguments)})")
        depth += 1
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            print(f"{indent}!! {func.__name__}: {type(error).__name__}: {error}")
            raise
        else:
            print(f"{indent}<- {func.__name__} = {result!r}")
            return result
        finally:
            depth -= 1

    return wrapper


if __name__ == "__main__":
    @tracer
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    factorial(4)
