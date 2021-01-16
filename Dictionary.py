#some playing with strings again
x='Water'
x=x.replace('t', 'a')
print(x.count('aa'))
 
#Dictionary - Not sure why its named like this
#dir("Dict")
#'__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

tab = { "Name": 'Naveen' , "LastName": 'Nainegali' , "Age": 33 , "BirthYear": 1988 }
#tab={"Test" : True}
print(tab)
print(tab["Name"])
tab.pop("BirthYear")
print(tab)
#
#tab1= {key: [i.upper() for i in tab[key] ]  for key in tab }
#print(tab1)

# initializing dictionary 
test_dict = {"Gfg" : ["ab", "cd", "ef"], 
             "Best" : ["gh", "ij"], "is" : ["kl"]} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# using upper to convert to upper case  
res = {key: [ele.upper() for ele in test_dict[key] ] for key in test_dict } 
  
# printing result  
print("The dictionary after conversion " + str(res))  