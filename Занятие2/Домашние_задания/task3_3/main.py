from collections.abc import Iterable
def prov_iter(fn) -> bool:
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, Iterable):
                raise TypeError(f"Объект {i} не является итерируемым")
        for k in kwargs:
            if not isinstance(k, Iterable):
                raise TypeError(f"Объект {k} не является итерируемым")
        print("OK")
    return wrapper


@prov_iter
def return_iter() -> iter:
    return " "


if __name__ == "__main__":
    return_iter()