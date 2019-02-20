import itertools
def analyse_term(term):
    ans = []
    if not term:
        return ans
    for symbol in '!"@#$%&\'()=~-^\\|`{}[]:*;+<>,./?\_':
        if symbol in term:
            for t in term.split(symbol):
                ans.append(t)
                ans += analyse_term(t)
    return ans

def read_dictionaly(dictionaly_file):
    f = open(dictionaly_file)
    words = set(map(lambda x: x.replace('\n','').replace('\r',''), f.readlines()))
    f.close()
    return words

def create_direct_word(dictionaly):
    for term in dictionaly:
        yield term

def create_indirect_word(dictionaly,string,additional_num):
    for term in dictionaly:
        for s in itertools.combinations_with_replacement(string,additional_num):
            s = ''.join(s)
            yield s+term
            yield term+s

def dictionaly_attack(user_id, string, dictionaly_file, max_additional_num, answer):
    dictionaly = set(analyse_term(user_id))
    print dictionaly
    dictionaly |= set(read_dictionaly(dictionaly_file))
    print dictionaly
    for term in create_direct_word(dictionaly):
        #print term
        if term == answer:
            return term
    for i in range(1,max_additional_num+1):
        for term in create_indirect_word(dictionaly,string,i):
            #print term
            if term == answer:
                return term
    return False
