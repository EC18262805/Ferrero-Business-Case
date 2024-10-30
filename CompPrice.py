import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')
    
    
def PriceCompareComp(data):
    
    regularMean = data.loc[:,'regular_price'].mean()
    compeditorsMean = []
    
    for i in range(6,16,1):
        column_headers = list(FullFile.columns.values)
        compeditorsMean.append(data.loc[:,column_headers[i]].mean())
    
    x = np.array(range (1,11,1))

    plt.scatter(x,compeditorsMean, color = 'red')
    plt.axhline(y = regularMean )

    for i in range (1,11,1):
        
        if (compeditorsMean[i-1] < regularMean):
            plt.plot([i,i],[compeditorsMean[i-1],regularMean],color = 'red',linestyle='dotted')
        else:
            plt.plot([i,i],[compeditorsMean[i-1],regularMean],color = 'green',linestyle='dotted')

    ymin, ymax = plt.ylim()    
    plt.ylim(ymin-0.005, ymax+0.005)
    
    roundMean = round(regularMean,2)
    Avrstr = str(roundMean)

    plt.title(data.iloc[0]['product'] + ' Avreage Price vs Comperitors\n' + 'Our Average = ' + Avrstr)
    plt.xlabel('Competiors')
    plt.ylabel('Price')
    plt.show()
    
    
FullFile = pd.read_csv('Retail_Sales_Data.csv')

retailProds = dict(tuple(FullFile.groupby('product')))

MintFresh = retailProds.get("MintyFresh Mint 18g")
ChocDark = retailProds.get("ChocoDelight Dark 200g")
ChocWhite = retailProds.get("ChocoDelight White 350g")
NuttyCream= retailProds.get("NuttyCream Hazelnuts 80g")
DarkDream = retailProds.get("DarkDream Dark 60g")

PriceCompareComp(MintFresh)
PriceCompareComp(ChocDark)
PriceCompareComp(ChocWhite)
PriceCompareComp(NuttyCream)
PriceCompareComp(DarkDream)



    
