import random
print("===============================")
print("ROCK PAPER SCISSOR LIZARD SPOCK")
print("===============================")
print("\n1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")
print("\nEnter your choice (1-5):")
x = int(input())
c=random.randint(1, 5)
if x == c:
    print("result: draw")
elif x==1:
    print("player chose: ✊")
    if c==2:
        print("comp chose: ✋")
        print("result: comp wins")
    elif c==3:
        print("comp chose: ✌️")
        print("result: player wins")
    elif c==4:
        print("comp chose: 🦎")
        print("result: player wins")
    elif c==5:
        print("comp chose: 🖖")
        print("result: comp wins")
elif x==2:
    print("player chose: ✋")
    if c==1:
        print("comp chose: ✊")
        print("result: player wins")
    elif c==3:
        print("comp chose: ✌️")
        print("result: comp wins")
    elif c==4:
        print("comp chose: 🦎")
        print("result: comp wins")
    elif c==5:
        print("comp chose: 🖖")
        print("result: player wins")
elif x==3:
    print("player chose: ✌️")
    if c==1:
        print("comp chose: ✊")
        print("result: comp wins")
    elif c==2:
        print("comp chose: ✋")
        print("result: player wins")
    elif c==4:
        print("comp chose: 🦎")
        print("result: player wins")
    elif c==5:
        print("comp chose: 🖖")
        print("result: comp wins")
elif x==4:
    print("player chose: 🦎")
    if c==1:
        print("comp chose: ✊")
        print("result: comp wins")
    elif c==2:
        print("comp chose: ✋")
        print("result: player wins")
    elif c==3:
        print("comp chose: ✌️")
        print("result: comp wins")
    elif c==5:
        print("comp chose: 🖖")
        print("result: player wins")
elif x==5:
    print("player chose: 🖖")
    if c==1:
        print("comp chose: ✊")
        print("result: player wins")
    elif c==2:
        print("comp chose: ✋")
        print("result: comp wins")
    elif c==3:
        print("comp chose: ✌️")
        print("result: player wins")
    elif c==4:
        print("comp chose: 🦎")
        print("result: comp wins")
