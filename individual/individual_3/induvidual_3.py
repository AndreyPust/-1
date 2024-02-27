#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":
    directory = input("Введите полный путь каталога, содержимое которго необходимо просмотреть: ")
    all_files = os.walk(directory)  # проход по всем файлам и подкаталогам

    for catalog in all_files:
        print("Папка", catalog[0], "содержит:")
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)
