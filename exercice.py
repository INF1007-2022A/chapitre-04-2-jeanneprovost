#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
    first_part = name[0].capitalize() + name[1:name.find('-')].lower()
    return 'Bonjour ' + first_part


def get_random_sentence(animals, adjectives, fruits):
    animal = animals[random.randint(0, len(animals) - 1)]
    adjective = adjectives[random.randint(0, len(adjectives) - 1)]
    fruit = fruits[random.randint(0, len(fruits) - 1)]
    return f"Aujourd'hui, j'ai vu un {animal} s'emparer d'un panier {adjective} plein de {fruit}."


def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter.isalpha():
            if ord(letter) <= 90-shift or 97 <= ord(letter) <= 122-shift:
                encrypted_text += chr(ord(letter)+shift)
            elif ord(letter) <= 90:
                encrypted_text += chr(90-ord(letter)+65+shift)
            else:
                encrypted_text += chr(122 - ord(letter) + 97 + shift)
        else:
            encrypted_text += letter
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
    parrot = "jEaN-MARC"
    print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "mangue")
    print(get_random_sentence(animals, adjectives, fruits))

    print(encrypt("ABC", 1))
    print(encrypt("abc 123 XYZ", 3))
    print(decrypt("DEF 123 ABC", 3))
