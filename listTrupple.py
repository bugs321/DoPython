#dir(list)
#'__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

x=["1",2, 1+2,"Test"]
print(x)
#operators are evaluated in list, in above example 2+2 was evaluated to 4

print(len(x))
print(x[-1])
print(x[1:3])
print(x[1:])
print(x[0]) #displayed with quotes

print(int(x[0])+x[1]) #example of casting
a = ['apple', 'banana', 'cherry']
b = ['Ford', 'BMW', 'Volvo']
a.append(b)
print(a)

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(0)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
x = fruits.insert(1, 'orange')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#----------------------------------------------------------
#Problem - arrange all number in increasing order
num = [1,4,3,2]
print(num)

num.sort() 
print(num)
num2=num
num2.sort(reverse=True)
print(num2)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)


#Truple
t = (1,2,3,'4','Time',1+4,'2'+'4','3+4')
print(t)