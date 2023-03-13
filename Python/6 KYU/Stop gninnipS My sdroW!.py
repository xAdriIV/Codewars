def spin_words(sentence):
    sentence = sentence.split()
    
    for word in range (len(sentence)):
        if len(sentence[word]) >= 5:
            sentence[word] = sentence[word][::-1]
    return " ".join(sentence)