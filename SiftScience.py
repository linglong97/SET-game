from itertools import combinations
'''
This code is for a program that takes in lines of input of the format of cards in the SET game,
and returns on the first line, the number of possible SETs from the cards inputted, the max number of disjoint intervals,
and then prints the disjoint intervals.
This code could be written using classes, but that is unnecessary.

'''




maxcounter = 0

maxset = []





'''
This function takes in our raw input "lines" and reformats the input into a list of tuples containing the attributes.
For example, Blue # will be converted into a 4 attribute tuple of the format: (Colour, Length, Symbol, Shading).
This is converted into a tuple to easily deal with it when checking if a collection of 3 cards is a SET.
'''

def change_input_format(lines):
    symbols= {'a':'a','@':'a','A':'a','s':'s','S':'s', '$': 's','h':'h', 'H':'h', '#':'h'}
    shading = {'@':'sy', '#':'sy', '$':'sy', 'a':'l','s':'l', 'h':'l', 'A':'u', 'S':'u', 'H':'u'}
    newlines = []
    for line in lines[1:]: # first line of input is number of cards
        array = line.split(' ')
        values = (array[0],len(array[1]),symbols[array[1][0]], shading[array[1][0]])
        newlines.append(values)          
    return newlines



'''
Checks if a group of 3 cards is a valid SET. For each attribute(an item in the tuple), it checks if the count of that attribute
for is 2. If it's 2, it can't be all the same or all the different for that attribute, so return False. Else, return True.
'''
def is_valid_set(cards):
    for i in range(4):
        if len(set(card[i] for card in cards)) == 2:
            return False
    return True


'''
itertools.combinations returns all possible combinations of specified length from a list. Therefore we can use it to generate every possible
grouping of 3 cards, and check if they form a set one-by-one. This is a brute force algorithm, and takes O(N choose 3) ~ O(N^3) algorithm.
(assuming that generating one combination is O(1), and since is_valid_set is O(1) since the number of attributes and attribute choices are known)

'''
def find_all_sets(lines):
    ans = []
    for cards in combinations(lines, 3): 
        if not is_valid_set(cards):
            continue
        toadd = []
        for card in cards:            
             toadd.append(card)
        ans.append(toadd)
    return (ans)

'''
This function passes in all possible SETs, and searches for groups of disjoint SETs. It starts from the beginning of the SETs, and either adds the SET
to our current list of disjoint sets(if it passes our check that it's disjoint from all the sets in our current list), or moves on to the next set in our list
of SETs. The function returns if the SET at index which we're checking is already in our set of disjoint SETs.

'''


def find_disjoint_sets(index, sets, currsetindices, currcards, counter):
    global maxcounter
    global maxset
    if index > len(sets)-1: # if the index has passed the end, return
        return
    
    if counter >= maxcounter: # if the current size
        maxcounter = counter
        maxset = currsetindices

    find_disjoint_sets((index+1), sets, currsetindices, currcards, counter)

    #if the current index we are at is disjoint from our current set
    if sets[index][0] not in currcards and sets[index][1] not in currcards and sets[index][2] not in currcards: 
        if counter >= maxcounter:
            maxset = currsetindices+[index]
        find_disjoint_sets(index+1, sets, currsetindices+[index],currcards+[sets[index][0], sets[index][1], sets[index][2]], counter+1)
    return
        
'''
Once we are done with the tuple formatted input, change it back to the original input to print as output.
'''

def reformat_card(card):
    adict = {'u': 'A', 'l': 'a', 'sy': '@'}
    sdict = {'u': 'S', 'l': 's', 'sy': '$'}
    hdict = {'u': 'H', 'l': 'h', 'sy': '#'}
    newcard = card[0]+ ' '
    if card[2] == 'a':
        newcard+= adict[card[3]]*card[1]
    elif card[2] == 's':
        newcard+= sdict[card[3]]*card[1]
    else:
        newcard +=hdict[card[3]]*card[1]
    return newcard    
    
if __name__ == "__main__":

    # first, read the input into a list 
    lines = open("input2.txt").read().splitlines()

    # the first line will be the number of input cards
    n = lines[0]

    # use our helper function to convert the cards from strings into tuples of attributes
    lines = change_input_format(lines)

    # use our function to find all sets of the tuples 
    sets = find_all_sets(lines)

    # use our function to act on all possible SETs to generate the max sized disjoint collection of SETs
    find_disjoint_sets(0, sets, [],[], 0)

    #first line
    print len(sets) 
    print len(maxset) # second line
       
    for index in maxset:
        print '\n'
        for item in sets[index]:
            print reformat_card(item)
    
            
    
