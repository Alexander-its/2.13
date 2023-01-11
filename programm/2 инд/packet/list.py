#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-

def list(spisok):
    if spisok:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 13)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^13} |".format(
                "No","Фамилия, Имя","Номер телефона","Дата рождения",
        )
    )
    print(line)
    for idx, sp in enumerate(spisok, 1):
        print(
            "| {:>4} | {:<30} | {:<20} | {:^13} |".format(
                idx,
                sp.get("name", ""),
                sp.get("tel", ""),
                sp.get("date", ""),
                " " * 5,
            )
        )
    print(line)