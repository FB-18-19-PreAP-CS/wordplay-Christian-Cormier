#def at_least():
#    
#    with open("words.txt") as file:
#        count_the = 0
#        for word in file:
#            if len(word) >= 20:
#                print(word)
#        
#

#def has_no_e(word):
#    '''
#    >>> has_no_e('texas')
#    False
#    
#    >>> has_no_e('UTEMP')
#    False
#    
#    >>> has_no_e('longhorn')
#    True
#    '''
#    if 'e' in word.lower():
#        return False
#    else:
#        return True
#def no_e():
#    with open("words.txt") as file:
#        count_e = 0
#        for word in file:
#            if has_no_e(word):
#                count_e += 1
#    percent = (count_e/ 113809) 
#    print(f"{percent * 100:.2f}%")


#def avoid(word,letters):
#    '''
#    >>> avoid('gain','a')
#    False
#    
#    >>> avoid('cod','z')
#    True
#    
#    >>> avoid('bibliography','i')
#    False
#    '''
#    f = 0
#    for i in range(0,len(letters)):
#        if letters[i] in word:
#            f += 1
#        else:
#            pass
#    if f > 0:
#        return False
#    if f == 0:
#        return True
#def count_avoids():
#    with open("words.txt") as file:
#        inp = input("what forbidden letters are you looking for--")
#        count_a = 0
#        for word in file:
#            if avoid(word,inp):
#                count_a += 1
#        print(count_a)

def uses_only(word,letters):
    '''
    >>> uses_only('gain','al')
    False
    
    >>> uses_only('cod','doc')
    True
    
    >>> uses_only('bibliography','iblography')
    True
    '''
    f = 0
    for i in range(0,len(letters)):
        if letters[i] in word:
            f += 1
        else:
            pass
    if f == len(letters):
        return True
    else:
        return False
    
def words_with_only(letters):
    with open("words.txt") as file:
        inp = input("what letters are you looking for--")
        count_a = 0
        for word in file:
            if uses_only(word,inp):
                count_a += 1
        print(count_a)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #at_least()
    #no_e()
    #count_avoids()
    words_with_only()

                