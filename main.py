import pandas as pd
import matplotlib.pyplot as plt 
import plotData
import importData

def main():
    LUXfilePath = r"C:\Users\DSPLab\Research\ExperimentData\LightReflex\LUXmeter_lightON_avg.txt"
    KinectfilePath = r"C:\Users\DSPLab\Research\ExperimentData\LightReflex\Kinect_lightON_avg.txt"
    # KinectTestPath = r"C:\Users\DSPLab\Research\ExperimentData\kinectMeterTest.txt"
    # LUXmeterTestPath = r"C:\Users\DSPLab\Research\ExperimentData\luxMeterTest.txt"
    LUXdata_df = importData.importLUX(LUXfilePath)
    KinectData_df = importData.importKINECT(KinectfilePath)
    # KinectTest_df = importData.importKINECT(KinectTestPath)
    # LUXmeterTes_df = importData.importLUX(LUXmeterTestPath)
    """Print DataFrame"""
    print(LUXdata_df.head(5))
    print(KinectData_df.head(5))
    '''Check dtype of columns'''
    # print(LUXdata_df.dtypes)
    # print(KinectData_df.dtypes)

    # print(KinectTest_df.head(5))
    # print(LUXmeterTes_df.head(5))

    #plot
    plotData.plotLUXcompared(LUXdata_df,KinectData_df,'LightMeter','Kinect')
    # plotData.plotLUXcompared(LUXmeterTes_df,KinectTest_df,'LightMeter','Kinect')
    


if __name__ == "__main__":
    
    main()