import os.path
import nltk
#requires importing txt of negative and positive words

punctList = [".","?","!",",",'"',":",";"]
pronouns = ["I", "me", "we", "us", "you", "she", "her", "he", "him", "it", "they", "them"]
abc = ['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
text = list()
repeatWords = list()
minidict =list()


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


def formatWord(word):
    for punct in punctList:
        word = word.replace(punct, "")
    word = word.lower()
    return word


def setDictionary(fileName):
    del minidict[:]
    if os.path.isfile(fileName + ".txt"):
        openFile = open(fileName + ".txt")
        stringFile = openFile.read()
        splitList = stringFile.split()
        for item in splitList:
            minidict.append(formatWord(item))
        return True
    else:
        return False


def scanRepeat(fileName):
    if os.path.isfile(fileName + ".txt"):
        openFile = open(fileName + ".txt")
        stringFile = openFile.read()
        splitList = stringFile.split()
        for item in splitList:
            if "--" in item:
                item = item.replace("--"," ")
                miniList = item.split()
                item1 = miniList[0]
                item1 = formatWord(item1)
                if item1 in text and item1 not in repeatWords:
                    repeatWords.append(item1)
                text.append(item1)
                if (len(miniList) > 1):
                    item2 = miniList[1]
                    item2 = formatWord(item2)
                    if item2 in text and item2 not in repeatWords:
                        repeatWords.append(item2)
                    text.append(item2)
            else:
                item = formatWord(item)
                if item in text and item not in repeatWords:
                    repeatWords.append(item)
                text.append(item)
        if repeatWords != []:
            print("These are the repeated words: " + ", ".join(repeatWords))
            setDictionary("negative")
            count = 0
            for word in repeatWords:
                if word in minidict:
                    count += 1
            if count * 10 / len(repeatWords) >= 1:
                print("The use of repeated negative words indicates a negative connotation.")
            setDictionary("positive")
            count = 0
            for word in repeatWords:
                if word in minidict:
                    count += 1
            if count * 10 / len(repeatWords) >= 1:
                print("The use of repeated positive words indicates a positive connotation.")
        print()
        return True
    else:
        return False


def alliteration(fileName):
    counter = dict()
    numArray = []
    char = ''
    allChar = []
    list = []
    lastWordList = []
    del text[:]
    if os.path.isfile(fileName + ".txt"):
        openFile = open(fileName + ".txt")
        stringFile = openFile.read()
        lineList = stringFile.split("\n")
        rhymeScheme = [None]*len(lineList)
        for line in lineList:
            splitList = line.split()
            for item in splitList:
                if "--" in item:
                    item = item.replace("--", " ")
                    miniList = item.split()
                    item1 = miniList[0]
                    item1 = formatWord(item1)
                    text.append(item1)
                    if (len(miniList) > 1):
                        item2 = miniList[1]
                        item2 = formatWord(item2)
                        text.append(item2)
                else:
                    item = formatWord(item)
                    text.append(item)
            idx1 = 0
            for item in text:
                if idx1 == len(text)-1:
                    lastWordList.append(item)
                char = item[0]
                list.append(char)
                idx1 += 1
            for letter in list:
                item = list.count(letter)
                numArray.append(item)
            idx2 = 0
            for item in numArray:
                if item*100/len(numArray) >= 35:
                    char = list[idx2]
                    if char not in allChar:
                        allChar.append(char)
                idx2 += 1
            if allChar != []:
                for item in allChar:
                    print(item + "'s in line ", lineList.index(line)+1, ".")
            del list[:]
            del numArray[:]
            del allChar[:]
            del text[:]
        print("\nLoading...")

        idx3 = 0
        for lastWord in lastWordList:
            idx4 = 0
            popped = False
            for item in lastWordList:
                if isRhyme(item,lastWordList[idx3]) and idx3 != idx4 and rhymeScheme[idx3] == None:
                    if rhymeScheme[idx4] != None:
                        rhymeScheme[idx3] = rhymeScheme[idx4]
                    else:
                        pop = abc.pop()
                        popped = True
                        rhymeScheme[idx3] = pop
                        rhymeScheme[idx4] = pop
                idx4 += 1
            if popped == False and rhymeScheme[idx3] == None:
                pop = abc.pop()
                rhymeScheme[idx3] = pop
            print(rhymeScheme)
            idx3 += 1
        print("Done!")
        for item in rhymeScheme:
            if item == None:
                rhymeScheme.pop()
        rhymeScheme.pop()
        print("\nRhyme Pattern: ", rhymeScheme, "\n")
        return True
    else:
        return False


while True:
    fileName = input("Please enter the name of the file to be analyzed, or press ENTER to exit: ")
    print()
    if fileName.strip() == "":
        break
    scanRepeat(fileName)
    print("Alliteration:")
    alliteration(fileName)