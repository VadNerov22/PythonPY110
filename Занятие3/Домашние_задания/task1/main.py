def write_list(file1, file2, file3):
    with open(file1) as f1, open(file2) as f2, open(file3, "w") as f3:
        return f3.write(f1.read() + "\n" + f2.read())


if __name__ == "__main__":
    write_list("list1.txt", "list2.txt", "list3.txt")
