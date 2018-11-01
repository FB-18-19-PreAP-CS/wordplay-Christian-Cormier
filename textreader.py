#def at_least():
#    
#    with open("words.txt") as file:
#        count_the = 0
#        for word in file:
#            if len(word) >= 20:
#                print(word)
#        
#
#if __name__ == "__main__":
#    at_least()

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
def no_e():
    count_e = 0
    num_count = 0
    has_no_e()
    if True:
        num_count += 1
    if False:
        count_e += 1
    print(num_count / count_e)
        
if __name__ == "__main__":
    no_e()

                