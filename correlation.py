# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from scipy import signal
import plotData
import importData

"""Import Data"""
#LUXonAvg = importData.importLUX(r"Data\LUXmeter_lightON_avg.txt")
#LUXonMed = importData.importLUX(r"Data\LUXmeter_lightON_median.txt")
#LUXoffAvg = importData.importLUX(r"Data\LUXmeter_lightOFF_avg.txt")
#LUXoffMed = importData.importLUX(r"Data\LUXmeter_lightOFF_median.txt")
#KinectOnAvg = importData.importKINECT(r"Data\Kinect_lightON_avg.txt")
#KinectOnMed = importData.importKINECT(r"Data\Kinect_lightON_median.txt")
#KinectOffAvg = importData.importKINECT(r"Data\Kinect_lightOFF_avg.txt")
#KinectOffMed = importData.importKINECT(r"Data\Kinect_lightOFF_median.txt")
LUXonAvgLong = importData.importLUX(r"Data\LUXmeter_lightON_avg_200samples.txt")
KinectOnAvgLong = importData.importKINECT(r"Data\Kinect_lightON_avg_200samples.txt")

""" Plug-in the file you want to use here """
KinectOnAvg = KinectOnAvgLong
LUXonAvg = LUXonAvgLong

"""Down sample to 1 second"""
plotData.plotLUXcompared(LUXonAvg,KinectOnAvg,'LightMeter (Light ON, Average)','Kinect')
KinectOnAvg = KinectOnAvg.resample('1S').median()
plotData.plotLUXcompared(LUXonAvg,KinectOnAvg,'LightMeter (Light ON, Average) Resampling','Kinect')

"""Put two signals to one dataframe"""
corr_df = pd.DataFrame()
corr_df["Kinect"] = KinectOnAvg["LUX"]
corr_df["LUXmeter"] = LUXonAvg["LUX"]
#corr_df= corr_df.assign(account=corr_df.index).reset_index(drop=True)
#corr_df = corr_df.drop(columns=['account'])

""" Find Delay using Cross Correlation
More detail: https://stackoverflow.com/questions/4688715/find-time-shift-between-two-similar-waveforms
"""

# Find delay by performing cross correlation (with NaN)
delay_index_kl = np.argmax(signal.correlate(corr_df["Kinect"],corr_df["LUXmeter"]))-len(corr_df)-1
delay_index_lk = np.argmax(signal.correlate(corr_df["LUXmeter"],corr_df["Kinect"]))-len(corr_df)-1
print("delay kl,lk (with NaN)")
print(delay_index_kl)
print(delay_index_lk)
# Drop NaN
corr_df_dropna = corr_df.dropna()
# Find delay by performing cross correlation (without NaN)
delay_index_kl_dropna = np.argmax(signal.correlate(corr_df_dropna["Kinect"],corr_df_dropna["LUXmeter"]))-len(corr_df_dropna)-1
delay_index_lk_dropna = np.argmax(signal.correlate(corr_df_dropna["LUXmeter"],corr_df_dropna["Kinect"]))-len(corr_df_dropna)-1
print("delay kl,lk (without NaN)")
print(delay_index_kl_dropna)
print(delay_index_lk_dropna)

""" Shift Signal Time """ 
# with NaN
k = corr_df.drop(columns=['LUXmeter'])
l = corr_df.drop(columns=['Kinect'])
plotData.plotLUXcompared(l,k,'plot corr_df before shifting (with NaN)','Kinect')
k = k.shift(periods=delay_index_lk)
#plotData.plotLUXcompared(l,k,'after shifting kinect shift (with NaN)','Kinect')
k['LUXmeter'] = l['LUXmeter']
k = k.dropna()
plotData.plotLUXcompared(k.drop(columns=['Kinect']),k.drop(columns=['LUXmeter']),'plot corr_df before shifting (Full signal)','Kinect')

# without NaN
k_dropna = corr_df_dropna.drop(columns=['LUXmeter'])
l_dropna = corr_df_dropna.drop(columns=['Kinect'])
#plotData.plotLUXcompared(l_dropna,k_dropna,'plot corr_df before shifting (without NaN)','Kinect')
k_dropna = k_dropna.shift(periods=delay_index_lk_dropna)
#plotData.plotLUXcompared(l_dropna,k_dropna,'plot corr_df before shifting (without NaN)','Kinect')
k_dropna['LUXmeter'] = l_dropna['LUXmeter']
k_dropna = k_dropna.dropna()
#plotData.plotLUXcompared(k_dropna.drop(columns=['Kinect']),k_dropna.drop(columns=['LUXmeter']),'plot corr_df before shifting (without NaN)','Kinect')

""" Find Linear correlation Pearson """ 
# with NaN
corr = k.corr(method='pearson', min_periods=1)
m,b = np.polyfit(k_dropna['Kinect'],k_dropna['LUXmeter'],1)
strOut = "m = %d , b = %d"%(m,b)
print(strOut)
#fit = np.polyfit(k_dropna['Kinect'],k_dropna['LUXmeter'],1)
#fit_fn = np.poly1d(fit)

# without NaN
corr_dropna = k_dropna.corr(method='pearson', min_periods=1)
print("Correlation full signal")
print(corr)
print("Correlation drop NaN")
print(corr_dropna)
#plt.scatter(k_dropna['Kinect'],k_dropna['LUXmeter'],c='blue')
plt.scatter(k['Kinect'],k['LUXmeter'],c='red')
plt.plot(k['Kinect'],(m*k['Kinect'])+b,'k')
#plt.plot(k['Kinect'],(fit_fn(k['Kinect'])),'k')


#"""Normalization"""
#x = corr_df["Kinect"].values #returns a numpy array
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#corr_df["Kinect"] = x_scaled
#
#x = corr_df["LUXmeter"] #returns a numpy array
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(x)
#corr_df["LUXmeter"] = x_scaled










