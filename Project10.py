###############################################################
# CSE 231 project #10
#
# program that creates a klondike solitaire game.
# this program will use cards.py to use card and deck classes in order to develop the game
# 
#function to initialize the 4 different data structures.
#function to display the board.
#function to move a card from the stock pile to the waste pile.
#function to move a card from the waste pile to a given tableau column.
#function to move a card from the waste pile to a given foundation column.
#function to move a card from a given tableau column to a given foundation column.
#function to move a card from one tableau column to another tableau column.
#function to check if the game is in winning format.
#function to parse the move option in order to make the main function easier.
#main function to interact and with the user and display the board.
###############################################################

from cards import Card, Deck

#menu constant
MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''

#function to initialize the 4 different data structures.
def initialize():
    '''function to initialize the 4 different data structures.
    Parameters: none
    returns: tableau, stock, foundation, and waste data structures'''
    #create the deck and shuffle it
    the_deck = Deck()
    the_deck.shuffle()

    #create an empty waste list and an empty foundation list
    waste = []
    foundation = []
    for i in range(4):
        foundation.append([])
    #create empty stock and tableau data structure 
    stock = []
    tableau = []
    #create 7 empty columns for the tableau
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    
    #7 different for loops that deal the appropriate amound of cards in each column
    for i in range(7):
        col1.append(the_deck.deal())
        col2.append(the_deck.deal())
        col3.append(the_deck.deal())
        col4.append(the_deck.deal())
        col5.append(the_deck.deal())
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(6):
        col2.append(the_deck.deal())
        col3.append(the_deck.deal())
        col4.append(the_deck.deal())
        col5.append(the_deck.deal())
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(5):
        col3.append(the_deck.deal())
        col4.append(the_deck.deal())
        col5.append(the_deck.deal())
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(4):
        col4.append(the_deck.deal())
        col5.append(the_deck.deal())
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(3):
        col5.append(the_deck.deal())
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(2):
        col6.append(the_deck.deal())
        col7.append(the_deck.deal())
        break
    for i in range(1):
        col7.append(the_deck.deal())
        break
    
    #flip over each card in each column
    for card in col1:
        card.flip_card()
    tableau.append(col1)
    for card in col2:
        card.flip_card()
    tableau.append(col2)
    for card in col3:
        card.flip_card()
    tableau.append(col3)
    for card in col4:
        card.flip_card()
    tableau.append(col4)
    for card in col5:
        card.flip_card()
    tableau.append(col5)
    for card in col6:
        card.flip_card()
    tableau.append(col6)
    for card in col7:
        card.flip_card()
    tableau.append(col7)
    
    #flip over the last card in each column
    col1[-1].flip_card()
    col2[-1].flip_card()
    col3[-1].flip_card()
    col4[-1].flip_card()
    col5[-1].flip_card()
    col6[-1].flip_card()
    col7[-1].flip_card()

    #assign the stock to be the leftover cards after creating the tableau
    stock = the_deck 
    #add a card from the stock to the waste list
    waste.append(stock.deal())

    #return each data structure
    return tableau, stock, foundation, waste
    
#function to display the board.    
def display(tableau, stock, foundation, waste):
    """ display the game setup 
    parameters: tableau, stock, foundation, and waste data structures
    returns: Nothing"""
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    
#function to move a card from the stock pile to the waste pile.
def stock_to_waste( stock, waste ):
    '''function to move a card from the stock pile to the waste pile.
    parameters: stock and waste data structures
    returns: true or false depending on if the move is valid or not'''
    #if the stock pile is not empty, add the last card to the waste pile
    #if the stock pile is empty, then the move isnt valid
    if len(stock) != 0:
        waste.append(stock.deal())
        return True
    else:
        return False
    
#function to move a card from the waste pile to a given tableau column.    
def waste_to_tableau( waste, tableau, t_num ):
    '''function to move a card from the waste pile to a given tableau column.    
    parameters: waste tableau and column number
    returns: true or false depending on if the move is valid or not'''
    #create a destination variable
    destination = tableau[t_num]
    #if the destination has no cards, only a king can be added to the column
    if len(destination) == 0:
        if waste[-1].rank() == 13:
            destination.append(waste[-1])
            waste.pop()
            return True
        else:
            return False
    #if the column is not empty, then check many different factors to see if the card can be added or not
    elif len(destination) != 0:
        #if the card is black
        if waste[-1].suit() == 1 or waste[-1].suit() == 4:
            #if the last card in the destination is red and one higher than the source card, then move is valid
            if (destination[-1].suit() == 2 or destination[-1].suit() == 3) and (waste[-1].rank() == destination[-1].rank() -1):
                destination.append(waste[-1])
                waste.pop()
                return True
            #if not a valid move, return False
            else:
                return False
        # if the card is red
        elif waste[-1].suit() == 2 or waste[-1].suit() == 3:
            #if the last card in the destination is blacka and one higher than the source card, then move is valid
            if (destination[-1].suit() == 1 or destination[-1].suit() == 4) and (waste[-1].rank() == destination[-1].rank() -1):
                destination.append(waste[-1])
                waste.pop()
                return True
            #if not a vaid move, return False
            else:
                return False
        
