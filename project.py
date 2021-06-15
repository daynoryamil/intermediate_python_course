import random
import os

def read_data(filepath="./files/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as data:
        for line in data:
            words.append(line.strip().upper())
    return words

def run():
    data = read_data(filepath="./files/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dic = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dic.get(letter):
            letter_index_dic[letter] = []
        letter_index_dic[letter].append(idx)

    while True:
        os.system("clear")
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dic[letter]:
                chosen_word_list_underscores[idx] = letter

        if "_" not in chosen_word_list_underscores:
            os.system("clear")
            print("¡Ganaste!, la palabra es", chosen_word)
            break


if __name__ == "__main__":
    run()