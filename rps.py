#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

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
    def __init__(self):
        self.name = "Toph Beifong"

    def move(self):
        return 'rock'

class Random(Player):
    def __init__(self):
        self.name = "Random Frequent Flyer Dent"

    def move(self):
        return random.choice(moves)

class Cycle(Player):
    def __init__(self):
        self.name = random.choice(["Agrajag", "Aang", "Korra", "Dave Lister", "Jane"])
        self.prev_move = 'scissors'

    def move(self):
        index = (moves.index(self.prev_move) + 1) % len(moves)
        return moves[index]

    def learn(self, my_move, their_move):
        self.prev_move = my_move

class Mimic(Player):
    def __init__(self):
        self.name = random.choice(["Raven Darkhölme", "Braling Two", "Stephen Byerley"])
        self.opponent_move = 'scissors'

    def move(self):
        return self.opponent_move

    def learn(self, my_move, their_move):
        self.opponent_move = their_move

class Strategic(Player):
    def __init__(self):
        self.name = random.choice(["Harbinger", "Jeeves", "SCORPIO"])
        self.losing_move = random.choice(moves)

    def move(self):
        return self.losing_move

    def learn(self, my_move, their_move):
        if my_move == their_move:
            self.losing_move = random.choice(moves)
        elif beats(my_move, their_move):
            self.losing_move = their_move
        else:
            self.losing_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def valid_move(move, moves):
    move = move.lower()
    while move not in moves:
        move = input(f"{move}? That doesn't make sense. Pick a new move: ")
        move = move.lower()
    return move


def game_type():
    type = input("You can play a single game of rock paper scissors or a  tournament. Let me know what you would prefer. \nType 'g' if you would like to play a single game or 't' if you would like to play a tournament. \n")
    while type.lower() != 'g' and type.lower() != 't':
        type = input("I'm afraid your response was invalid. \n Please type 'g' to play a single game or 't' if you would prefer a tournament. \n")
    return type


def game_variant():
    pass


def create_opponent():
    opponent_type = random.choice(['rock', 'random', 'cycle', 'mimic', 'strategic'])#put the list here since rubric said do not use global variables except for moves. Let me know if I should move the list of player subclasses to a global variable
    if type == 'rock':
        return Rock()
    elif type == 'random':
        return Random()
    elif type == 'cycle':
        return Cycle()
    elif type == 'mimic':
        return Mimic()
    else:
        return Strategic()


def choose_opponents(players):
    p1 = random.choice(players)
    players.pop(players.index(p1))
    p2 = random.choice(players)
    players.pop(players.index(p2))
    return p1, p2


def play_tournament():
    player2 = Rock()
    player3 = Random()
    player4 = Cycle()
    player5 = Mimic()
    player6 = Strategic()
    players = [player1, player2, player3, player4, player5, player6]
    print("Tournament Begin:\n")
    round = 1
    while len(players) > 1:
        opponent1, opponent2 = choose_opponents(players)
        print(players)
        game = Game(opponent1, opponent2)
        print(f"Game {round}\n")
        winner = game.play_game()
        players.append(winner)
        round += 1
    print(f"Tournament Over!\nWinner is {winner.name}")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.name1 = p1.name
        self.p2 = p2
        self.name2 = p2.name

    def play_round(self):
        move1 = valid_move(self.p1.move(), moves)
        move2 = valid_move(self.p2.move(), moves)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"{self.name1}: {move1}  {self.name2}: {move2}")
        if move1 == move2:
            print("Tie")
        elif beats(move1, move2):
            print(f"{self.name1} wins!")
            return "player1"
        else:
            print(f"{self.name2} wins!")
            return "player2"

    def tiebreaker(self, score):
        print("Score is tied. Entering tiebreaker round to determine winner.")
        while score['player1'] == score['player2']:
            self.keep_score(score)

    def keep_score(self, score):
        winner = self.play_round()
        if winner != None:
            score[winner] = score[winner] + 1

    def play_game(self):
        score = {"player1" : 0, "player2" : 0}
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.keep_score(score)
        if score['player1'] == score['player2']:
            self.tiebreaker(score)
        if score['player1'] > score['player2']:
            winner = self.p1
            winner_name = self.name1
        else:
            winner = self.p2
            winner_name = self.name2
        print(f"Rounds complete! \nFinal score is {self.name1} {score['player1']} and {self.name2}: {score['player2']}. \nThe winner is {winner_name}!")
        return winner


if __name__ == '__main__':
    player1 = Human()
    play = "y"
    while play == "y" or play == "yes":
        tournament = game_type()
        if tournament == "t":
            play_tournament()
        else:
            player2 = create_opponent()
            game = Game(player1, player2)
            game.play_game()
        play = input(f"\n{player1.name}, would you like to play again? (y/n) ")
        play = play.lower()
        while play != "y" and play != "n" and play != "yes" and play != "no":
            play = input("I'm sorry I don't understand that input. \nPlease type y if you wish to play again or n if you would like to quit. ")
    print("Farewell!")
