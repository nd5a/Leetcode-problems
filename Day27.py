# Check if a word occurs as a prefix of any word in a sentence

def isprefixWord(sentence, searchWord):
    words = sentence.split(" ")
    
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i + 1
    else:
        return -1