class ConllEntry:
    def __init__(self, id, form, lemma, pos, cpos, feats=None, \
                 parent_id=None, relation=None,deps=None, misc=None):
        self.id = id
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.cpos = cpos
        self.feats = feats
        self.parent_id = parent_id
        self.relation = relation
        self.deps = deps
        self.misc = misc
        

        
class Sentence:
    def __init__(self):
        self.text = ""
        self.sent_id = ""
        self.words = []
        self.is_complex = False

    def add_word(self, word):
        self.words.append(word)

    def set_sent_id(self, sent_id):
        self.sent_id = sent_id

    def set_text(self, text):
        self.text = text

    def is_not_empty(self):
        return len(self.words) > 0

    def set_complex(self):
        self.is_complex = True

    def is_complex(self):
        return self.is_complex
        
        
        
fh = open("ru_syntagrus-ud-test.conllu",'r',encoding='utf-8')
sents_read = 0
sents = []
complex_sents = []
comments = set()

sent = Sentence()
for line in fh:
    tok = line.strip().split('\t')
    if not tok or line.strip() == '': # empty line, add sentence to list
        if sent.is_not_empty:
            sents_read += 1
            if sent.is_complex:
                complex_sents.append(sent)
            else:
                sents.append(sent)
        sent = Sentence()
    else:
        if line[0] == '#' or '-' in tok[0]: # a comment line
            line = line.strip()
            if line[:12] == "# sent_id = ":
                sent.set_sent_id(line[12:])
            elif line[:9] == "# text = ":
                sent.set_text(line[9:])
            else:
                comments.add(line)

        else: # an actual ConllEntry, add to tokens
            if tok[2] == "_":
                tok[2] = tok[1].lower()

            word = ConllEntry(*tok)
            sent.add_word(word)
            if "." in tok[0]:
                sent.set_complex()
fh.close()

