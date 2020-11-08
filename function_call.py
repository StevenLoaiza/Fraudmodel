# Custom functions for Data Science Challenge

def plt_hist(data,title,xlab,ylab,bins=50):
    '''
    Creates a Matplotlib histogram

            Parameters:
                    data : Pandas DataFrame
                    Title (string): Plot Title
                    xlab (string): plot y label
                    xlab (string): plot x label
                    bin (int): Argument for the histogram see matplotlib for more info

            Returns:
                    Inline Histogram plot
    '''
    
    import matplotlib.pyplot as plt
    
    #create histogram
    plt.hist(data,bins=bins)
    
    #labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    #options
    plt.grid(True)
    #display
    plt.show()
    
# Convert the transaction Date Time to Date only.
def dateconvert(df,column,newcolumn,format_="%Y-%m-%d",drop=True):
    '''
    Slices a DateTime feature into desired format

            Parameters:
                    df : Pandas DataFrame
                    column (string): Name of the DateTime Column
                    newcolumn (string): New Variable created name
                    format (string): String split format
                    Drop : Drop old column if True.
                    
            Returns:
                    New DataFrame with create column
    '''
    #libraries
    import dateutil
    import pandas as pd
    #parse each row into the wanted format
    tmp = [dateutil.parser.parse(x).strftime(format_) for x in df[column]]
    #create pandas DF
    tmp_df=pd.DataFrame(tmp)
    #rename column
    tmp_df.rename({0:newcolumn}, axis='columns',inplace=True)
    # concat original data set and new column
    new_df=pd.concat([df,tmp_df],axis=1)
    # drop old feature
    if drop==True:
        new_df.drop([column],axis=1,inplace=True)
    
    #return
    return(new_df)

# Create Dummy Variables
def dummy_trans(df,col_list,drop=True):
    '''
    Transforms categorical variables into (n-1) dummies

            Parameters:
                    df : Pandas DataFrame
                    col_list (string): List of string column names
                    Drop : Drop old column if True.
                    
            Returns:
                    New DataFrame with create column
    '''
    import pandas as pd
    #make a copy
    new_df=df
    #iterate over col list
    for col in col_list:
        #create dummy variables
        dummy=pd.get_dummies(df[col])
        #drop first dummy
        dummy.drop(dummy.columns[0], axis=1,inplace=True)
        #concat back to original
        new_df=pd.concat([new_df,dummy],axis=1)
    #drop original variables
    if drop==True:
        new_df.drop(col_list,axis=1)
    return(new_df)

# Label Encoder
class MultiColumnLabelEncoder:

    def __init__(self,columns = None):

        self.columns = columns # array of column names to encode

 

    def fit(self,X,y=None):

        return self # not relevant here

 

    def transform(self,X):

        '''

        Transforms columns of X specified in self.columns using

        LabelEncoder(). If no columns specified, transforms all

        columns in X.

        '''

        from sklearn.preprocessing import LabelEncoder

        le=LabelEncoder()

        output = X.copy()

        if self.columns is not None:

            for col in self.columns:
                output[col] = le.fit_transform(output[col])

        else:

            for colname,col in output.iteritems():

                output[colname] = le.fit_transform(col)

        return output

 

    def fit_transform(self,X,y=None):

        return self.fit(X,y).transform(X)

# Create an Percentage of transaction compared to the average per person
def Avg_transaction(df):
    '''
    Creates additional features for Train/Test Sets (transaction amount as a percent of the avg transactions)

            Parameters:
                    df : Pandas DataFrame
                    
            Returns:
                    New DataFrame with create column
    '''  
    
    # Grab the avg transaction for each account.customer
    avg_trans=df.groupby(['accountNumber','customerId'],as_index=False)['transactionAmount'].mean()
    #rename the column
    avg_trans.rename({'transactionAmount':'AvgTransaction'},axis='columns',inplace=True)
    
    #merge the avg trans back to the original df
    new_df=pd.merge(df,avg_trans,on=['accountNumber','customerId'])
    #create a new variable called which is the transaction amount as a percent of the avg transactions
    new_df['Perc_Avg']=new_df.transactionAmount/new_df.AvgTransaction
    new_df.loc[new_df.Perc_Avg.isnull()==True,['Perc_Avg']]=0
    new_df.drop(['AvgTransaction'],axis=1,inplace=True)
    #return df
    return(new_df)
