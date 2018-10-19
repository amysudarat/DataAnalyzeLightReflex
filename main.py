import pandas as pd
import matplotlib.pyplot as plt 
import plotData
import importData

"""Import Data"""
LUXonAvg = importData.importLUX(r"Data\LUXmeter_lightON_avg.txt")
LUXonMed = importData.importLUX(r"Data\LUXmeter_lightON_median.txt")
LUXoffAvg = importData.importLUX(r"Data\LUXmeter_lightOFF_avg.txt")
LUXoffMed = importData.importLUX(r"Data\LUXmeter_lightOFF_median.txt")
KinectOnAvg = importData.importKINECT(r"Data\Kinect_lightON_avg.txt")
KinectOnMed = importData.importKINECT(r"Data\Kinect_lightON_median.txt")
KinectOffAvg = importData.importKINECT(r"Data\Kinect_lightOFF_avg.txt")
KinectOffMed = importData.importKINECT(r"Data\Kinect_lightOFF_median.txt")


"""Print DataFrame"""
#print(LUXdata_df.head(5))
#print(KinectData_df.head(5))

'''Check dtype of columns'''
# print(LUXdata_df.dtypes)
# print(KinectData_df.dtypes)
# print(KinectTest_df.head(5))
# print(LUXmeterTes_df.head(5))

""" Plot Data """
plotData.plotLUXcompared(LUXonAvg,KinectOnAvg,'LightMeter (Light ON, Average)','Kinect')
plotData.plotLUXcompared(LUXonMed,KinectOnMed,'LightMeter (Light ON, Median)','Kinect')
plotData.plotLUXcompared(LUXoffAvg,KinectOffAvg,'LightMeter (Light OFF, Average)','Kinect')
plotData.plotLUXcompared(LUXoffMed,KinectOffMed,'LightMeter (Light OFF, Median)','Kinect')

    


