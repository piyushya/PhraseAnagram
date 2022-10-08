from collections import Counter
import sys

file = "data/words.txt"
def load() :
    try:
        with open(file) as dict_file :
            loaded_txt = dict_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
    except IOError as err :
        print(f"{err} Error opening {file}. Terminating program.")
        sys.exit(1)
    return loaded_txt
word_list = load()
word_list.append('a')
word_list.append('i')
word_list = sorted(word_list)

#print(word_list)

def getName() :
    return input("Enter name : ").lower()

def getAnagrams(name) :
    anagrams = []
    nameCount = Counter(name)
    for word in word_list :
        anagram = ""
        wordCount = Counter(word)
        for ch in word :
            if wordCount[ch] > nameCount[ch] :
                break
            anagram += ch
        if anagram == word :
            anagrams.append(anagram)
    return anagrams

def main():
    anaPhrase = []
    name = getName()
    remaining = list("".join(name.lower().split()))
    while remaining :
        anagrams = getAnagrams("".join(remaining))
        if not anagrams :
            print("phrase not possible")
            return []
        print(*anagrams, sep="\n")
        print("Remaining letters : ", end="")
        print(*remaining,sep=" ")
        print(f"no. of remaining letters : {len(remaining)}")
        print("Current anagram phrase : ", end="")
        print(*anaPhrase, sep="\n")
        choice = input("Enter a word or # to start again : ")
        if choice == "#":
            return []
        if choice in anagrams :
            anaPhrase.append(choice)
            for str in choice :
                remaining.remove(str)
    return anaPhrase

while True :
    print(*main(), sep=" ")