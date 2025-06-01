import random
card_num=['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
card_shape=['diamond','heart','spade','club']
deck=[]
s=''
deck_quantity=int(input("enter number of decks to be shuffled = "))
player_quantity=int(input("enter number of players in game = "))
card_quantity=int(input("enter number of cards to be dealt to each player = "))
if card_quantity*player_quantity>deck_quantity*52:
    print("You can't deal more cards than you have")
    exit()
for i in range(0,deck_quantity):#deck forming loop
    for j in range(0,13):
        for k in range(0,4):
            s=card_num[j]+' of '+card_shape[k]
            deck.append(s)
for i in range(player_quantity):
    print(f"cards of player number {i+1} =")
    for j in range(card_quantity):
        card=random.choice(deck)
        print(card)
        deck.remove(card)