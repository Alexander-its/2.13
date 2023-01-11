#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-

def add():
    # Запросить данные .
    name = input("Фамилия, Имя ")
    tel = input("Номер телефона ")
    date = input("Дата рождения ")

    return {
        "name": name,
        "tel": tel,
        "date": date,
        }