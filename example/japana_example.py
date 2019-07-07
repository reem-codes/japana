from japana.word_count import word_count


text = "私は貴方の事を好き好き大好き私の恋人。成程。身体"
kana = True
_dict = True
asc = False


words = word_count(text, kana, asc, _dict)

for word in words:
    print(word)


'''
# OUTPUT:
total word count:  15
unique word count:  12
 |██████████████████████████████████████████████████| 100.0% words has been done
{'word': '私', 'pronunciation': '1. わたし<br>2. わたくし<br>', 'meaning': '1. I; me<br>2. private affairs; personal matter; secrecy', 'frequency': 2}
{'word': 'の', 'frequency': 2}
{'word': '好き', 'pronunciation': '1. すき<br>', 'meaning': '1. liking; fondness; love', 'frequency': 2}
{'word': 'は', 'frequency': 1}
{'word': '貴方', 'pronunciation': '1. きほう<br>', 'meaning': "1. your home; your residence<br>2. you (referring to one's equal; epistolary style)", 'frequency': 1}
{'word': '事', 'pronunciation': '1. こと<br>2. こん<br>', 'meaning': '1. thing; matter<br>2. incident; occurrence; event; something serious', 'frequency': 1}
{'word': 'を', 'frequency': 1}
{'word': '大好き', 'pronunciation': '1. だいすき<br>', 'meaning': '1. loveable; very likeable; like very much', 'frequency': 1}
{'word': '恋人', 'pronunciation': '1. こいびと<br>', 'meaning': '1. lover; sweetheart', 'frequency': 1}
{'word': '成', 'frequency': 1}
{'word': '程', 'pronunciation': '1. ほど<br>', 'meaning': '1. degree; extent; bounds; limit<br>2. indicates approx. amount or maximum; upper limit', 'frequency': 1}
{'word': '身体', 'pronunciation': '1. しんたい<br>2. しんだい<br>3. しんてい<br>', 'meaning': '1. body; physical system; person', 'frequency': 1}
'''
