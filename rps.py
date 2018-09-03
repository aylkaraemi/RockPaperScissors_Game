#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

standard = ['rock', 'paper', 'scissors']

RPSLS = ['rock', 'paper', 'scissors', 'lizard', 'spock']

Pokemon = ['charmander', 'bulbasaur', 'squirtle']

BearHunterNinja = ['bear', 'hunter', 'ninja']

Lovecraft = ['cthulhu', 'elder sign', 'cultist']

variants = ['standard', 'rpsls', 'pokemon', 'bhn', 'lovecraft']


"""The Player class is the parent class for all of the Players
in this game"""

import random

class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

class Human(Player):
    def __init__(self):
        self.name = input("Greetings Gentlebeing! What is your name? ")

    def move(self):
        return input("What is your move? ")

class Rock(Player):
    def __init__(self, variant):
        self.name = "Toph Beifong"
        self.variant = variant

    def move(self):
        if self.variant == 'standard' or self.variant == 'rpsls':
            return 'rock'
        if self.variant == 'pokemon':
            return 'Bulbasaur'
        if self.variant == 'bhn':
            return 'Bear'
        if self.variant == 'lovecraft':
            return 'Elder Sign'

class Random(Player):
    def __init__(self, moves):
        self.name = "Random Frequent Flyer Dent"
        self.moves = moves

    def move(self):
        return random.choice(self.moves)

class Cycle(Player):
    def __init__(self, moves):
        self.name = random.choice(["Agrajag", "Aang", "Korra", "Dave Lister", "Jane"])
        self.moves = moves
        self.prev_move = random.choice(self.moves)

    def move(self):
        index = (moves.index(self.prev_move) + 1) % len(moves)
        return moves[index]

    def learn(self, my_move, their_move):
        self.prev_move = my_move

class Mimic(Player):
    def __init__(self, moves):
        self.name = random.choice(["Raven Darkhölme", "Braling Two", "Stephen Byerley"])
        self.moves = moves
        self.opponent_move = random.choice(self.moves)

    def move(self):
        return self.opponent_move

    def learn(self, my_move, their_move):
        self.opponent_move = their_move

class Strategic(Player):
    def __init__(self, moves, variant):
        self.name = random.choice(["Harbinger", "Jeeves", "SCORPIO"])
        self.moves = moves
        self.variant = variant
        self.losing_move = random.choice(self.moves)

    def move(self):
        return self.losing_move

    def learn(self, my_move, their_move):
        if my_move == their_move:
            self.losing_move = random.choice(moves)
        elif beats(my_move, their_move, self.variant):
            self.losing_move = their_move
        else:
            self.losing_move = my_move


def beats(one, two, variant):
    if variant == 'standard':
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))
    if variant == 'rpsls':
        return ((one == 'rock' and two == 'scissors') or
                (one == 'rock' and two == 'lizard') or
                (one == 'paper' and two == 'rock') or
                (one == 'paper' and two == 'spock') or
                (one == 'scissors' and two == 'paper') or
                (one == 'scissors' and two == 'lizard') or
                (one == 'lizard' and two == 'paper') or
                (one == 'lizard' and two == 'spock') or
                (one == 'spock' and two =='scissors') or
                (one == 'spock' and two == 'rock'))
    if variant == 'pokemon':
        return ((one == 'charmander' and two == 'bulbasaur') or
                (one == 'bulbasaur' and two == 'squirtle') or
                (one == 'squirtle' and two == 'charmander'))
    if variant == 'bhn':
        return ((one == 'bear' and two == 'ninja') or
                (one == 'ninja' and two == 'hunter') or
                (one == 'hunter' and two == 'bear'))
    if variant == 'lovecraft':
        return ((one == 'cthulhu' and two == 'cultist') or
                (one == 'cultist' and two == 'elder sign') or
                (one == 'elder sign' and two == 'cthulhu'))


def valid_move(move, moves):
    move = move.lower()
    while move not in moves:
        move = input(f"{move}? That doesn't match any choices. \nPlease choose again from the following options: \n{moves} \n")
        move = move.lower()
    return move


