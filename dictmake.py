import pymorphy2
from readstr import sents, complex_sents


def check_stand_pos(py_parses, word_str_pos, str_pos, py_pos_list, smlr_parse):
  if word_str_pos == str_pos:
    for parse in py_parses:
      if parse.tag.POS in py_pos_list:
        smlr_parse.append(parse)
  return


def check_not_stand_pos(py_parses, word_str_pos, str_pos, py_ns_pos_list, smlr_parse):
  if word_str_pos == str_pos:
    for parse in py_parses:
      for pos in py_ns_pos_list:
        if pos in parse.tag:
          smlr_parse.append(parse)
  return


def check_pos(word):
  py_parse = morph.parse(word.form)
  smlr_parse = []
  check_stand_pos(py_parse, word.pos, "ADJ", ["ADJF", "ADJS", "COMP"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "ADP", ["PREP"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "ADV", ["ADVB"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "AUX", ["VERB"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "CCONJ", ["CONJ"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "DET", ["NPRO"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "INTJ", ["INTJ"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "NOUN", ["NOUN"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "NUM", ["NUMR"], smlr_parse)
  check_not_stand_pos(py_parse, word.pos, "NUM", ["NUMB"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "PART", ["PRCL"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "PRON", ["NPRO"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "PROPN", ["NOUN"], smlr_parse)
  check_not_stand_pos(py_parse, word.pos, "PUNCT", ["PNCT"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "SCONJ", ["CONJ"], smlr_parse)
  check_not_stand_pos(py_parse, word.pos, "SYM", ["PNCT", "UNKN"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "VERB", ["VERB", "INFN", "PRTF", "PRTS", "GRND"], smlr_parse)
  check_stand_pos(py_parse, word.pos, "X", ["NOUN"], smlr_parse)
  check_not_stand_pos(py_parse, word.pos, "x", ["LATN", "UNKN", "ROMN"], smlr_parse)
  return smlr_parse


def check_anim(py_anim, str_anim):
  if (((py_anim == 'anim') and (str_anim == 'Anim')) or
      ((py_anim == 'inan') and (str_anim == 'Inan'))):
    return True
  else:
    return False


def check_asp(py_asp, str_asp):
  if (((py_asp == 'perf') and (str_asp == 'Perf')) or
      ((py_asp == 'impf') and (str_asp == 'Imp'))):
    return True
  else:
    return False


def check_case(py_case, str_case):
  if (((py_case == 'nomn') and (str_case == 'Nom')) or
      ((py_case == 'gent') and (str_case == 'Gen')) or
      ((py_case == 'datv') and (str_case == 'Dat')) or
      ((py_case == 'accs') and (str_case == 'Acc')) or
      ((py_case == 'ablt') and (str_case == 'Ins')) or
      ((py_case == 'loct') and (str_case == 'Loc')) or
      ((py_case == 'voct') and (str_case == 'Voc'))):
    return True
  elif ((str_case == "Par") or
        (py_case == "gen1") or
        (py_case == "gen2") or
        (py_case == "acc2") or
        (py_case == "loc1") or
        (py_case == "loc2")):
    return
  else:
    return False


def check_gend(py_gend, str_gend, parse):
  if (((py_gend == 'masc') and (str_gend == 'Masc')) or
           ((py_gend == 'femn') and (str_gend == 'Fem')) or
           ((py_gend == 'neut') and (str_gend == 'Neut'))):
    return True
  elif "ms-f" in parse:
    return
  else:
    return False


def check_mood(py_mood, str_mood):
  if (((py_mood == 'indc') and (str_mood == 'Ind')) or
      ((py_mood == 'impr') and (str_mood == 'Imp'))):
    return True
  elif str_mood == "Cnd":
    return
  else:
    return False


def check_numb(py_numb, str_numb):
  if (((py_numb == 'sing') and (str_numb == 'Sing')) or
      ((py_numb == 'plur') and (str_numb == 'Plur'))):
    return True
  else:
    return False


def check_per(py_pers, str_pers):
  if (((py_pers == '1per') and (str_pers == '1')) or
      ((py_pers == '2per') and (str_pers == '2')) or
      ((py_pers == '3per') and (str_pers == '3'))):
    return True
  else:
    return False


def check_tens(py_tens, str_tens):
  if (((py_tens == 'pres') and (str_tens == 'Pres')) or
      ((py_tens == 'past') and (str_tens == 'Past')) or
      ((py_tens == 'futr') and (str_tens == 'Fut'))):
    return True
  else:
    return False


def check_voic(py_voic, str_voic):
  if (((py_voic == 'actv') and (str_voic == 'Act')) or
      ((py_voic == 'pssv') and (str_voic == 'Pass'))):
    return True
  elif str_voic == "Mid":
    return
  else:
    return False


def check_properties(parse, feats, values):
  properties = []
  if 'Animacy' in feats:
    py_anim = parse.tag.animacy
    str_anim = values[feats.index('Animacy')]
    properties.append(check_anim(py_anim, str_anim))
  if 'Aspect' in feats:
    py_asp = parse.tag.aspect
    str_asp = values[feats.index('Aspect')]
    properties.append(check_asp(py_asp, str_asp))
  if 'Case' in feats:
    py_case = parse.tag.case
    str_case = values[feats.index('Case')]
    properties.append(check_case(py_case, str_case))
  if 'Gender' in feats:
    py_gend = parse.tag.gender
    str_gend = values[feats.index('Gender')]
    properties.append(check_gend(py_gend, str_gend, parse.tag))
  if 'Mood' in feats:
    py_mood = parse.tag.mood
    str_mood = values[feats.index('Mood')]
    properties.append(check_mood(py_mood, str_mood))
  if 'Number' in feats:
    py_numb = parse.tag.number
    str_numb = values[feats.index('Number')]
    properties.append(check_numb(py_numb, str_numb))
  if 'Person' in feats:
    py_per = parse.tag.person
    str_per = values[feats.index('Person')]
    properties.append(check_per(py_per, str_per))
  if 'Tense' in feats:
    py_tens = parse.tag.tense
    str_tens = values[feats.index('Tense')]
    properties.append(check_tens(py_tens, str_tens))
  if 'Voice' in feats:
    py_voic = parse.tag.voice
    str_voic = values[feats.index('Voice')]
    properties.append(check_voic(py_voic, str_voic))
  return all(properties)
  


def word_occured(occur_dict, sent_id, word):
  cort_key = (word.form, word.feats)
  if cort_key not in occur_dict:
    occur_dict[cort_key] = [(sent_id, word.id)]
  else:
    occur_dict[cort_key] += [(sent_id, word.id)]
    
    
def add_suited_parse(suited_parses, cort_key, is_properties_same, parse):
  if cort_key not in suited_parses:
    suited_parses[cort_key] = []
  if is_properties_same and (parse not in suited_parses[cort_key]):
    suited_parses[cort_key] += [parse]


def check_word(suited_parses, word):
  cort_key = (word.form, word.feats)
  parses_with_suited_pos = check_pos(word)
  feats = []
  values = []
  if word.feats != '_':
    feats = [i.split('=')[0] for i in word.feats.split('|')]
    values = [i.split('=')[1] for i in word.feats.split('|')]
  for parse in parses_with_suited_pos:
    is_properties_same = check_properties(parse, feats, values)
    add_suited_parse(suited_parses, cort_key, is_properties_same, parse)



morph = pymorphy2.MorphAnalyzer()

occur_dict = dict()

for n_sent in range(len(sents)):
  for word in sents[n_sent].words:
    word_occured(occur_dict, sents[n_sent].sent_id, word)

for n_sent in range(len(complex_sents)):
  for word in complex_sents[n_sent].words:
    word_occured(occur_dict, complex_sents[n_sent].sent_id, word)

suited_parses = dict()

for n_sent in range(len(sents)):
  for word in sents[n_sent].words:
    check_word(suited_parses, word)

for n_sent in range(len(complex_sents)):
  for word in complex_sents[n_sent].words:
    check_word(suited_parses, word)
