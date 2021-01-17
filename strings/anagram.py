from collections import defaultdict


def anagrams(sentence):  # S is a set of strings
    d = defaultdict(list)  # maps s to list of words with signature s
    for word in sentence.split():  # group words according to the signature
        s = ''.join(sorted(word))  # calculate the signature
        d[s].append(word)

    return [d[s] for s in d if len(d[s]) > 1]


if __name__ == '__main__':
    result = anagrams(
        'below the c ar is a rat drinking cider and bending its elbow while this thing is an arc that can act like a '
        'cat which cried during the night caused by pain in its bowel')
    print(result)
