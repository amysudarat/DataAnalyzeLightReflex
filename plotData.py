import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use('seaborn')

def plotLUXcompared(df1,df2,legend1,legend2):
    #plot the data
    fig, axs = plt.subplots(2,1,sharex=True)
    ax = axs[0]
    ax.plot(df1['LUX'],'bo',df1['LUX'])  
    ax.grid(True)
    ax.set_title(legend1)
    ax = axs[1] 
    ax.plot(df2['LUX'],'ro',df2['LUX'])
    ax.grid(True)
    ax.set_title(legend2)

    plt.show()




