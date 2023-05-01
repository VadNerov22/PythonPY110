import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda item: item["length"])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    with open("output.json", "w") as f1:
        f1.write(json.dumps(data, indent=4))
