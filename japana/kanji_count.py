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
    # print(len(kanji_list), kanji_list)
    print("unique kanji count: ", len(kanji_list))
    return kanji_list
#
#
# word = list_kanji("word.csv")
# jlpt = list_kanji("jlpt.csv")
# n3 = list_kanji("jlpt3.csv")
# done = list_kanji("exportcsv.csv")
# kanji_list = word + jlpt + done + n3
# kanji_list = remove_duplicate(kanji_list)
# print(len(kanji_list), kanji_list)
#
# print("kanji left in kanjidamage: ")
#
# f = open("kanjidamage.csv", "r")
# kd = f.read()
# f.close()
# new_kanji = list(set(kd)^set(kanji_list))
# new_kanji = ''.join(new_kanji)
# print(len(new_kanji), new_kanji)
# new_kanji = ''.join(extract_unicode_block(kanji, new_kanji))
# print(len(new_kanji), new_kanji)
#
# old = open("KanjiDamage Reordered.txt", "r")
# new_file = open("new_kanjiDamage.txt", "a")
# new_file.truncate(0)
# for line in old:
#     word = line.split("\t", 2)[1]
#     if word in new_kanji and re.match(kanji, word):
#         new_file.write(line)
# new_file.close()
# old.close()
#

#
# new = ''
# doc = open("new_kanjiDamage.txt", 'r')
# for line in doc:
#     new = new + line.split("\t", 2)[1]
#
# print(len(new), new)
#
# now = list_kanji("now.csv")
# exclude = list(set(new)^set(now))
# exclude = ''.join(exclude)
# print(len(exclude), exclude)