import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd



# plot count and percentage between target and features 
def display_targetfeature(df,target,index,count_feature, horizantal = False):
    df_group = df.groupby([target,index])[count_feature].agg(['count']).reset_index()
    
    
    # sum of count as per target 
    total_paid = df_group[df_group[target]==0]['count'].sum()
    total_notpaid = df_group[df_group[target]==1]['count'].sum()
    
    

    # creat new feature for percent of count as per target 0 1
    df_group['percent_count'] = np.where(df_group[target]==0,round(df_group['count']/total_paid*100,2),round(df_group['count']/total_notpaid*100,2) )
    
    
    # plot bar feature with hue target 0 and 1
    fig , ax = plt.subplots(1,2 ,figsize = (27,6))
    
    if horizantal:
        # count 
        sns.barplot(x='count',y=index ,hue='TARGET',data = df_group,ax =ax[0],fontsize = 25 , 
                    label = " 0: repaid \n 1: notrepaid ")
        ax[0].set_title(" Counts %s with target(0,1) " %index)
    
        #percentage 
        sns.barplot(x='percent_count',y=index ,hue='TARGET',data = df_group,ax =ax[1],fontsize = 25,
                   label = " 0: repaid \n 1: notrepaid ")
        ax[1].set_title(" Percentage %s with target(0,1) " %index)
        
        plt.legend(loc ='best')
        
      
    
    
    else:
    
        # count 
        sns.barplot(x=index,y='count' ,hue='TARGET',data = df_group,ax =ax[0])
        ax[0].set_title(" Counts %s with target(0,1) " %index)
    
        #percentage 
        sns.barplot(x=index,y='percent_count' ,hue='TARGET',data = df_group,ax =ax[1])
        ax[1].set_title(" Percentage %s with target(0,1) " %index)
    
    
    fig.savefig("%s and target relationship.png" %index)
    plt.show()
    
    
    
    
# plot only count =between target and features     
    
def display_groupdata(df,target,index,count_feature, horizantal = False):
    df_group = df.groupby([target,index])[count_feature].count()
    flag = True
    for index_no,val in enumerate(df_group.index):
        if val[0]==1:
            if flag == True:
                total_notrepaid = df_group[df_group.index[index_no:]].sum()
                flag = False
            print(f" Percentage  {target} and  {index} { df_group.index[index_no]} : {TxtFormat().BOLD} { round(df_group[df_group.index[index_no]]/total_notrepaid*100,2)} %  {TxtFormat().END}")
        elif val[0]==0:
            
            total_repaid = df_group[df_group.index[index_no:]].sum()
              
            print(f" Percentage {target} and  {index} { df_group.index[index_no]} : {TxtFormat().BOLD} { round(df_group[df_group.index[index_no]]/total_repaid*100,2)} %  {TxtFormat().END}")
    
    print("\n")
    
    if horizantal:
        #df_group.plot(kind='barh',figsize=(12,6),label='0:repaid \n1: not repaid',colors = sns.color_palette())
        df_group.plot(kind='barh',figsize=(12,6),label='0:repaid \n1: not repaid')
        plt.title("Information with repaid or not_repaid")
        plt.legend(loc='best',fontsize = 15)
        plt.xlabel('No of Applicants')
        plt.ylabel('Type of Loan with target')
    
    else:
        #df_group.plot(kind='bar',figsize=(12,6),label='0:repaid \n1: not repaid',colors = sns.color_palette())
        df_group.plot(kind='bar',figsize=(12,6),label='0:repaid \n1: not repaid')
        plt.title("Information with repaid or not_repaid")
        plt.legend(loc='best',fontsize = 15)
        plt.xlabel('Type of Loan with target')
        plt.ylabel('No of Applicants')
    plt.show()    
    
    

    
# plot distribution of multiple features with target =1 / 0 on same graph
def plot_distribution_comp(df,list_features,n_row):
    i =0 
    
    # target repaid 0 and notrepaid 1
    t1 = df.loc[df['TARGET'] != 0 ]
    t0 = df.loc[df['TARGET'] == 0 ]
    
    
    #sns.set_style("whitegrid")
    fig,ax = plt.subplots(n_row,2,figsize =(12,6*n_row))
    
    for feature in list_features:
        i +=1
        plt.subplot(n_row,2,i)
        sns.kdeplot(t1[feature],bw =0.5,label = 'TARGET == 1')
        sns.kdeplot(t0[feature],bw =0.5,label = 'TARGET == 0')
        
        plt.ylabel("Density Plot" ,fontsize = 12)
        plt.xlabel(feature,fontsize  =12)
        locs,labels = plt.xticks()
        plt.tick_params(axis = 'both' ,which ='major' ,labelsize =12)
    plt.show()
    #fig.savefig("features_comp_.png" %index)
    

    
# plot of distribution of one features
def plot_distribution_onefeature(df,feature,color):
    plt.figure(figsize =(10,6))
    plt.title(f"Distribution of {feature}")
    sns.distplot(df[feature],color = color,kde = True ,bins =100)
    plt.show()