from functools import wraps
from typing import Callable, ParamSpec, TypeVar, cast

T = TypeVar("T")
P = ParamSpec("P")

NOT_CALLED = object()


def single_call(f: Callable[P, T]) -> Callable[P, T]:
    result: T | object = NOT_CALLED

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        nonlocal result
        if result is NOT_CALLED:
            result = f(*args, **kwargs)

        return cast(T, result)

    return wrapper
