import pandas as pd 
import dask.dataframe as dd

def main(): 
    print("hello World!")
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
    return 0

if __name__ == "__main__":
    main()
