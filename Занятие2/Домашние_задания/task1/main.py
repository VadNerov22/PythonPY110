def geometr(start: float = 1, step: float = 1, finish: float = 100):
    while start < finish:
        yield start ** (step - 1)
        start += start


if __name__ == "__main__":
    print(*geometr(1, 2))