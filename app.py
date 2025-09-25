import random 
user=[]
bot=[]
win=False
dealerstays=False
print("welcome to blackjack! You start with 2 cards, try to get as close to 21 as possible without going over.")
for i in range(2):
    user.append(random.randint(1,14))
    bot.append(random.randint(1,14))
if sum(user)>=21:
    print("your total is ",sum(user),"bot wins")
while sum(user)<21 and win==False:
    print("your cards:",user)
    print("dealer's cards:",bot)
    another_round=input("your total is "+str(sum(user))+", do you want another card? (y/n)")
    if another_round=="y":
        user.append(random.randint(1,14))
        print("your cards:",user)
    if sum(bot)<sum(user) and sum(bot)<16:
        print("dealer draws")
        bot.append(random.randint(1,14))
        print("dealer's cards:",bot)
    else: 
        print("dealer stays")
        dealerstays=True
    if another_round=="n" and dealerstays==True:
        if sum(user)>sum(bot):
            print("you win!")
            win=True
            break
        elif sum(user)<sum(bot):
            print("you lose!")
            win=True
            break
        elif sum(user)==sum(bot):
            print("it's a tie! go again")
            dealerstays=False
            another_round="y"
    if sum(user)>21:
        print("you lose!")
        break
    elif sum(bot)>21:
        print("you win!")
        win=True
        break
    elif sum(user)==21:
        print("you win!")
        win=True
        break
    elif sum(bot)==21:
        print("you lose!")
        break

