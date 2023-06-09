#!/usr/bin/env python3

PLACEHOLDER = "[name]"


with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()



with open("./input/letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./output/Readtosend/letter_for_{stripped_name}.txt,", mode="w") as completed_letter:
            completed_letter.write(new_letter)
