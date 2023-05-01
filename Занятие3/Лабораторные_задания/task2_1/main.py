import json


def task() -> str:
    dict_numbers = {k: k ** 2 for k in range(1, 11)}
    return json.dumps(dict_numbers,indent=4)


if __name__ == "__main__":
    print(task())
