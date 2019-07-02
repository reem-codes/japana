
from word_count import word_count


text = "私は貴方の事を好き好き大好き私の恋人。成程。身体"
kana = True
_dict = True
asc = False


words = word_count(text, kana, asc, _dict)

for word in words:
    print(word)
