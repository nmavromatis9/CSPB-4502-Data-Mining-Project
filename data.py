import pandas as pd 
import dask.dataframe as dd

def main(): 
    print("hello World!")
    try:
        df = pd.read_csv('D:/DesktopCopy/dataProject/bike/Accidents.csv')
        print(df)
    except:
        print("An exception occurred")
    
    return 0

if __name__ == "__main__":
    main()
