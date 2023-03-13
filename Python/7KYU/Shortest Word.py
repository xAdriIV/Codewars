def find_short(s):
    word = s.split(' ')
    word.sort(key=len)
    return len(word[0])
