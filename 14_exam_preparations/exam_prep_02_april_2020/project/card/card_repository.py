from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            c = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        c = [cd for cd in self.cards if cd.name == card][0]
        self.cards.remove(c)
        self.count -= 1

    def find(self, name: str):
        c = [cd for cd in self.cards if cd.name == name][0]
        return c
