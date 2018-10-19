# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from scipy import signal
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

"""Put two signals to one dataframe"""
corr_df = pd.DataFrame()
corr_df["Kinect"] = KinectOnAvg["LUX"]
corr_df["LUXmeter"] = LUXonAvg["LUX"]

""" Remove NaN """
corr_df = corr_df.dropna()

""" Find Delay using Cross Correlation
More detail: https://stackoverflow.com/questions/4688715/find-time-shift-between-two-similar-waveforms
"""
corr_df["Kinect"] = corr_df["Kinect"].astype(float)
corr_df["LUXmeter"] = corr_df["LUXmeter"].astype(float)
delay_index_kl = np.argmax(signal.correlate(corr_df["Kinect"],["LUXmeter"]))
delay_index_lk = np.argmax(signal.correlate(corr_df["LUXmeter"],["Kinect"]))
#delay_index_lk = np.argmax(signal.correlate(corr_df["LUXmeter"],["Kinect"]))-len(corr_df.index)
print(delay_index_kl)
print(delay_index_lk)

""" Shift Signal Time """


"""Normalization"""
x = corr_df["Kinect"].values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
corr_df["Kinect"] = x_scaled

x = corr_df["LUXmeter"] #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
corr_df["LUXmeter"] = x_scaled

"""Scatter Plot"""
corr_df.plot(kind='scatter',x='Kinect',y='LUXmeter')








