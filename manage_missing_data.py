import pandas as pd


# display no of missing values and percentage
def missing_data_display(df):
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending= False)
    return pd.concat([total,percent],axis= 1 ,keys=['Total','Percent'])

    
# delete columns where have more than 40% null values     
def delete_missing_values(df):
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending= False)
    df_percent = pd.concat([total,percent],axis= 1 ,keys=['Total','Percent'])
    indexs = df_percent[df_percent['Percent']>40].index
    df.drop(columns=list(indexs),inplace = True)

    
    
# fill null value by mean for numerical and unknown for categorical data  
def handle_missing_value(df):
    total = df.isnull().sum().sort_values(ascending = False)
    percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending= False)
    df_indexs = pd.concat([total,percent],axis= 1 ,keys=['Total','Percent'])
    features = df_indexs[df_indexs['Percent']>0].index
    for feature in features:
        if (df[feature].dtype) != 'object':
            #print(df[feature].dtype)
           # df[feature].fillna(df[feature].median(),inplace = True)
            if list(df[feature].unique()) ==[1]:
                df[feature].fillna(1,inplace = True)
            elif list(df[feature].unique()) ==[0]:   
                df[feature].fillna(0,inplace = True)
            elif list(df[feature].unique()) ==[1,0]:   
                df[feature].fillna(df[feature].median(),inplace = True)
            else:    
                df[feature].fillna(df[feature].median(),inplace = True)
        else:
            #print(df_app_train[feature].dtype)
            df[feature].fillna('unknown',inplace = True)
    #missing_data(df)        