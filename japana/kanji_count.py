import re
from collections import OrderedDict

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'
kanji = r'[㐀-䶵一-鿋豈-頻]'
radicals = r'[⺀-⿕]'
katakana_half_width = r'[｟-ﾟ]'
alphanum_full = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'


def extract_unicode_block(unicode_block, string):
    ''' extracts and returns all texts from a unicode block from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.findall( unicode_block, string)


def remove_unicode_block(unicode_block, string):
    ''' removes all chaacters from a unicode block and returns all remaining texts from string argument.
        Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.sub(unicode_block, '', string)


def remove_duplicate(str1):
    return "".join(OrderedDict.fromkeys(str1))


def list_kanji(str):
    f = open(str, "r")
    vocab = f.read()
    f.close()
    vocab = ''.join(extract_unicode_block(kanji, vocab))
    kanji_list = remove_duplicate(vocab)
    print("unique kanji count: ", len(kanji_list))
    return kanji_list
