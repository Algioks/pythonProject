import random

ranks = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}
suits = ("Spades", "Hearts", "Diamonds", "Clubs")


class Card:
    def __init__(self, suit: str, rank: str):
        if suit not in suits:
            raise ValueError("incorrect suit received")

        if rank not in ranks:
            raise ValueError("incorrect rank received")
        self.suit = suit
        self.rank = rank
        self.points = ranks.get(rank)

    def __str__(self):
        return f"Card {self.rank} of {self.suit}. Points: {self.points}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        return f"Deck of {len(self.cards)} cards: {[str(card) for card in self.cards]}"

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"Player {self.name} has {[str(card) for card in self.hand]} and the score {self.get_points()}."

    def get_points(self) -> int:
        points = 0
        num_aces = 0
        for card in self.hand:
            points += card.points
            if card.rank == "Ace":
                num_aces += 1

        while points > 21 and num_aces > 0:
            points -= 10
            num_aces -= 1
        return points


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    nick = Player("Nick")
    dealer = Player("dealer")

    for _ in range(2):
        card = deck.deal()
        nick.hand.append(card)
        card = deck.deal()
        dealer.hand.append(card)

    game_over = False
    while not game_over:
        print(nick)
        action = input("Need one more card? (y/n)")

        if action == "y":
            new_card = deck.deal()
            nick.hand.append(new_card)
            nick_points = nick.get_points()
            if nick_points > 21:
                print(f"Nick lost! his score:{nick_points}")
                game_over = True
        else:
            while dealer.get_points() < 16:
                new_card = deck.deal()
                dealer.hand.append(new_card)

            if dealer.get_points() > 21 or dealer.get_points() < nick.get_points():
                print(f"Dealer lost! points: {dealer.get_points()}")
                game_over = True
            elif dealer.get_points() > nick.get_points():
                print(f"Dealer won!")
            elif dealer.get_points() == nick.get_points():
                print("it's a tie")
            else:
                raise Exception("unexpected scenario")