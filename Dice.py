import random
x='Y'
while x=='Y':
    x = random.randint(1,6)
  #  print(x)
    if x==1:
        print(" -------------")
        print("|             |")
        print("|      0      |")
        print("|             |")
        print(" -------------")
    elif x==2:
        print(" -------------")
        print("|             |")
        print("|    0  0     |")
        print("|             |")
        print(" -------------")
    elif x==3:
        print(" -------------")
        print("|             |")
        print("|   0  0  0   |")
        print("|             |")
        print(" -------------")       
    elif x==4:
        print(" -------------")
        print("|   0     0   |")
        print("|             |")
        print("|   0     0   |")
        print(" -------------")
    elif x==5:
        print(" -------------")
        print("|    0   0    |")
        print("|      0      |")
        print("|    0   0    |")
        print(" -------------")   
    else:
        print(" -------------")
        print("|    0  0     |")
        print("|    0  0     |")
        print("|    0  0     |")
        print(" -------------")   

    y = input("Shall we roll again?! Y / N \n")
    if (y=='Y' or y=='y'):   
        x='Y'
    else: 
        x='N'


print ("Dice Destroyed!!!! eeehhha ha Ha Ha eeeHaaaahaaaa\n\n\n")