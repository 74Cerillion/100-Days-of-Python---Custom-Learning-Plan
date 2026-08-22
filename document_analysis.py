import sys
from pathlib import Path
import json

def main():
    print(r"""
 __        __  _____   _        ____    ___    __  __   _____
 \ \      / / | ____| | |      / ___|  / _ \  |  \/  | | ____|
  \ \ /\ / /  |  _|   | |     | |     | | | | | |\/| | |  _|
   \ V  V /   | |___  | |___  | |___  | |_| | | |  | | | |___
    \_/\_/    |_____| |_____|  \____|  \___/  |_|  |_| |_____|
    """)
    document_to_analyze = input("\nEnter " \
    "the text document you would like analyzed: ")

    while True:
        p = Path(document_to_analyze)
        if p.exists():
            break
        else:
            document_to_analyze = input("Invalid input. Please " \
            "enter a valid filepath, or press 'q' to quit: ")
            if document_to_analyze == 'q':
                sys.exit()

    with open('100 Days of Python/Day 5/config.json', 'r') as cf:
        settings = json.load(cf)

        sentence_count = settings.get("sentence_count")
        word_count = settings.get("word_count")
        special_characters = settings.get("special_characters")
        top_x_list = settings.get("top_x_list")
        read_mode = settings.get("case_sensitivity")

    unique_words = {}

    with open(document_to_analyze, encoding='UTF-8', 
              errors='ignore') as f:
        if read_mode == True:
            file = f.read()
            file = file.split()
        if read_mode == False:
            file = f.read().lower()
            file = file.split()

    for word in file:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            sentence_count += 1
        cleaned_word = "".join(
            char for char in word if char not in special_characters
            )
        word_count += 1
        if cleaned_word in unique_words:
            unique_words[cleaned_word] += 1
        elif cleaned_word not in unique_words and cleaned_word != "":
            unique_words[cleaned_word] = 1

    print("\nDocument Parsed Successfully!------------")
    print("\nFile: {}".format(document_to_analyze))
    print("\nTotal Words: {}".format(word_count))
    print("\nTotal Sentences: {}".format(sentence_count))
    print("\nUnique Words: {}".format(len(unique_words)))
    print("\nVocabulary Richness: {}".format(
        round(len(unique_words) / word_count, 2)
    ))
    print("\n-------------------------------------------------")
    print("\nAverage Word Length: {}".format(
        calc_avg_word_len(unique_words, word_count)
    ))
    print("\nAverage Sentence Length: {}".format(
        round(word_count / sentence_count, 2)
    ))
    print("\n-------------------------------------------------")
    print("\nThe top 10 most used words are:\n")
    top_10 = sorted(unique_words.items(), key=lambda item: item[1], 
                    reverse=True)[:top_x_list]
    for k, v in top_10:
        print("\n{}: {}".format(k, v))

def calc_avg_word_len(unique_words, word_count):
    char = 0
    for k, v in unique_words.items():
        char += len(k) * v
    avg_word_len = char / word_count
    return round(avg_word_len, 2)

if __name__ == '__main__':
    main()