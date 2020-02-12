import seaborn as sns
import matplotlib.pyplot as plt

# Function for displaying correlation between  target feature and other features 
def target_corrs(df):
    
    # list of correlations
    corrs=[]
    
    # iteration on columns
    for col in df.columns:
        #print(col)
        
        #skip target feature 
        if col != 'TARGET':
            corr = df['TARGET'].corr(df[col])
            
            # append all corr
            corrs.append((col,corr))
            
    corrs = sorted(corrs , key = lambda x : abs(x[1]),reverse = True)
    
    
    return corrs




# kde plot target and features
def Kde_target(var_name,df):
    # calculate corr with target
    corr= df['TARGET'].corr(df[var_name])
    
    #calculate median of previous loan counts with target 0 and 1
    
    avg_repaid = df.loc[df['TARGET']==0,var_name].median()
    avg_not_repaid = df.loc[df['TARGET']==1,var_name].median()
    
    
    plt.figure(figsize = (12,6))
    
    
    # plot Kde 
    
    sns.kdeplot(df.loc[df['TARGET']==0,var_name],label='TARGET = 0')
    
    sns.kdeplot(df.loc[df['TARGET']==1,var_name],label='TARGET = 1')
    
    plt.xlabel(var_name)
    plt.ylabel('Density')
    plt.title('%s Distribution' % var_name)
    plt.legend()
    
    # print Corr
    print("The correlation between %s and the TARGET is %0.4f" % (var_name,corr))
    
    # print average value
    print('Median value for loan that was not repaid = %0.4f' %avg_not_repaid)
    print('Median value for loan that was repaid = %0.4f' %avg_repaid)