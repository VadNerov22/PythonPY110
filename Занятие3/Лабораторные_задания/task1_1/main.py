INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as f:
        for line in f:
            print(line, end="")


if __name__ == "__main__":
    task()
