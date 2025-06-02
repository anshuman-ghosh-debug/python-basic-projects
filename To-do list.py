file=open("to-do.txt",'a')
d="TO-DO DAILY:-"
file.write(d)
print("enter daily tasks to be added")
while True:
    task=input("enter task =")
    file.write("\n-"+task)
    cont=input("do you want to add more tasks(y/n)?")
    if cont=="y":
       continue
    else:
       break
m=input("do you want to add reminder for goal to be completed(y/n)?")
if m=="y":
    while True:
        date = input("enter the goal deadline date (example-21st may)")
        file.write("\n"+f"GOALS TO BE COMPLETED BY {date}:-")
        while True:
            task = input("enter task =")
            file.write("\n-"+task)
            cont = input("do you want to add more tasks for given deadline(y/n)?")
            if cont == "y":
                continue
            else:
                break
        z=input("do you want to add more tasks for different deadlines(y/n)?")
        if z=="y":
            continue
        else:
            break
file.close()