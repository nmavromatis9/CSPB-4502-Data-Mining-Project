import pandas as pd 
import datetime
from scipy.stats import *
import matplotlib.pyplot as plt

#venv\Scripts\activate
#Note for hdd use: open Data folder in vs code
def main(): 
    print("hello World!")
    try:
        df = pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/bikeData.csv')
        #print(df)
    except:
        print("An exception occurred!!!")
      
    
    return 0
def preProcess():
    try:
        df = pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/bikeData.csv')
        #print(df)
    except:
        print("An exception occurred!!!")
    #Process df, adding season in.
    #make copy of df for safety.
    df2=df
    #put in standard datetime (pandas)
    #convert to season, splitting by date
    df2['Date']=df2['Date'].apply(pd.to_datetime)
    df2["Season"]=(df2['Date'].dt.month-1)//3
    df2["Season"] += (df['Date'].dt.month == 3)&(df['Date'].dt.day>=20)
    df2["Season"] += (df['Date'].dt.month == 6)&(df['Date'].dt.day>=21)
    df2["Season"] += (df['Date'].dt.month == 9)&(df['Date'].dt.day>=23)
    df2["Season"] -= 3*((df['Date'].dt.month == 12)&(df['Date'].dt.day>=21)).astype(int)
    df2.loc[df2["Season"]==0, 'Season']= "Winter"
    df2.loc[df2["Season"]==1, 'Season']= "Spring"
    df2.loc[df2["Season"]==2, 'Season']= "Summer"
    df2.loc[df2["Season"]==3, 'Season']= "Fall"
    #print(df2)
    df2.to_csv(r'C:/Users/shogu/Python_files/Data/Project/bikeData/bikeDataClean.csv', index=False)
    return 0
    
    return 0
def integrate():
    try:
        df = pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/Accidents.csv')
        df2 = pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/Bikers.csv')
        #print(df)
    except:
        print("An exception occurred!!!")
    
    df3=pd.merge(df, df2, on="Accident_Index")
    #print(df3)
    try:
        df3.to_csv(r'C:/Users/shogu/Python_files/Data/Project/bikeData/bikeData.csv', index=False)
    except:
        print("CSV output error")
        
def graph():
    df=pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/bikeDataClean.csv')
    arr1=df['Season']
    arr2=df.groupby(['Season'],as_index=False).sum()
    #print(arr2['Season'])
    plt.bar(arr2["Season"], arr2["Number_of_Casualties"])
    plt.show()
    
def stats():
    df=pd.read_csv('C:/Users/shogu/Python_files/Data/Project/bikeData/bikeDataClean.csv')
   #df.drop(df[df['Gender']=='Other'].index, inplace=True)
    contingency = pd.crosstab(df['Gender'], df['Severity'])
    print(contingency)
    c, p, dof, expected = chi2_contingency(contingency)
    print("p=" , p)
    print("EXPECTED= ", expected)
    print("C= ", c)
    #contingency2 = pd.crosstab(df['Light_conditions'], df['Number_of_Casualties'])
    #c2, p2, dof2, expected2 = chi2_contingency(contingency2)
    #print(contingency2)
    #print("p2= ", p2)
        
if __name__ == "__main__":
    main()
    #preProcess()
    #graph()
    stats()