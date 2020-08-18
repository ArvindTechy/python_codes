def myfunc(words):
    new_word=[]
    n=0 #n=1 will captalize from first word
    for word in words:
        if n==0:
            nw=word.lower()
            new_word.append(nw)
            n=1  
        else:
            nw=word.upper()
            new_word.append(nw)
            n=0
    return''.join(new_word)
