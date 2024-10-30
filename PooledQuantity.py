import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import statsmodels.graphics.tsaplots as tsap



def createDF(data,text):
    
    x = []
    y = []
     
    for i in range(len(retail1weeks)):

        week = retail1weeks[i+1]
        
        x.append(week.loc[:,text].mean())
        y.append(week.loc[:,'quantity'].mean())
    
    dict = {'independent': x, 'dependent': y} 
    
    df = pd.DataFrame(dict)
        
    return df

def TestModel(data,independents):

    for i in range(len(independents)):
        
        trainData = createDF(train,independents[i])
        testData = createDF(test,independents[i])
    
        #define predictor and response variables
        X, y = trainData[["independent"]], testData.dependent
        
        pooled_X = sm.add_constant(X)
              
        #define predictor and response variables
        pooled_olsr_model = sm.OLS(endog=y, exog=pooled_X)
        
        #fit regression model
        pooled_olsr_model_results = pooled_olsr_model.fit()
        
        print('\n\n')
        print('Testing ' + independents[i] + ' as independent variable')
        
        print(pooled_olsr_model_results.summary())
        
        print('Mean value of residual errors='+str(pooled_olsr_model_results.resid.mean()))
        
        sm.qqplot(data=pooled_olsr_model_results.resid, line='45')
               
        fig, ax = plt.subplots()
        fig.suptitle('Raw residuals of Pooled OLS versus y')
        plt.ylabel('Residual (y - mu)')
        plt.xlabel('X = ' + independents[i])
        ax.scatter(y, pooled_olsr_model_results.resid, s=4, c='black', label='Residual Error')
        plt.show()
        
        print("////////////////////////////////////////////////////////////////////////////////////////")
        
        

FullFile = pd.read_csv('Retail_Sales_Data.csv')

msk = np.random.rand(len(FullFile)) < 0.8

train = FullFile[msk]
test = FullFile[~msk]

retail1 = train.loc[train.retailer=='retail1']
retail1weeks = dict(tuple(retail1.groupby('week')))

independents = ['value']

TestModel(retail1weeks,independents)


