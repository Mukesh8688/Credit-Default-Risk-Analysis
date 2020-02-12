import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
def plot_feature(model,df):
    n_features = df.shape[1]
    plt.figure(figsize=(25,20))
    plt.barh(range(len(sorted(model.feature_importances_,reverse =True)[:20])),
             sorted(model.feature_importances_,reverse =True)[:20],align='center')
    #plt.yticks(np.arange(n_features),df.columns.values)
    #plt.yticks(np.arange(len(sorted(model.feature_importances_,reverse =True)[:20])),df.columns.values)
    #plt.xlabel('Feature importance')
    #plt.ylabel('Feature')
    plt.show()
    
"""

#do code to support model
#"data" is the X dataframe and model is the SKlearn object
def plot_feature(model,df):
    feats = {} # a dict to hold feature_name: feature_importance
    for feature, importance in zip(df.columns, model.feature_importances_):
        feats[feature] = importance #add the name/value pair 

    importances = pd.DataFrame.from_dict(feats, orient='index').rename(columns={0: 'Gini-importance'})
    importances.sort_values(by='Gini-importance',ascending = False)[:15].plot(kind='barh',figsize =(12,6))