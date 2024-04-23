#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":

    # Необходимо пройтись по всем каталогам заданного каталога и вывести все
    # содержимое всех каталогов и подкаталогов. Функция walk() модуля «os»
    # позволяет проходиться по всем каталогам определенной директории.

    directory = input("Введите полный путь каталога, содержимое которго необходимо просмотреть: ")
    all_files = os.walk(directory)  # проход по всем файлам и подкаталогам

    for catalog in all_files:
        print("Папка", catalog[0], "содержит:")
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)
