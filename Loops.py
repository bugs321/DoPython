x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    print(str(i))
print("End of Loop")


y=["Apple","Orange","Mango","Pinapple","Pears","Guava","Grapes","WaterMellon"]
for i in y:
    print(str(i))
print("End of Loop")


#-----------------
#Add numbers sequentially until 0 base don user input

num = input("Enter a number ")
a = int(num)
b=a
for i in range(a, 0, -1) :
    b = b + (a - 1)
    a=a-1
print(f'Total is {b}.')    

