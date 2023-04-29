def int_(fn) -> bool:
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError(f"аргументы функции {fn} должны быть int")
        print("Ok")
    return wrapper


@int_
def return_int() -> int:
    return " "


if __name__ == "__main__":
    return_int()