#function to move a card from the waste pile to a given foundation column.
def waste_to_foundation( waste, foundation, f_num ):
    '''function to move a card from the waste pile to a given foundation column.
    parameters: waste, foundation and foundation column number
    returns true if move is valid, false otherwise'''
    #create a destination variable
    destination = foundation[f_num]
    #if the destination has no cards in it, then only an ace can be added
    if len(destination) == 0:
        if waste[-1].rank() ==1:
            destination.append(waste[-1])
            waste.pop()
            return True
        else:
            return False
    #if the destination isnt empty 
    #check and see if the suit is the same and the rank is one higher than last card in the destination column
    elif len(destination) != 0:
        if waste[-1].suit() == destination[-1].suit() and waste[-1].rank() == destination[-1].rank() +1:
            destination.append(waste[-1])
            waste.pop()
            return True
        else:
            return False

#function to move a card from a given tableau column to a given foundation column.
def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''function to move a card from a given tableau column to a given foundation column.
    parameters: tableau, foundation, t_num, f_num
    returns: True if the move is valid, false otherwise'''
    #create destination and source card variables
    destination = foundation[f_num]
    the_card = tableau[t_num][-1]
    
    # if the destination has no cards, then only an ace can be moved
    if len(destination) == 0:
        if the_card.rank() == 1:
            destination.append(the_card)
            tableau[t_num].pop()
            if len(tableau[t_num]) != 0:
                if tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card()
            return True
        else:
            return False
    #if the destination is not empty, then use some criteria
    elif len(destination) != 0:
        #if the card is the same suit as previous suits and is one rank higher, then move is valid
        if the_card.suit() == destination[-1].suit() and the_card.rank() == destination[-1].rank() + 1:
            destination.append(the_card)
            tableau[t_num].pop()
            if len(tableau[t_num]) != 0:
                if tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card()
            return True
        #if not, move is invalid
        else:
            return False

#function to move a card from one tableau column to another tableau column.
def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''function to move a card from one tableau column to another tableau column.
    parameters: tableau, tableau source column, tableau destination column
    returns: true if move is valid, false otherwise'''

    #create a destination variable
    destination = tableau[t_num2]
    #if the destination column is empty, then only a king can be moved into it
    if len(destination) == 0:
        if tableau[t_num1][-1].rank() == 13:
            destination.append(tableau[t_num1][-1])
            tableau[t_num1].pop()
            if len(tableau[t_num1]) != 0:
                if tableau[t_num1][-1].is_face_up() == False:
                    tableau[t_num1][-1].flip_card()
            return True
        else:
            return False
    # if the destination is not empty then check criteria
    elif len(destination) != 0:
        #check if the card is black
        if tableau[t_num1][-1].suit() == 1 or tableau[t_num1][-1].suit() == 4:
            #if the card is black then it can only be moved onto a red one
            #also check if the rank is one lower than destination card
            if (destination[-1].suit() == 2 or destination[-1].suit() == 3) and (tableau[t_num1][-1].rank() == destination[-1].rank() -1):
                destination.append(tableau[t_num1][-1])
                tableau[t_num1].pop()
                #if the move was valid then check and see if we need to flip the new last card
                if len(tableau[t_num1]) != 0:
                    if tableau[t_num1][-1].is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
                return True
            #if invalid, return false
            else:
                return False
        #chekc if card is red
        elif tableau[t_num1][-1].suit() == 2 or tableau[t_num1][-1].suit() == 3:
            #if the card is red, it can only be moved onto a black one
            #also check if the rank is one lower than the destination card
            if (destination[-1].suit() == 1 or destination[-1].suit() == 4) and (tableau[t_num1][-1].rank() == destination[-1].rank() -1):
                destination.append(tableau[t_num1][-1])
                tableau[t_num1].pop()
                #if the move was vaild, check and see if we need to flip the new last card
                if len(tableau[t_num1]) != 0:
                    if tableau[t_num1][-1].is_face_up() == False:
                        tableau[t_num1][-1].flip_card()
                return True
            # if invalid, return false
            else:
                return False


