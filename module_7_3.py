import io
from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding= 'utf-8') as file:
                words = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(j,'')
                all_words[i] = words.split()
        return all_words

    def find(self,word):
        find_word = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_word[key] = value.index(word.lower()) + 1
        return find_word

    def count(self, word):
        count_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            count_[value] = words_count
        return count_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

print()

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))

print()

finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))

print()

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))



