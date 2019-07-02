from jamdict import Jamdict
jmd = Jamdict()


def lookup_dic(word):
    word_dic = dict()
    result = jmd.lookup(word)
    result = result.to_json()['entries']
    for entry in result:
        if entry['kanji'][0]['text'] == word:
            word_dic['word'] = entry['kanji'][0]['text']
            word_dic['pronunciation'] = entry['kana'][0]['text']
            word_dic['meaning'] = ""
            for j, meaning in enumerate(entry['senses'], start=1):
                if j >= 3:
                    break
                word_dic['meaning'] += str(j) + ". "
                for i, one_sense in enumerate(meaning['SenseGloss'], start=1):
                    if i >= 5:
                        break
                    word_dic['meaning'] += one_sense['text']
                    if i != len(meaning['SenseGloss']) and i != 5:
                        word_dic['meaning'] += "; "
                if j != len(entry['senses']) and j != 3:
                    word_dic['meaning'] += "<br>"
            return word_dic
    return {"word": word}

