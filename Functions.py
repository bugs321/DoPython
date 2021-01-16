#alternate to function, if done manually
x=input("Write 1st val: \n")
y=input("Write 2nd val: \n")
if (x.isnumeric() & y.isnumeric()):
    print(int(x)+int(y))
else:
    print("You did not enter numbers Dude! What should I add ? You Deserve an Error : ") 
    #raise Exception("Invalid Input Provided, You Suck!")

print("This should Print all the time")

#---------------------
def add(x,y):
    a = int(x) + int(y)
    return a

print (add(x,y))

#----------------------

def tempConvert(x):
    x=int(x)
    y=(9/5)*x+32
    return y
a = input("Enter temperature in Degree celcius! \n")
print('The temperature in degree celcium %s when converted to farenheit will be %s',a,tempConvert(a))
