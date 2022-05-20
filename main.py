import nltk
import random


def write_lines(contents, file):
    with open(file, 'w') as writer:
        writer.writelines(contents)


def generate_names(char, num):
    char = char.upper()
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("Value of char is not a character.")

    # nltk.download('names')

    male_tag = "male"
    female_tag = "female"

    name_list = \
        [(it, male_tag) for it in nltk.corpus.names.words('male.txt') if it[0] == char] + \
        [(it, female_tag) for it in nltk.corpus.names.words('female.txt') if it[0] == char]

    if len(name_list) < num:
        print(f"Less than {num} names found for character {char}.")

        if not name_list:
            print("In fact, not a single name found.")

        return

    name_sample = random.sample(name_list, num)

    print(name_sample)

    write_lines([name + '\n' for (name, gender) in name_sample if gender == male_tag], "male_names.txt")
    write_lines([name + '\n' for (name, gender) in name_sample if gender == female_tag], "female_names.txt")


class SynAnt:

    def __init__(self, list_of_words):

        # Check for invalid inputs.
        if not (list_of_words and isinstance(list_of_words, list) and all(
                isinstance(elem, str) for elem in list_of_words)):
            raise ValueError("The provided input is not an non-empty list of strings.")

        self.words = list_of_words

        # Need these for find_synonyms and find_antonyms, so we download them once here.
        # nltk.download('wordnet')
        # nltk.download('omw-1.4')

    def find_synonyms(self):
        for word in self.words:
            print(f"Synonyms for {word}: ", end="")

            # set to prevent duplicates.
            synonyms = set()

            # Look at all synsets of the current word.
            for syn in nltk.corpus.wordnet.synsets(word):
                # Go through each lemma (i.e. word) in the synset.
                for i in syn.lemmas():
                    # Add it as synonym.
                    synonyms.add(i.name())

            if synonyms:
                print(synonyms)
            else:
                print("None found.")

    def find_antonyms(self):
        for word in self.words:
            print(f"Antonyms for {word}: ", end="")

            # set to prevent duplicates.
            antonyms = set()

            # Look at all synsets of the current word.
            for syn in nltk.corpus.wordnet.synsets(word):
                # Go through each lemma (i.e. word) in the synset.
                for i in syn.lemmas():
                    # Go through all its antonyms.
                    for j in i.antonyms():
                        # Add it as antonym.
                        antonyms.add(j.name())

            if antonyms:
                print(antonyms)
            else:
                print("None found.")
