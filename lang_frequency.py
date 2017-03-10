import sys
import os
import re
from collections import Counter


def get_file_path():
    return sys.argv[1] if len(sys.argv) > 1 else input('Введите путь к файлу .txt : ')


def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(source_text):
    required_number_of_words = 10
    word_regex = re.compile(r'\w+')
    all_words = Counter(word_regex.findall(source_text.lower()))
    return [word for word, amount in all_words.most_common(required_number_of_words)]


if __name__ == '__main__':
    list_words = load_data(get_file_path())
    if list_words is None:
        print('Нельзя загрузить файл')
        sys.exit()
    print('Самые частые слова в тексте: ')
    print(' '.join(get_most_frequent_words(list_words)))
