#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-

def select(spisok, nom):
    count = 0
    for idx , sp in enumerate(spisok, 1):
        if sp['name'] == str(nom):
            print(
                "Фамилия, Имя: ",
                sp["name"],
                "\nНомер телефона: ",
                sp["tel"],
                "\nДата рождения:",
                sp["date"],
            )
            count += 1

    # Если счетчик равен 0, то рейсы не найдены.
    if count == 0:
        print("Люди не найден.")