def game_type():
    type = input("\nYou can play a single game of rock paper scissors or a  tournament. Let me know what you would prefer. \nType 'g' if you would like to play a single game or 't' if you would like to play a tournament. \n")
    while type.lower() != 'g' and type.lower() != 't':
        type = input("I'm afraid your response was invalid. \n Please type 'g' to play a single game or 't' if you would prefer a tournament. \n")
    return type


def game_variant():
    print("This game allows you to play different variants of rock paper scissors.\n")
    variant = input("Please select which variant you would like to play. \nFor standard rock paper scissors, enter: standard \nFor Rock-Paper-Scissors-Lizard-Spock, enter: rpsls \nFor Bear-Hunter-Ninja, enter: bhn \nFor the Pokemon themed variant, enter: pokemon \nFor the Lovecraftian themed variant, enter: lovecraft \n\n")
    variant = valid_move(variant, variants)
    rules(variant)
    return variant

def rules(variant):
    need_rules = input(f"Do you need to know the rules for the {variant} moves? (y/n) \n")
    while need_rules != 'y' and need_rules != 'n':
        need_rules = input("I'm sorry, I don't understand. \nPlease type 'y'if you need to know the rules for this variant or 'n' to skip. \n")
    if need_rules == 'y':
        if variant == 'standard':
            print("Rock smashes Scissors \nPaper covers Rock \nScissors cuts Paper\n\n")
        elif variant == 'rpsls':
            print("Rock smashes Scissors and crushes Lizard \nPaper covers Rock and disproves Spock \nScissors cuts Paper and decapitates Lizard \nLizard eats paper and poisons Spock \nSpock smashes Scissors and vaporizes Rock\n\n")
        elif variant == 'pokemon':
            print("Charmander defeats Bulbasaur \nBulbasaur defeats Squirtle \nSquirtle defeats Charmander\n\n")
        elif variant == 'bhn':
            print("Bear eats Ninja \nNinja kills Hunter \nHunter shoots Bear\n\n")
        else:
            print("Cthulhu eats Cultist \nCultist destroys Elder Sign \nElder Sign imprisons Cthulhu\n\n")
    else:
        print("Then enjoy your game!")


def move_set(variant):
    if variant == 'standard':
        return standard
    if variant == 'rpsls':
        return RPSLS
    if variant == 'pokemon':
        return Pokemon
    if variant == 'bhn':
        return BearHunterNinja
    if variant == 'lovecraft':
        return Lovecraft


def create_opponent(moves, variant):
    opponent_type = random.choice(['rock', 'random', 'cycle', 'mimic', 'strategic'])#put the list here since rubric said do not use global variables except for moves. Let me know if I should move the list of player subclasses to a global variable
    if type == 'rock':
        return Rock(variant)
    elif type == 'random':
        return Random(moves)
    elif type == 'cycle':
        return Cycle(moves)
    elif type == 'mimic':
        return Mimic(moves)
    else:
        return Strategic(moves, variant)


def choose_opponents(players):
    p1 = random.choice(players)
    players.pop(players.index(p1))
    p2 = random.choice(players)
    players.pop(players.index(p2))
    return p1, p2


def tourney_round(players, score, moves, variant):
    winners = []
    losers = []
    while len(players) > 1:
        opponent1, opponent2 = choose_opponents(players)
        game = Game(opponent1, opponent2, moves, variant)
        winner, loser = game.play_game()
        winners.append(winner)
        losers.append(loser)
        score[loser][1] += 1
        score[winner][0] += 1
    if players:
        losers.append(players[0])
    return winners, losers


def elimination(losers, score, eliminated):
    for loser in losers:
        if score[loser][1] == 3:
            losers.pop(losers.index(loser))
            eliminated.append(loser)
            print(f"{loser.name} has been eliminated\n")

