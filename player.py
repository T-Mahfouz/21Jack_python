import random
from card import Card

import helper

class Player:
    
    def __init__(self, name):
        self.name = name
        
        self.cards = []
        self.aces_cards = []
        self.not_aces_cards = []
        self.total = 0
        self.initiate_cards()
        
    def initiate_cards(self):
        self.visible = self.get_random_card()
        
        self.cards.append(self.visible)
        self.cards.append(self.get_random_card())
    
    def get_random_card(self):
        rand = random.randrange(0, 12, 1)
        card = helper.get_cards_list()[rand]
        return Card(card['name'], card['value'])
            
    def pick_card(self):
        card = self.get_random_card()
        self.cards.append(card)
    
    def get_ace_cards(self):
        for card in self.cards:
            if card.name == 'Ace':
                self.aces_cards.append(card)
        return self.aces_cards
    
    def calculate_cards(self, cards):
        total = 0
        for card in cards:
            total += card.value
        return total
    
    def get_total(self):
        all_cards_total = self.calculate_cards(self.cards)
        ace_cards_total = self.calculate_cards(self.get_ace_cards())
        
        if ace_cards_total > 0 and all_cards_total <= 11:
           # ( calculate one of aces as 11 and remove its old value )
           self.total = all_cards_total + 10
        else:
            self.total = all_cards_total
        
        return self.total
