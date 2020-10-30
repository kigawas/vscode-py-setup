from typing import Optional, Tuple


def f(a: int = None) -> Optional[int]:
    return a


def g(a: int):
    return f(a)


class Base:
    @classmethod
    def a(cls) -> Tuple[str, ...]:
        return ("a", "b")


class Sub(Base):
    @classmethod
    def a(cls) -> Tuple[str, ...]:
        return super().a() + ("c",)


if __name__ == "__main__":
    print(f"g result: {g(1)}")
    print(Sub.a())
