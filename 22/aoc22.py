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
    return deck_1, deck_2


def combat(deck_1, deck_2, recursive=False):
    """ Play the game and return winner plus their score """
    history = []
    while len(deck_1) > 0 and len(deck_2) > 0:
        if has_been_played(deck_1, history):
            return 1, deck_1
        history.append(deck_1[:])
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if recursive and len(deck_1) >= card_1 and len(deck_2) >= card_2:
            new_deck_1 = deck_1[:card_1]
            new_deck_2 = deck_2[:card_2]

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

    if len(deck_1) != 0:
        winner = 1
        winning_deck = deck_1
    else:
        winner = 2
        winning_deck = deck_2
    return winner, get_score(winning_deck)


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
        top_card = deck.pop(0)
        total_score += top_card * (len(deck) + 1)

    return total_score


def problem(recursive=False):
    start = time()
    deck_1, deck_2 = get_decks()
    winner, score = combat(deck_1, deck_2, recursive)
    print(f"Winner: {winner}\nScore: {score}")
    print(time() - start)


if __name__ == "__main__":
    # Problem 1
    problem()

    # Problem 2
    problem(recursive=True)
