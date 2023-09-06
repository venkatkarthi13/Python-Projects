#Anagram

words = input("Enter your word: ").lower()
lists = input("Enter some list of words: ").lower().split(',')

def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def find(word, list):
    anagrams = []
    for lists in list:
        if anagram(word, lists):
         anagrams.append(lists)
    return anagrams
anagrams = find(words, lists)

if anagrams:
    print("Anagram Found:",','.join(anagrams))
else:
    print("No anagrams found try another word or list")

