import re
pattern = """(.|\n)+?"""

if __name__ == "__main__":
    with open("input.txt", encoding="UTF-8") as f:
        text = f.read()
    print(re.findall(pattern, text))

