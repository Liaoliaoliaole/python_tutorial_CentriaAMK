#BlackJack cardgame (Note: part ok => 3 classes ok)

import random
from sys import exit

class Poke:
    def __init__(self):
        self.cards = [[face, suite] for face in "♠♥♦♣" for suite in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']]
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.cards = Poke().cards

    def give_one_card(self):
        if not self.cards:
            self.cards.extend(Poke().cards)
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.points = 0
        self.cards_in_hand = []

    def init(self):
        self.cards_in_hand = []
        self.points = 0

    def now_count(self):
        point = 0 
        for  suite in self.cards_in_hand:
            if suite in ['J', 'Q', 'K']:
                suite = 10
            point += suite
        self.points = point

    def is_win(self, player):
        s1 = self.points
        s2 = player.points
        if s1 > s2:
            print(f"Player {self.name} has {s1} points, Computer {player.name} has {s2} points, Player {self.name} wins!")
            self.score += 1
        elif s1 == s2:
            print(f"Player {self.name} has {s1} points, Computer {player.name} has {s2} points, draw!")
        else:
            print(f"Player {self.name} has {s1} points, Computer {player.name} has {s2} points, Computer {player.name} wins!")
            player.score += 1            

    def get(self, *cards):
        for card in cards:
            self.cards_in_hand.append(card)
        self.now_count() # reset points

# game playing main function
def main(dealer: Dealer, computer: Player, human: Player):
    # round counts
    count = 0
    while True:
        count += 1
        print(f"Round {count}：")
        #set for gameover in advance
        flag = False
            
        human.init()
        computer.init()
        # two cards each
        human.get(dealer.give_one_card(), dealer.give_one_card())
        computer.get(dealer.give_one_card(), dealer.give_one_card())
        print(f"Player {human.name}'s hand: {human.cards_in_hand[-2]}, {human.cards_in_hand[-1]}")
        print(f"Computer {computer.name}'s hand: {computer.cards_in_hand[-2]}, ?")
        # judging whether it's blackjack
        if human.points == 21 == computer.points:
            print("Player {human.name} and Computer {computer.name} both get 21 points, draw!")
        elif human.points == 21:
            print("Player {human.name} has 21 points, congratulation {human.name} wins!")
            human.score += 1
        else:
            # Player ask more card
            while True:
                if_next_card = input("Continue getting card: (Y/N)")
                if if_next_card in ['N', 'n']:
                   break                   
                elif if_next_card in ['Y', 'y']:
                    human.get(dealer.give_one_card())
                    print(f"Player {human.name} gets {human.cards_in_hand[-1]}, Player {human.name}'s hand: '{human.cards_in_hand}")
                    # judging if player over 21，if it is, gave over in advance, set true
                    if human.points > 21:
                        print(f"Player {human.name} has {human.points} points, over 21 points, Player {human.name} lost!")
                        computer.score += 1
                        flag = True
                        break
                # Computer ask card
            if not flag:
                # if points smaller than human player, ask more
                while computer.points < human.points:
                    computer.get(dealer.give_one_card())
                    print(f"Computer {computer.name} gets: {computer.cards_in_hand[-1]}, Computer {computer.name}'s hand: {computer.cards_in_hand}")
                    # judging if computer over 21，if it is, gave over in advance
                if computer.points > 21:
                    print(f"Computer {computer.name} has {computer.points} points, over 21, Congratulation {human.name} wins!")
                    human.score += 1
                else:
                # If there is no early end, that is, if both are less than 21 points, judge whether to win or lose
                    human.is_win(computer)
        print("-" * 30)
        # if next round
        if_play_again = input("One more try?:(Y/N)")

        if if_play_again in ['Y', 'y']:
            print(f"Player {human.name}, Computer {computer.name} total scores is {human.score}:{computer.score}")
            # if fully stop，print result
        elif if_play_again in ['N', 'n']:
            print(f"PLAYER {human.name},COMPUTER {computer.name} final score : {human.score}:{computer.score}")
            if human.score > computer.score:
                print(f"{human.name}win!")
            elif human.score < computer.score:
                print(f"{computer.name}win! ")
            else:
                print("The battle is fierce, you are even!")
            print("GAME OVER")
            exit(0)
        else:
            print("Invalid input, input again: ")

# game starts
computer = Player('Robo')
human = Player('Lili')
dealer = Dealer()
main(dealer, computer, human)
