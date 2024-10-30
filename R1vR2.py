import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
R1vR2.py is part of Q1
Comparing the price of all the products by all competiors in Retail 1 and Retail2
Then producuing a scatter plot and line to show the trend in price over 104 weeks
The results are then shown as a plot
The best way to present this data is as a series of images (gif) to show the trend across products
'''


def AveragebyWeek(data,colum):
    
    yValues = []
    xpoints = np.array(range(1,104,1))

    for i in range(len(xpoints)):

        week = data[data["week"] == i+1]
        
        yValues.append(week.loc[:,colum].mean())
    
    '''
    name = data.iloc[0]['product']
    retailer = data.iloc[0]['retailer']
    
    plt.scatter(xpoints,yValues, c=yValues,cmap='Spectral')
    plt.ylim(0,20)
    
    plt.title(name + " Price " + retailer)
    plt.xlabel("Week")
    plt.ylabel("Price")

    plt.show()
    '''
    results = yValues
    return results

    
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    return a, b     

def RetailComparePrice(data1,data2,colum):
    
    
    
    DataAv_1 = AveragebyWeek(data1,colum)
    DataAv_2 = AveragebyWeek(data2,colum)
    
    xpoints = np.array(range(1,104,1))
    
    a1, b1 = best_fit(xpoints, DataAv_1)
    y1fit = [a1 + b1 * xi for xi in xpoints]
    plt.scatter(xpoints, DataAv_1, color = 'blue')
    plt.plot(xpoints,y1fit,color = 'blue',label='Retail 1')
    
    a2, b2 = best_fit(xpoints, DataAv_2)
    y2fit = [a2 + b2 * xi for xi in xpoints]
    plt.scatter(xpoints, DataAv_2, color = 'red')
    plt.plot(xpoints,y2fit,color = 'red',label='Retail 2')
    
    strcolum = colum.replace("_"," ")
    
    plt.title('Average price Comparison: ' + strcolum + '\n' + data1.iloc[0]['product'] )
    plt.xlabel('Weeks')
    plt.ylabel('Price')
    plt.ylim(8, 18) 
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    
def RetailComparePriceAll(data1,data2):
    
    column_headers = list(FullFile.columns.values)
    
    for i in range(5,16,1):
        RetailComparePrice(data1, data2,column_headers[i])

FullFile = pd.read_csv('Retail_Sales_Data.csv')


retail1 = FullFile.loc[FullFile.retailer=='retail1']
retail2 = FullFile.loc[FullFile.retailer=='retail2']

retail1Prods = dict(tuple(retail1.groupby('product')))
retail2Prods = dict(tuple(retail2.groupby('product')))

MintFresh_1 = retail1Prods.get("MintyFresh Mint 18g")
ChocDelight_D_1 = retail1Prods.get("ChocoDelight Dark 200g")
ChocDelight_W_1 = retail1Prods.get("ChocoDelight White 350g")
NuttyCream_1 = retail1Prods.get("NuttyCream Hazelnuts 80g")
DarkDream_1 = retail1Prods.get("DarkDream Dark 60g")

MintFresh_2 = retail2Prods.get("MintyFresh Mint 18g")
ChocDelight_D_2 = retail2Prods.get("ChocoDelight Dark 200g")
ChocDelight_W_2 = retail2Prods.get("ChocoDelight White 350g")
NuttyCream_2 = retail2Prods.get("NuttyCream Hazelnuts 80g")
DarkDream_2 = retail2Prods.get("DarkDream Dark 60g")

RetailComparePriceAll(MintFresh_1,MintFresh_2)
RetailComparePriceAll(ChocDelight_D_1,ChocDelight_D_2)
RetailComparePriceAll(ChocDelight_W_1,ChocDelight_W_2)
RetailComparePriceAll(NuttyCream_1,NuttyCream_2)
RetailComparePriceAll(DarkDream_1,DarkDream_2)
