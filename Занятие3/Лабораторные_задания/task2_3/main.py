import json


def task():
    filename = "input.json"
    with open(filename) as f:
        dic_ = json.load(f)

    return max(dic_, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
