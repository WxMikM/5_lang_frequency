import sys
import os
import re


def get_file_path():
    return sys.argv[1] if len(sys.argv) > 1 else input('Введите путь к файлу .txt : ')


def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(source_text):
    all_words = {}
    word_regex = re.compile(r'\w+')
    for elem in word_regex.findall(source_text):
        all_words[elem.lower()] = all_words.get(elem.lower(), 0) + 1
    all_words = sorted(all_words.items(), key=lambda x: x[1], reverse=True)
    return [('{}'.format(key)) for key, value in all_words[:10]]


if __name__ == '__main__':
    data = load_data(get_file_path())
    if data is None:
        print('Нельзя загрузить файл')
        sys.exit()
    print(' '.join(get_most_frequent_words(data)))
    
