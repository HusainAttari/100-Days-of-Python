import logos
import random
import os
from time import sleep

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

cards_logo = logos.Cards()


print(logos.logo)

#Constants and declarations
#cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
#player_cards = []
#dealer_cards = []
#player_score = 0
#dealer_score = 0
#lose = False

def draw(n=1):
    drawn = []
    for _ in range(0, n):
        drawn.append(cards.pop(cards.index(random.choice(cards))))
    return drawn

def score(x):
    
    def cmp(a):
        if a=='A':
            return 11
        if a=='K' or a=='Q' or a=='J':
            return 10
        return a
    
    x = list(map(cmp, x))
    x.sort()
    total = 0
    for card in x:
        if card==11:
            total += 11 if total+11<22 else 1
        else:
            total += card
    return total

play = True if input("Press Y to start the game and N to exit [y/n]:")=="y" else False
while play:
    clear()
    print(logos.logo)
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    lose = False
    print('The dealer draws two cards for you and two cards for themselves.')
    player_cards += draw(2)
    player_score = score(player_cards)
    dealer_cards += draw(2)
    print(f'Your cards : {player_cards}\nYour score : {player_score}')
    cards_logo.print(player_cards)
    print(f'Dealer\'s cards: [{dealer_cards[0]}, *]')
    cards_logo.print([dealer_cards[0], '*'])
    if player_score==21:
        print('BLACKJACK!!!\nYOU WIN! CONGRATULATIONS!\n')
        sleep(5)
        if input('Press Y to play again or N to stop playing [y/n]: ')=='y':
            continue
        else:
            break
    toDraw = True if input("Press D to draw or S to stand [d/s]:")=="d" else False
    while toDraw:
        clear()
        player_cards += draw()
        player_score = score(player_cards)
        print(f'Your cards : {player_cards}\nYour score : {player_score}')
        cards_logo.print(player_cards)
        print(f'Dealer\'s cards: [{dealer_cards[0]}, *]')
        cards_logo.print([dealer_cards[0], '*'])
        sleep(2)
        if player_score>21:
            print(f'\nPLAYER BUST!\nYOU LOSE!')
            lose = True
            break
        toDraw = True if input("Press D to draw or S to stand [d/s]:")=="d" else False
    if lose:
        if input('Press Y to play again or N to stop playing [y/n]: ')=='y':
            continue
        else:
            break
    while dealer_score<17:
        dealer_cards += draw()
        dealer_score = score(dealer_cards)
        print(f'Dealer\'s cards: {dealer_cards}\nDealer\'s score : {dealer_score}')
        cards_logo.print(dealer_cards)
        sleep(2)
    clear()
    print(f'Your cards : {player_cards}\nYour score : {player_score}')
    cards_logo.print(player_cards)
    print(f'Dealer\'s cards: {dealer_cards}\nDealer\'s score : {dealer_score}\n')
    cards_logo.print(dealer_cards)
    if dealer_score>21:
        print('DEALER BUST! YOU WIN!')
    elif dealer_score>player_score:
        print('DEALER WINS! BETTER LUCK NEXT TIME!')
    elif dealer_score==player_score:
        print('IT\'S A TIE!')
    else:
        print('YOU WIN! CONGRATULATIONS!')
    sleep(5)
    play = True if input('Press Y to play again or N to stop playing [y/n]: ')=='y' else False

clear()
print(logos.logo)
print('WE HOPE TO SEE YOU AGAIN!')