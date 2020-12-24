#Play War game 
import random
suits=('Hearts','Diamond','Spades','Clubs')
ranks= ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values= {"Two" : 2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queeen":12, "King":13, "Ace":14}
playing = True
#Card class
class card:
    def __int__ (self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
        print (self.values)
    def __str__ (self):
        print (values)
#Deck Class

class deck:
    def __init__ (self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Created the card object
                Created = card(suit,rank)
                self.all_cards.append(Created)
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return 'The Deck has: ' +deck_comp 
#shuffle class                 
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal(self):
        single_card = self.all_cards.pop()
        return single_card

class hand:
    def __init__(self):
        self.cards=[]
        self.value = 0
        self.aces = 0 
    def add_card(self,card):
        self.cards.append(card)
        self.value +=values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value = - 10
            self.aces = - 1
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0 
    def win_bet (self):
        self.total += self.bet
    def loose_bet(self):
        self.total = - self.bet
def take_bets(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet : "))
        except ValueError:
            if chips.bet == 0 :
                print ("Enter bets > 0 ")
        else:
            if chips.bet > chips.total :
                print ("Sorry, You bet can't execeed ", chips.total)
            else:
                break
def hit( deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing 
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print ("Dealer is playing ")
            playing = False
        else:
            print ("Please try again")
            continue
        break
def show_some(player, dealer):
    print ("\n Dealers hand: ")
    print (" <Card hidden>")
    print ('', dealer.cards[1])
    print ("\n Player's Hand: ", *player.cards, sep='\n ')
def show_all(player,delaer):
    print ("\n Dealers Hand: ", *dealer.cards, sep='\n ')
    print ("Dealers hand = ", dealer.value)
    print ("\n Players Hand: ", *player.cards, sep='\n ')
    print ("Players hand = ", player.value)

#Game scenarios :- Who wins and who losses

def player_loose(player,dealer,chips):
    print ("Player Lost! ")
    chips.loose_bet()
def player_wins(player,delaer,chips):
    print ("Player Wins!")
    chips.win_bet()
def dealer_loose(player,delaer,chips):
    print ("Dealer Lost!")
    chips.win_bet()
def delaer_wins(player,delaer,chips):
    print ("Dealer Wins!")
    chips.loose_bet()
def push(player,delaer,chips):
    print ("Dealer and Player Tie, Its a push.")

while True:
    print ("Welcome to Back Jack ")
    deck = Deck()


#Game Setup
#player_one = Player("One")
#player_two = Player("Two")
#new_deck = deck()
#new_deck.shuffle()


if __name__ == "__main__":
    new_deck= deck()

