print("Type in a sentence:")
inp = input(">")
inp = "\n".join(inp)
inp = inp.lower()
inp = inp.split
list = []
punctList = [".","?","!",",",'"',":",";","-"]
pronouns = ["I", "me", "we", "us", "you", "she", "her", "he", "him", "it", "they", "them"]
counter = dict()
print(inp)
for word in inp:
    if word in pronouns:
        counter[word] = counter.get(word, 0) + 1
        continue
    char = word[0]
    if char in punctList:
        counter[char] = counter.get(char, 0) + 1
        continue
    if char not in list:
        list.append(word[0])
        continue
    if char in list:
        counter[char] = counter.get(char, 1) + 1
    continue
for item, number in counter.items():
    print("There are", number, item + "'s")
print(counter)

