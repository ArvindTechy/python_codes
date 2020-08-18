#this will sort nos according to even and odd and generate a list of those numbers, this will only work for whole integers
def func(*args):#args will take multiple input and excute them 
    odd = []#blank list
    even = []#blank list
    for no in args:
        if no % 2 == 0:#divide by 2 if remainder 0 then continue or go to else
            even.append(no)#number will be added to even list
        else:
            odd.append(no)#number will be added to odd list
    print ("Even nos.=",even)#prints the list of even numbers
    print ("Odd nos.=",odd) #prints the list of odd numbers
