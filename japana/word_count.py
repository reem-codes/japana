from janome.tokenizer import Tokenizer
import re
from japana.dictionary import lookup_dic
from japana.kanji_count import extract_unicode_block
from japana.progress_bar import printProgressBar
from japana.word_classifier import word_classifier


def word_count(text, kana=False, asc=True, _dict=False, ignore=True, celery=None):
    kanji = r'[ぁ-ゟ]*[㐀-䶵一-鿋豈-頻][ぁ-ゟ]*'
    letters = r'[ぁ-んァ-ン一-龯]|[㐀-䶵一-鿋豈-頻]\s'
    t = Tokenizer()
    tokens = t.tokenize(''.join(extract_unicode_block(letters, text)))
    print("total word count: ", len(tokens))

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
    for index, value in enumerate(words, start=1):
        word_dic = dict()
        if celery:
            meta = {'current': index, 'total': len(words)}
            celery.update_state(state='PROGRESS', meta=meta)
        printProgressBar(index, len(words), suffix='words has been done', length=50)
        if _dict:
            try:
                word_dic = lookup_dic(value["word"], ignore)
                if word_dic is None:
                    pass
                word_dic['frequency'] = value["frequency"]
                word_dic['jlpt'] = word_classifier(word_dic['word'])
                word_list.append(word_dic)

            except:
                pass
        else:
            word_dic['word'] = value["word"]
            word_dic['jlpt'] = word_classifier(word_dic['word'])
            word_dic['frequency'] = value["frequency"]
            word_list.append(word_dic)
    return word_list


