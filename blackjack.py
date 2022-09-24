import random
logo='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''
def blackjack():
  print(logo)
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  your_cards=[]
  n=1
  your_score=0
  computer_score=0
  while n<3:
    your_cards.append(random.choice(cards))
    your_score+=int(your_cards[n-1])
    if your_score==21:
      print(f"Your hand: {your_cards}, your score: {your_score}")
      print("You have won")
    elif your_score>21:
      your_score-=11
      for i in your_cards:
        your_cards[i]=1
        your_score+=1
    n+=1
  print(f"Your hand: {your_cards}, your score: {your_score}")
  computer_cards=[]
  m=1
  while m<3:
    computer_cards.append(random.choice(cards))
    computer_score+=int(computer_cards[m-1])
    if computer_score>21:
      computer_score-=11
      for i in computer_cards:
        computer_cards[i]=1
      computer_score+=1
    m+=1
  print(f"Computer's first card: {int(computer_cards[0])}")
  new_card=input("Type 'y' to get another card, type 'n' to pass: ")
  if your_score<17:
    new_card='y'
  while new_card=='y':
    your_cards.append(random.choice(cards))
    your_score+=int(your_cards[n-1])
    print(f"Your hand: {your_cards}, your score: {your_score}")
    if your_score>21:
      print(f"Your final hand: {your_cards}, final score: {your_score}")
      print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
      print("You have lost")
      next=input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
      if next=='y':
        blackjack()
      else:
        quit()
    new_card=input("Type 'y' to get another card, type 'n' to pass: ") 
  if new_card=="n":
    list=['y','n']
    cnew_card=random.choice(list)
    while cnew_card=='y':
      computer_cards.append(random.choice(cards))
      computer_score+=int(computer_cards[m-1])
      if computer_score>21:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You have won")
        next=input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if next=='y':
          blackjack()
        else:
          quit()
      cnew_card=random.choice(list)
      if computer_score<17:
        cnew_card='y'
    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    if  (computer_score<=21):
      if your_score>computer_score:
        print("You have won")
        next=input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if next=='y':
          blackjack()
        else:
          quit()
      elif your_score==computer_score:
        print("Draw")
        next=input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if next=='y':
          blackjack()
        else:
          quit()
      else:
        print("You have lost")
        next=input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        if next=='y':
          blackjack()
        else:
          quit()
blackjack()