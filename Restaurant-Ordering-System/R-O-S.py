def menu():
    menu={"pizza":12.99,"burger":10.99,"fries":4.99,"combo-1":14.99,"combo-2":25.99}
    return menu
def order(menu1):
    bill=0
    s=0
    while s==0:
        item=input("enter exact item name to order:\n")
        if item in menu1:
            h=int(input(f"how many {item} do you want to order:\n"))
            for i in range(1,h+1,1):
                bill+=menu1[item]
            print(f"{h} {item}(s) added\n")
        else:
            print("invalid item")
        s=int(input("would you like to add another item to cart(enter 0)\nexit enter any other number:\n"))
    return bill
menu1=menu()
while True:
    n=int(input("choice:\n1.menu\n2.order\n3.exit\n"))
    match n:
        case 1:
            for key, value in menu1.items():
                print(key," -> ",value,"\n")
        case 2:
            print(f"final bill={order(menu1)}\n")
        case _:
            print(f"exiting.....\n")
            break
