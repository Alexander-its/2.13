#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from packet.add import add
from packet.help import help
from packet.list import list
from packet.select import select


def main():
    spisok = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            sp = add()
            spisok.append(sp)
        elif command == "list":
            list()
        elif command.startswith("select"):
            name = input("Введите имя человека ")
            select()
        elif command == "help":
            help()
        else:
            print(f"неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
