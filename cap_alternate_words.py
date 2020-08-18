def myfunc(words):
    new_word=[]#empty list 
    n=0 #n=1 will captalize from first word
    for word in words:
        if n==0:
            nw=word.lower() #to lower the alphabet
            new_word.append(nw)#adds the word into the list
            n=1  #to switch the next word
        else:
            nw=word.upper()#to capitalize the alphabet 
            new_word.append(nw)#adds the word into the list
            n=0 #to switch the next word
    return''.join(new_word)#to combine the aplhabets into original word