def play_tournament(moves, variant):
    player2 = Rock(variant)
    player3 = Random(moves)
    player4 = Cycle(moves)
    player5 = Mimic(moves)
    player6 = Strategic(moves, variant)
    score = {player1 : [0, 0], player2 : [0, 0], player3 : [0, 0], player4 : [0, 0], player5 : [0, 0], player6: [0, 0]}
    players = [player1, player2, player3, player4, player5, player6]
    eliminated = []
    round = 1
    print(f"Tournament Begin:\nTourney Round {round}\n")
    winners, losers = tourney_round(players, score, moves, variant)
    round += 1
    while len(eliminated) < 5:
        elimination(losers, score, eliminated)
        print(f"Tourney Round{round}\n")
        if len(winners) >= 2 and len(losers) >=2:
            winners1, losers1 = tourney_round(winners, score, moves, variant)
            winners2, losers2 = tourney_round(losers, score, moves, variant)
            winners = winners1 + winners2
            losers = losers1 + losers2
        else:
            players = winners + losers
            winners, losers = tourney_round(players, score, moves, variant)
        round +=1
    players = winners + losers
    winner = players[0]
    print(f"Tournament Over!\nWinner is {winner.name}! \n\nScores were:\n{player1.name}: {score[player1][0]} wins and {score[player1][1]} losses \n{player2.name}: {score[player2][0]} wins and {score[player2][1]} losses \n{player3.name}: {score[player3][0]} wins and {score[player3][1]} losses \n{player4.name}: {score[player4][0]} wins and {score[player4][1]} losses \n{player5.name}: {score[player5][0]} wins and {score[player5][1]} losses \n{player6.name}: {score[player6][0]} wins and {score[player6][1]} losses\n\n")


class Game:
    def __init__(self, p1, p2, moves, variant):
        self.p1 = p1
        self.name1 = p1.name
        self.p2 = p2
        self.name2 = p2.name
        self.moves = moves
        self.variant = variant

    def play_round(self):
        move1 = valid_move(self.p1.move(), self.moves)
        move2 = valid_move(self.p2.move(), self.moves)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"{self.name1}: {move1}  {self.name2}: {move2}")
        if move1 == move2:
            print("Tie\n")
        elif beats(move1, move2, self.variant):
            print(f"{self.name1} wins!\n")
            return "player1"
        else:
            print(f"{self.name2} wins!\n")
            return "player2"

    def tiebreaker(self, score):
        rounds = 0
        print("Score is tied. Entering tiebreaker round to determine winner.")
        while score['player1'] == score['player2']:
            self.keep_score(score)
            rounds += 1
            if rounds == 10:
                print("Game is still tied, winner will be chosen by coin flip.")
                winner = random.choice(['player1', 'player2'])
                score[winner] +=1


    def keep_score(self, score):
        winner = self.play_round()
        if winner != None:
            score[winner] = score[winner] + 1

    def play_game(self):
        score = {"player1" : 0, "player2" : 0}
        print(f"{self.name1} vs {self.name2}\n")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.keep_score(score)
        if score['player1'] == score['player2']:
            self.tiebreaker(score)
        if score['player1'] > score['player2']:
            winner = self.p1
            loser = self.p2
            winner_name = self.name1
        else:
            winner = self.p2
            loser = self.p1
            winner_name = self.name2
        print(f"Rounds complete! \nFinal score is {self.name1} {score['player1']} and {self.name2}: {score['player2']}. \nThe winner is {winner_name}!\n\n")
        return winner, loser


if __name__ == '__main__':
    player1 = Human()
    play = "y"
    variant = game_variant()
    moves = move_set(variant)
    while play == "y" or play == "yes":
        tournament = game_type()
        if tournament == "t":
            play_tournament(moves, variant)
        else:
            player2 = create_opponent(moves, variant)
            game = Game(player1, player2, moves, variant)
            game.play_game()
        play = input(f"\n{player1.name}, would you like to play again? (y/n) ")
        play = play.lower()
        while play != "y" and play != "n" and play != "yes" and play != "no":
            play = input("I'm sorry I don't understand that input. \nPlease type y if you wish to play again or n if you would like to quit. ")
    print("Farewell!")
