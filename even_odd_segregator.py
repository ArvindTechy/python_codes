def func(*args):
    odd = []
    even = []
    for no in args:
        if no % 2 == 0:
            even.append(no)
        else:
            odd.append(no)
    print ("Even nos.=",even)
    print ("Odd nos.=",odd) 
