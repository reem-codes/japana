from janome.tokenizer import Tokenizer
import re
from japana.dictionary import lookup_dic


def word_count(text, kana=False, asc=True, _dict=False):
    t = Tokenizer()
    tokens = t.tokenize(text)
    print("total word count: ", len(tokens))
    kanji = r'[ぁ-ゟ]*[㐀-䶵一-鿋豈-頻][ぁ-ゟ]*'
    letters = r'[ぁ-んァ-ン一-龯]|[㐀-䶵一-鿋豈-頻]'

    words = dict()
    for token in tokens:
        word = dict()
        if words.get(token.base_form) is None and re.match(letters if kana else kanji, token.base_form):
            word["word"] = token.base_form
            word["frequency"] = 1
            words[token.base_form] = word
        elif words.get(token.base_form):
            words[token.base_form]["frequency"] += 1

    print("unique word count: ", len(words))
    words = [v for v in words.values()]
    words = sorted(words, key=lambda k: k['frequency'], reverse=not asc)
    word_list = list()
    for value in words:
        word_dic = dict()
        if _dict:
            try:
                word_dic = lookup_dic(value["word"])
            except:
                pass
        word_dic['word'] = value["word"]
        word_dic['frequency'] = value["frequency"]
        word_list.append(word_dic)
    return word_list

