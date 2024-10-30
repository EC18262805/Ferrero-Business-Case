import re
import pandas as pd


FullFile = pd.read_csv('Retail_Sales_Data.csv')

test = FullFile.head(300)

products = []


for i in range(len(test)):

    phrase = str(test.description[i])
    
    x = re.search(r'\d+\s?[Gg]',phrase)
    
    x = x.group().lower().replace(" ","")
    
    nametext = re.split(' ',phrase)
    
    for i in range(len(nametext)):
        
        name = re.match(r'^[A-Z]+[a-z]+[A-Z]+[a-z]+',nametext[i])
        
        if name:
            
            break
    
    
    name = name.string
    
    if name == 'ChocoDelight':
        
        if x =='200g':
            name = name + ' ' + 'Dark'
            
        elif x =='350g':
            name = name + ' ' + 'White'     
            
            
            
    desciption  = (name + ' ' + x)
        
    products.append(desciption)
    
    

    
    
    
    
    
    


        