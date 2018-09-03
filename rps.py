#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

std_moves = ['rock', 'paper', 'scissors']

rpsls = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

pokemon = ['Charmander', 'Bulbasaur', 'Squirtle']


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
    type = input("\nYou can play a single game of rock paper scissors or a  tournament. Let me know what you would prefer. \nType 'g' if you would like to play a single game or 't' if you would like to play a tournament. \n")
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


def tourney_round(players, wins, losses):
    winners = []
    losers = []
    while len(players) > 1:
        opponent1, opponent2 = choose_opponents(players)
        game = Game(opponent1, opponent2)
        winner, loser = game.play_game()
        winners.append(winner)
        losers.append(loser)
        losses[loser] += 1
        wins[winner] += 1
    if players:
        losers.append(players[0])
    return winners, losers


def elimination(losers, losses, eliminated):
    for loser in losers:
        if losses[loser] == 3:
            losers.pop(losers.index(loser))
            eliminated.append(loser)
            print(f"{loser.name} has been eliminated\n")

def play_tournament():
    player2 = Rock()
    player3 = Random()
    player4 = Cycle()
    player5 = Mimic()
    player6 = Strategic()
    wins = {player1 : 0, player2 : 0, player3 : 0, player4 : 0, player5 : 0, player6: 0}
    losses = {player1 : 0, player2 : 0, player3 : 0, player4 : 0, player5 : 0, player6: 0}
    players = [player1, player2, player3, player4, player5, player6]
    eliminated = []
    round = 1
    print(f"Tournament Begin:\nTourney Round {round}\n")
    winners, losers = tourney_round(players, wins, losses)
    round += 1
    while len(eliminated) < 5:
        elimination(losers, losses, eliminated)
        print(f"Tourney Round{round}\n")
        if len(winners) >= 2 and len(losers) >=2:
            winners1, losers1 = tourney_round(winners, wins, losses)
            winners2, losers2 = tourney_round(losers, wins, losses)
            winners = winners1 + winners2
            losers = losers1 + losers2
        else:
            players = winners + losers
            winners, losers = tourney_round(players, wins, losses)
        round +=1
    players = winners + losers
    winner = players[0]
    print(f"Tournament Over!\nWinner is {winner.name}! \n\nScores were:\n{player1.name}: {wins[player1]} wins and {losses[player1]} losses \n{player2.name}: {wins[player2]} wins and {losses[player2]} losses \n{player3.name}: {wins[player3]} wins and {losses[player3]} losses \n{player4.name}: {wins[player4]} wins and {losses[player4]} losses \n{player5.name}: {wins[player5]} wins and {losses[player5]} losses \n{player6.name}: {wins[player6]} wins and {losses[player6]} losses\n\n")


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
            print("Tie\n")
        elif beats(move1, move2):
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
