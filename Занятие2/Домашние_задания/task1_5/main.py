from string import ascii_lowercase, ascii_uppercase, digits
from random import sample

def parol(n: int = 8) -> str:
    list_ = ascii_lowercase + ascii_uppercase + digits
    yield sample(list_, n)


if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    print("".join(*parol()))
