# coding=utf8
import json

class_file = open('lookup_lists/word_classes.json', 'rt', encoding='utf-8')
class_dict = json.load(class_file)
class_file.close()


def word_classifier(word):
    return class_dict.get(word)
