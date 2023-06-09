import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"""#{4}.(?P<position>\d+)\..\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>.+?)\s+\((?P<recommended>\d+\.\d\%).\w+\W+?\[]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\".\[.+?\]\(.+?\)"""


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE, encoding='UTF-8') as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
