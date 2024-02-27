#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with (open("text.txt", "r", encoding="utf-8") as file):
        all_text = file.read()
        all_text = all_text.lower()
        words = all_text.split()

        # Создадим словарь со всеми буквами алфавита.
        dictionary_letters = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
            }

        # Посчитаем количество слов для каждой буквы.
        for word in words:
            for letter in word:
                if letter in dictionary_letters:
                    dictionary_letters[letter] += 1

        # Получим информацию о букве, которая встретилась в наименьшем количестве слов.
        min_letter = 'a'
        for i in dictionary_letters:
            if dictionary_letters[i] <= dictionary_letters[min_letter]:
                min_letter = i

        # Выведем полученную информацию.
        len_text = len(words)
        for i in dictionary_letters:
            print("Буква", i, "встретилась в тексте в",
                  f"{(dictionary_letters[i] / len_text) * 100:.{3}f}", "% слов.")

        print("Буква, которая встретилась в тексте меньше всего:", min_letter)