#function to check if the game is in winning format.
def check_win (stock, waste, foundation, tableau):
    '''function to check if the game is in winning format.
    paramters: stock, waste, foundation, and tableau data strucures
    returns: true if the game has been won, false otherwise'''
    #check to see if stock and waste data structures are empty
    if len(stock) == 0:
        if len(waste) == 0:
            #check to see if each tableau column is empty
            if len(tableau[0]) == 0 and len(tableau[1]) == 0 and len(tableau[2]) == 0 and len(tableau[3]) == 0 and len(tableau[4]) == 0 and len(tableau[5]) == 0 and len(tableau[6])==0:
                #check to see if each foundation column has 13 cards in it
                if len(foundation[0]) == 13 and len(foundation[1]) == 13 and len(foundation[2]) == 13 and len(foundation[3]) == 13:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

#function to parse the move option in order to make the main function easier.
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above

#main function to interact and with the user and display the board.
def main():   
    #initialize the board
    tableau, stock, foundation, waste = initialize()
    #print the menu options
    print(MENU)
    #display the board
    display(tableau, stock, foundation, waste)
    option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
    #prompt for an option and parse the option
    the_parse = parse_option(option) 
    #if error in the option, display the board and reprompt
    while the_parse == None:
        display(tableau, stock, foundation, waste)
        option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        the_parse = parse_option(option) 
    #while the user hasn't quit the program
    while the_parse[0] != 'Q':
        #if the user option is TT
        if the_parse[0] == 'TT':
            #call tableau_to_tableau function to see if the move is valid
            tt_move = tableau_to_tableau(tableau, the_parse[1] - 1, the_parse[2] - 1)
            #if valid, display the board
            if tt_move == True:
                display(tableau, stock, foundation, waste)
                #if not print error message and display the board
            else:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
        #if the user option is TF
        elif the_parse[0] == 'TF':
            #call tableau_to_founation fuction to see if the move was valid
            tf_move = tableau_to_foundation(tableau, foundation, the_parse[1] - 1, the_parse[2] - 1)
            #if valid, display the board and check if the game has been won
            if tf_move == True:
                #if the game has been won, quit the loop
                if check_win(stock, waste, foundation, tableau) == True:
                    print('You won!')
                    display(tableau, stock, foundation, waste)
                    break
                elif check_win(stock, waste, foundation, tableau) == False:
                    display(tableau, stock, foundation, waste)
            else:
                #if not valid, print error message and display the board
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
        #if the option is WT
        elif the_parse[0] == 'WT':
            #call waste_to_foundation function in order to see if the move was valid
            wt_move = waste_to_tableau(waste, tableau, the_parse[1] - 1)
            #if move was valid, display the board, if not, print error message and display the board
            if wt_move == True:
                display(tableau, stock, foundation, waste)
            else:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
        #if the option is WF
        elif the_parse[0] == 'WF':
            #call waste_to_foundation function to see if move was valid
            wf_move = waste_to_foundation(waste, foundation, the_parse[1] - 1)
            #if valid move, check to see if the game is in winning condition
            if wf_move == True:
                #if the game has been won, display message, the baord, and quit the game
                if check_win(stock, waste, foundation, tableau) == True:
                    print('You won!')
                    break 
                    display(tableau, stock, foundation, waste)
                elif check_win(stock, waste, foundation, tableau) == False:
                    display(tableau, stock, foundation, waste)
            #if the move was invalid, display error message and display the board
            else:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
        #if the option is SW
        elif the_parse[0] == 'SW':
            #call stock to waste function to see if the move is valid
            sw_move = stock_to_waste(stock, waste)
            #if the move is valid, display the board, if invalid, display error message and display board
            if sw_move == True:
                display(tableau, stock, foundation, waste)
            else:
                print("\nInvalid move!\n")
                display(tableau, stock, foundation, waste)
        # if the option is R
        elif the_parse[0] == 'R':
            #initialize the game again and display the baord
            tableau, stock, foundation, waste = initialize()
            print(MENU)
            display(tableau, stock, foundation, waste)
        #if the option is H print the menu options
        elif the_parse[0] == 'H':
            print(MENU)
        #remprompt for option and parse the option
        option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        the_parse = parse_option(option) 
        #if error in option, print error message and reprompt
        while the_parse == None:
            display(tableau, stock, foundation, waste)
            option = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
            the_parse = parse_option(option) 
    

if __name__ == '__main__':
     main()
