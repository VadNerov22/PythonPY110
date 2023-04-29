def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


def task():
    count = sum(((pair[1][0] - pair[0][0]) ** 2 + (pair[1][1] - pair[0][1]) ** 2) ** 0.5 for pair in pairwise(pts))

    print(count)


if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    task()
