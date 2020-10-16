from typing import Optional


def f(a: Optional[int] = None) -> Optional[int]:
    return a


def g():
    return f()


if __name__ == "__main__":
    g()
