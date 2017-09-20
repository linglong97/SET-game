from itertools import combinations


'''
Basically, take any combination of 3 cards out of the total number of cards.
We want to check if these 3 are a set, by iterating through each of the attributes,
and if any of the attributes has a count of 2(i.e. not all same or all different),
then we know it isn't a set. In that case, break the loop and go to the next combination
of 3 cards to check if that is a set. Otherwise, print the cards in a line.
'''

# this function converts the input strings into tuples with 4 attributes,
# (colour, number, symbol,shading)
# where colour is yellow, green, blue
# number is 1,2,3
# symbol is a,s,h
# shading is sy, l, u

def change_input_format(lines):
    symbols= {'a':'a','@':'a','A':'a','s':'s','S':'s', '$': 's','h':'h', 'H':'h', '#':'h'}
    shading = {'@':'sy', '#':'sy', '$':'sy', 'a':'l','s':'l', 'h':'l', 'A':'u', 'S':'u', 'H':'u'}
    newlines = []
    for line in lines[1:]:
        array = line.split(' ')
        values = (array[0],len(array[1]),symbols[array[1][0]], shading[array[1][0]])
        newlines.append(values)
           
    return newlines

def is_valid_set(cards):
    for i in range(4):
        if len(set(card[i] for card in cards)) == 2:
            return False
    return True

#reformats the tuple to be printed
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
    
    
def find_all_sets(lines):
    ans = []
    for cards in combinations(lines[1:], 3): 
        if not is_valid_set(cards):
            continue
        toprint = ''
        for card in cards:            
           toprint += reformat_card(card) + ' '
        
        print(toprint)        
if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    n = lines[0]
    new = change_input_format(lines)
    find_all_sets(new)

    
        
