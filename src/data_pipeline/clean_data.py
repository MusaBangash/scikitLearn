
import pandas as pd 
import os 
import sys 


RAW_DATA_PATH = "data/raw/HouseTS.csv" 
#PROCESSED_DATA_PATH = "data/processed/HouseTS_Clean.csv"


def main():

    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error:File not found  at {RAW_DATA_PATH}")
        return


df = pd.read_csv(RAW_DATA_PATH)
print(df.head())



if __name__ == "__main__":
    main()

