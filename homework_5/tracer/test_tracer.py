import pytest

from homework_5.tracer.algo import tracer


def test_recursive_calls_and_returns(capsys):
    @tracer
    def factorial(n):
        """Calculate factorial."""
        return 1 if n <= 1 else n * factorial(n - 1)

    assert factorial(3) == 6
    assert capsys.readouterr().out.splitlines() == [
        "-> factorial(3)",
        "  -> factorial(2)",
        "    -> factorial(1)",
        "    <- factorial = 1",
        "  <- factorial = 2",
        "<- factorial = 6",
    ]
    assert factorial.__name__ == "factorial"
    assert factorial.__doc__ == "Calculate factorial."
    assert factorial(0) == 1
    assert capsys.readouterr().out.splitlines()[0] == "-> factorial(0)"


def test_keyword_arguments_and_none(capsys):
    @tracer
    def example(value, *, flag=False):
        return value if flag else None

    assert example("a", flag=True) == "a"
    assert capsys.readouterr().out.splitlines() == [
        "-> example('a', flag=True)", "<- example = 'a'",
    ]
    assert example(1) is None
    assert capsys.readouterr().out.splitlines()[-1] == "<- example = None"


def test_depth_restored_after_exception(capsys):
    error = ValueError("negative")

    @tracer
    def countdown(n):
        if n == 0:
            raise error
        return countdown(n - 1)

    with pytest.raises(ValueError) as caught:
        countdown(2)
    assert caught.value is error
    assert capsys.readouterr().out.splitlines() == [
        "-> countdown(2)", "  -> countdown(1)", "    -> countdown(0)",
        "    !! countdown: ValueError: negative",
        "  !! countdown: ValueError: negative",
        "!! countdown: ValueError: negative",
    ]
    with pytest.raises(ValueError):
        countdown(0)
    assert capsys.readouterr().out.splitlines()[0] == "-> countdown(0)"


def test_branching_recursion(capsys):
    @tracer
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    assert fibonacci(3) == 2
    lines = capsys.readouterr().out.splitlines()
    assert lines.count("  -> fibonacci(1)") == 1
    assert lines.count("    -> fibonacci(1)") == 1
    assert lines[-1] == "<- fibonacci = 2"
