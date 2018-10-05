import pandas as pd
import matplotlib.pyplot as plt

def importLUX(filePath):
    data_df = pd.read_csv(filePath,sep="\t",skiprows=1,header=None)
    # only select column 1 and 2
    data_df = data_df.iloc[:,1:3]
    # Add header manually
    data_df.columns = ["time","LUXlightMeter"]
    return data_df


def importKINECT(filePath):
    data_df = pd.read_csv(filePath,sep="\t",skiprows=1,header=None)   
    # Add header manually
    data_df.columns = ["time","LUXkinect"]
    return data_df
    
