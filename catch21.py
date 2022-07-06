#Catch 21, Blackjack, 21
#Trista Smith
#4 July 2022

import sys, random
print(
"""
Rules of 21: 
    Get as close to 21 without busting (going over)
        Queen, King, Jack = 10 points
        Aces = 1 or 11 points
        2 - 10 = Their face value
    (H)it = draws another card
    (S)tand = stop drawing cards
    Tie = bets returned or restart
"""
)

HEARTS = chr(9829)
SPADES = chr(9824)
CLUBS = chr(9827)
DIAMONDS = chr(9830)

BACKSIDE = 'backside'

def getBet(maxBet):
    #ask amount to bet
    while True: #keep asking until vailed amount
        print('How much would you like to bet? $1-${}, or Q'.format(maxBet))
        bet = input('> ').upper()
        if bet == 'Q':
            print('Until next time!')
            sys.exit()
        if not bet.isdecimal():
            continue #repeat if no number entered
        
        bet = int(bet)

        if 1 <= bet <= maxBet:
            return bet #vaild number entered



def getDeck(): #return list (rank, suit) for all 52 cards
    deck = []
    for suit in (SPADES, HEARTS, CLUBS, DIAMONDS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #add face and aces
    random.shuffle(deck)
    return deck



def displayHands(playerHand, dealerHand, showDealerHand): #show player's hand, hide dealers first card if card showDealerHand is false
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ?')
        displayCards([BACKSIDE]+ dealerHand[1:])
    #show player cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards): #returns value of cards. function picks best ace value
    value = 0 
    numberofAce = 0

    #value of non-ace cards
    for card in cards:
        rank = card[0]
        if rank =='A':
            numberofAce += 1
        elif rank in ('K', 'Q', 'J'): #face cards = 10 points
            value += 10
        else:
            value += int(rank) #number cards = correcsponding number
    
    #value for aces
    value += numberofAce
    for i in range(numberofAce):
        if value + 10 <= 21:
            value += 10
    return value
    
def displayCards(cards): #displays all cards in card list
    
    rows = ['', '', '', '', ''] #text in each row
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' #prints top line of card
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|   |'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))    

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move

def main():    

    money = 1000       
    while True: # main loop
        #check is player has money
        if money <= 0:
            print('You Broke, You Leave Now!')
            sys.exit()

        #player enters bet
        print(f'Your wallet: ${money}')
        bet = getBet(money)

        #player and dealer recieve 2 cards from deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #player actions
        print(f'Bet: ${bet}')
        while True: #loop keeps going until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            
            #check is player bust
            if getHandValue(playerHand) > 21:
                print("You busted!")
                break

            #get player moves (H) or (S)
            move = getMove(playerHand, money - bet)

            #player actions
            if move in ('H'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S'):
                break
        #dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer's hit......")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    print('Dealer has busted')
                    break
                input('Press Enter to continue.')
                print('\n\n')

        #reveal final hand
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)


        #player won, lost, or tied
        if dealerValue > 21:
            print('You WIN ${}!'.format(bet))
            money += bet
        elif (playerValue) > 21 or (playerValue < dealerValue):
            print('Take an L')
            money -= bet
        elif playerValue > dealerValue:
            print('You WIN ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("A TIE. Bets have been returned")
        input("Press Enter to continue.")
        print('\n\n')


if __name__ == '__main__':
    main()