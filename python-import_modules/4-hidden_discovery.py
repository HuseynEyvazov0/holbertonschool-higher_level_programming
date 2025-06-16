#!/usr/bin/python3
import marshal
import sys

def main():
    path = "/tmp/hidden_4.pyc"
    with open(path, "rb") as f:
        f.read(16)  # Пропустить заголовок .pyc (в Python 3.7+ обычно 16 байт)
        code = marshal.load(f)  # Загрузить объект кода

    names = code.co_names
    # Отфильтровать имена, которые не начинаются с "__" и отсортировать их
    filtered_names = sorted(name for name in names if not name.startswith("__"))

    for name in filtered_names:
        print(name)

if __name__ == "__main__":
    main()
