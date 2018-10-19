# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
#import plotData
import importData

"""Import Data"""
LUXonAvg = importData.importLUX(r"Data\LUXmeter_lightON_avg.txt")
#LUXonMed = importData.importLUX(r"Data\LUXmeter_lightON_median.txt")
#LUXoffAvg = importData.importLUX(r"Data\LUXmeter_lightOFF_avg.txt")
#LUXoffMed = importData.importLUX(r"Data\LUXmeter_lightOFF_median.txt")
KinectOnAvg = importData.importKINECT(r"Data\Kinect_lightON_avg.txt")
#KinectOnMed = importData.importKINECT(r"Data\Kinect_lightON_median.txt")
#KinectOffAvg = importData.importKINECT(r"Data\Kinect_lightOFF_avg.txt")
#KinectOffMed = importData.importKINECT(r"Data\Kinect_lightOFF_median.txt")


"""Down sample to 1 second"""
#plotData.plotLUXcompared(LUXonAvg,KinectOnAvg,'LightMeter (Light ON, Average)','Kinect')
KinectOnAvg = KinectOnAvg.resample('1S').median()
#plotData.plotLUXcompared(LUXonAvg,KinectOnAvg,'LightMeter (Light ON, Average) Resampling','Kinect')

"""Normalization"""
x = KinectOnAvg.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
KinectOnAvg["LUX"] = x_scaled

x = LUXonAvg.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
LUXonAvg["LUX"] = x_scaled

#plt.scatter(KinectOnAvg,LUXonAvg)
