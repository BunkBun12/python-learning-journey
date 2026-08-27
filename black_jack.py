## black jack

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


play = input("do you want to play a game of Black Jack? Type 'y' or 'n' : ").lower()


if play == 'y' :


  balance = int(input("enter the amount to deposit :"))
  
  while balance > 0:

    print(f"current balance : {balance}")
    bet = int(input("enter the amount to gamble :"))

    while bet > balance or bet <= 0:
      print("Invalid bet!")
      bet = int(input("Enter a valid amount to gamble: "))

    # user ---------

    user_cards = [
      random.choice(cards),
      random.choice(cards)
    ]

    current_score = sum(user_cards)

    while current_score > 21 and 11 in user_cards:
      user_cards[user_cards.index(11)] = 1
      current_score = sum(user_cards)

    # dealer ------------

    dealer_first_card = random.choice(cards)

    dealer_cards = [
      dealer_first_card,random.choice(cards)
    ]

    dealer_score = sum(dealer_cards)  
    while dealer_score > 21 and 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
        dealer_score = sum(dealer_cards)

    

    print(r"""
  .------.            _     _            _    _            _    
  |A_  _ |.          | |   | |          | |  (_)          | |   
  |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
  | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
  |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
  '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
        |  \/ K|                            _/ |                
        '------'                           |__/           """)


    print(f"Your cards : {user_cards} , current score is {current_score}")
    print(f"Computer's first card : {dealer_first_card}")

    while current_score < 21:

      hit = input("Type 'y' to get another card (Hit), type 'n' to (Stand) : ").lower()
      if hit == 'y' :
        user_cards.append(random.choice(cards))

        current_score = sum(user_cards)

        if current_score > 21 and 11 in user_cards:
          user_cards[user_cards.index(11)] = 1
          current_score = sum(user_cards)

        print(f"Your cards : {user_cards} , current score is {current_score}")
        print(f"dealer's first card : {dealer_first_card}")


        if current_score > 21 :
          print("You went over 21! You loose")
          break

        elif current_score == 21 :
          print("BlackJack! You won")
          break

      elif hit == 'n':
        print("You stand!")
        break


    while dealer_score < 17 :

      dealer_cards.append(random.choice(cards))
      dealer_score = sum(dealer_cards)

      while dealer_score > 21 and 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
        dealer_score = sum(dealer_cards)

    print(f"Dealer cards : {dealer_cards}")
    print(f"Dealer score : {dealer_score}")


    if current_score > 21:

      print("\nYou busted! Dealer wins!")
      balance -= bet

    elif dealer_score > 21:

      print("\nDealer busted! You win!")
      balance += bet

    elif current_score > dealer_score:

      print("\nYou won!")
      balance += bet

    elif current_score < dealer_score:

      print("\nDealer won!")
      balance -= bet

    else:

      print("\nDraw! Push")

    # OUTSIDE the result conditions
    print(f"\nCurrent balance: {balance}")

    if balance <= 0:

      print("You are out of money! Game over.")
      break

    play_again = input(
      "Do you want to play another round? (y/n): "
    ).lower()

    if play_again != "y":

      print(f"\nThanks for playing! Final balance: {balance}")
      break

else :
  exit()