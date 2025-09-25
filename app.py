import random 
user=[]
bot=[]
win=False
dealerstays=False
print("welcome to blackjack!")
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
    if sum(bot)<sum(user) and sum(bot)<16:
        print("dealer draws")
        bot.append(random.randint(1,14))
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
        win=True
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
        win=True
        break
    bot.append(random.randint(1,14))
    another_round=input("your total is "+str(sum(user))+" do you want another card? (y/n)")