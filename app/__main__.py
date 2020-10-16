from typing import Optional


def f(a: Optional[int] = None) -> Optional[int]:
    return a


def g(a):
    return f(a)


if __name__ == "__main__":
    print(f"g result: {g(1)}")
