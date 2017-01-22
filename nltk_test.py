import nltk



def isRhyme(w1, w2):
    if w1.find(w2) == len(w1) - len(w2):
        return False
    if w2.find(w1) == len(w2) - len(w1):
        return False

    return w1 in rhyme(w2, 1)


def rhyme(i, l):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == i]
    rhymes = []
    for (word, syllable) in syllables:
        rhymes += [word for word, pron in entries if pron[-l:] == syllable[-l:]]
    return set(rhymes)


print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))
print(isRhyme("bad", "mad"))