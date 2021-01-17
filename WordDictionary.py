import json     #To read data from json file
from difflib import get_close_matches #To get close matches

data = json.load(open("data.json"))

def wordLookup(x):
    if x in data:
        return data[x]
    elif x.title() in data:
        return(data[x.title()])  
    elif x.lower() in data:
        return(data[x.lower()])
    elif x.upper() in data:
        return(data[x.upper()])
    elif len(get_close_matches(x,data.keys())) > 0 :
        print("Did you mean %s, answer in Y or N " %get_close_matches(x, data.keys())[0])
        check = input("Answer as Y for yes or N for No \n")
        if (check =='Y'):
            return data[get_close_matches(x, data.keys())[0]]
        elif (check!='Y' or check!='N'):
            return  "Please enter a valid response, Y or N"
        else :
            return "No Such Word Exists"    
    else:
        return "No Such Word Exists"

word = input("Enter the word you want to lookup: \n")
#print(word.lower())
#print(word.title())
presentable_word = wordLookup(word) #calling the function
if type(presentable_word)==list:
    for d in presentable_word:
        print(d)        
else:
    print(presentable_word)
