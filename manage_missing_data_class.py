import pandas as pd


class Managedata:
    
    def __init__(self, df):
        self.df = df
    
    def missing_data(self):

        total = self.df.isnull().sum().sort_values(ascending = False)
        percent = (self.df.isnull().sum()/self.df.isnull().count()*100).sort_values(ascending= False)
        return pd.concat([total,percent],axis= 1 ,keys=['Total','Percent'])
    
    #percent = (df_app_train.isnull().sum()/df_app_train.isnull().count()*100).sort_values(ascending = False)   
    def delete_missing_values(self):
        percent = missing_data(self.df)
        indexs = percent[percent['Percent']>40].index
        df.drop(columns=list(indexs),inplace = True)
        self.missing_data(self.df)
    # handling missing values 
    def handle_missing_value(self):
        indexs = missing_data(self.df)
        features = indexs[indexs['Percent']>0].index
        for feature in features:
            if (self.df[feature].dtype) != 'object':
               #print(df[feature].dtype)
               df[feature].fillna(df[feature].mean(),inplace = True)
            else:
                #print(df_app_train[feature].dtype)
                self.df[feature].fillna('unknown',inplace = True)
        self.missing_data(self.df)        