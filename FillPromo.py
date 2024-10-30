import pandas as pd
import numpy as np

def fillin(data,feild1,feild2):


    table1 = data.loc[:,feild1].to_list()
    table2 = data.loc[:,feild2].to_list()
    
    MeanRatio = []
    
    for i in range(len(table1)):
        x = table2[i]/table1[i]
        
        MeanRatio.insert(i,x)
        
    AMR = np.mean(MeanRatio)
    
    products = dict(tuple(FullFile.groupby('product')))
    UnFill= products.get(data['product'].iloc[0])
    
    testBi = UnFill.isna()
    
    for  index, row in testBi.iterrows():
            
        if testBi.loc[ index,feild2]==True:
                    
            UnFill.loc[index,feild2] = UnFill.loc[index,feild1]*AMR
            
        else:
            pass 
        
     
    return UnFill   
  
def FullFill(data):
    
    list1 = ['regular_price',
             'competition_1_regular_price',
             'competition_2_regular_price',
             'competition_3_regular_price',
             'competition_4_regular_price',
             'competition_5_regular_price',
             'competition_6_regular_price',
             'competition_7_regular_price',
             'competition_8_regular_price',
             'competition_9_regular_price',
             'competition_10_regular_price']
    
    list2 = ['promo_price',
             'competition_1_promo_price',
             'competition_2_promo_price',
             'competition_3_promo_price',
             'competition_4_promo_price',
             'competition_5_promo_price',
             'competition_6_promo_price',
             'competition_7_promo_price',
             'competition_8_promo_price',
             'competition_9_promo_price',
             'competition_10_promo_price']
    
    for i in range(len(list1)):
        
            fillin(data,list1[i],list2[i])
            
    return data
   
FullFile = pd.read_csv('Retail_Sales_Data.csv')



products = dict(tuple(FullFile.groupby('product')))

SMintFreshUn = products.get("MintyFresh Mint 18g")

MintFresh = products.get("MintyFresh Mint 18g").dropna()
ChocDelight_D = products.get("ChocoDelight Dark 200g").dropna()
ChocDelight_W = products.get("ChocoDelight White 350g").dropna()
NuttyCream = products.get("NuttyCream Hazelnuts 80g").dropna()
DarkDream = products.get("DarkDream Dark 60g").dropna()


FullMintFresh = FullFill(MintFresh)
FullChocDelight_D = FullFill(ChocDelight_D)
FullChocDelight_W = FullFill(ChocDelight_W)
FullNuttyCream = FullFill(NuttyCream)
FullDarkDream = FullFill(DarkDream)







