#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with (open("text.txt", "r", encoding="utf-8") as file):
        all_text = file.read()
        words = all_text.split()
        count_words = 0  # счетчик для слов из 7-ми и более букв

        for word in words:
            count_letter = 0  # счетчик для букв в слове

            # Посчитаем количество букв в каждом слове без учета прочих символов.
            for letter in word:
                if (letter != "," and letter != "." and letter != ";" and letter != ":"
                        and letter != "-" and letter != "!" and letter != "?"
                        and letter != "(" and letter != ")"):
                    count_letter += 1

            if count_letter >= 7:
                count_words += 1

    print("Количество слов из не менее чем семи букв в тексте: ", count_words)
