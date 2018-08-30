#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random

class Player:
    def move(self):
        #return 'rock'
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

class Rock (Player):
    def __init__(self):
        self.name = "Toph Beifong"

    def move(self):
        return 'rock'

class Random (Player):
    def __init__(self):
        self.name = "Random Frequent Flyer Dent"

    def move(self):
        return random.choice(moves)


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


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = valid_move(self.p1.move(), moves)
        move2 = valid_move(self.p2.move(), moves)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("Tie")
        elif beats(move1, move2):
            print("Player 1 wins!")
            return "player1"
        else:
            print("Player 2 wins!")
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
        print(f"Rounds complete! Final score is Player 1: {score['player1']} and Player 2: {score['player2']}.")


if __name__ == '__main__':
    game = Game(Random(), Rock())
    game.play_game()
