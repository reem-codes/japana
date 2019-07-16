from jamdict import Jamdict, config
jmd = Jamdict(db_file=config.get_file('JAMDICT_DB'))


def lookup_dic(word, igonre=True):
    word_dic = dict()
    result = jmd.lookup(word, strict_lookup=True, lookup_chars=False)
    result = result.to_json()['entries']
    for entry in result:
        if entry['kanji'][0]['text'] == word:
            word_dic['word'] = entry['kanji'][0]['text']
            word_dic['pronunciation'] = ""
            for k, p in enumerate(entry['kana'], start=1):
                if len(entry['kana']) == 1:
                    word_dic['pronunciation'] += p['text']
                else:
                    word_dic['pronunciation'] += str(k) + ". " + p['text'] + "<br>"
            word_dic['meaning'] = ""
            for j, meaning in enumerate(entry['senses'], start=1):
                if j >= 3:
                    break
                if len(entry['senses']) > 1:
                    word_dic['meaning'] += str(j) + ". "
                for i, one_sense in enumerate(meaning['SenseGloss'], start=1):
                    if i >= 5:
                        break
                    word_dic['meaning'] += one_sense['text']
                    if i != len(meaning['SenseGloss']) and i != 4:
                        word_dic['meaning'] += "; "
                if j != len(entry['senses']) and j != 2:
                    word_dic['meaning'] += "<br>"
            return word_dic
    if not igonre:
        return {"word": word}
    return None

