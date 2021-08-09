from player import Player

def main():
    print(""" 
        Each player will has 2 cards, one of them is
        visible to the other player,
        each player calculate the summition of his/her cards,
        and palyer can pick a card until the total be more
        close to 21,
        for Ace it's two values (1/11) depending on
        its position at the game, by default it's 1
        but can be 11 if the total will be 21 or less,
    """)
    
    continue_playing = True
    human_finished_picking = False
    cpu_finished_picking = False
    
    cpu = Player('CPU')
    
    human_name = input('Please enter your name:\n')
    human = Player(human_name)
    
    print(f'You got {human.get_total()}, Your cards are:')
    for card in human.cards:
        print(f"{card.name}, {card.value} \n")
    
    while(continue_playing):
        while(not human_finished_picking):
            print(f'CPU has: {cpu.visible.name}, {cpu.visible.value} \n')
            
            new_pick = input('Would you like to pick a new card? \n(y for yes / anything for no):\n')
            if(new_pick.lower() == 'y' or new_pick.lower() == 'yes'):
                human.pick_card()
                print(f'Total cards: {human.get_total()}, Your cards are:')
                for card in human.cards:
                    print(f"{card.name}, {card.value} \n")
                if(human.get_total() > 21):
                    print(f'You got {human.get_total()} more than 21, You lose :(')
                    human_finished_picking = True
                    continue_playing = False
            else:
                human_finished_picking = True

        print('=============================================')
        
        while(not cpu_finished_picking):
            if(cpu.get_total() < 17):
                cpu.pick_card()
                if(cpu.get_total() > 21):
                    print(f'CPU got {cpu.get_total()} more than 21, You Won :)')
                    cpu_finished_picking = True
                    continue_playing = False
            else:
                cpu_finished_picking = True
                continue_playing = False

    if cpu.get_total() <= 21 and  human.get_total() <= 21:
        if cpu.get_total() > human.get_total():
            print(f'CPU got {cpu.get_total()}, and you got {human.get_total()}\n YOU LOSE :(')
        else:
            print(f'CPU got {cpu.get_total()}, and you got {human.get_total()}\n YOU WON :)')

    print('=============================================')
    print(f'Your cards: {human.get_total()}, as following:')
    for card in human.cards:
        print(f"{card.name}, {card.value} \t")
    print('=============================================')
    print(f'CPU cards: {cpu.get_total()}, as following:')
    for card in cpu.cards:
        print(f"{card.name}, {card.value} \t") 
        
main()