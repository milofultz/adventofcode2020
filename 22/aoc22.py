from collections import deque
from copy import deepcopy
from time import time

P_IN = './aoc22-data'
P_INS = './aoc22-data-small'


def get_decks():
    """ Make both the decks from the input file """
    with open(P_IN, 'r') as f:
        raw_decks = f.read()

    deck_1, deck_2 = raw_decks.replace('Player 1:\n', '').split('\n\nPlayer 2:\n')
    deck_1 = [int(x) for x in deck_1.split('\n') if x != '']
    deck_2 = [int(x) for x in deck_2.split('\n') if x != '']
    return deque(deck_1), deque(deck_2)


def combat(deck_1, deck_2, recursive=False):
    """ Play the game and return winner plus their deck """
    history = []
    while len(deck_1) > 0 and len(deck_2) > 0:
        if has_been_played(deck_1, history):
            return 1, deck_1
        history.append(deepcopy(deck_1))
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()

        if recursive and len(deck_1) >= card_1 and len(deck_2) >= card_2:
            new_deck_1 = deepcopy(deck_1)
            new_deck_2 = deepcopy(deck_2)
            while len(new_deck_1) != card_1:
                new_deck_1.pop()
            while len(new_deck_2) != card_2:
                new_deck_2.pop()

            winner, _ = combat(new_deck_1, new_deck_2, recursive=True)
            if winner == 1:
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)
        elif card_1 > card_2:
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    winner = 1 if len(deck_1) != 0 else 2
    winning_deck = deck_1 if len(deck_1) != 0 else deck_2
    return winner, winning_deck


def has_been_played(deck_1, history):
    """ Check if the current hand has been played """
    for record in history:
        if record == deck_1:
            return True
    return False


def get_score(deck):
    """ Get the winner's deck score """
    total_score = 0
    while len(deck) != 0:
        top_card = deck.popleft()
        total_score += top_card * (len(deck) + 1)

    return total_score


def problem_1():
    deck_1, deck_2 = get_decks()
    _, winning_deck = combat(deck_1, deck_2)
    print(get_score(winning_deck))


def problem_2():
    deck_1, deck_2 = get_decks()
    _, winning_deck = combat(deck_1, deck_2, recursive=True)
    print(get_score(winning_deck))


if __name__ == "__main__":
    start_1 = time()
    problem_1()
    print(time() - start_1)
    start_2 = time()
    problem_2()
    print(time() - start_2)
