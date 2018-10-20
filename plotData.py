import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use('seaborn')

def plotLUXcompared(df1,df2,legend1,legend2):
    #plot the data
    fig, axs = plt.subplots(2,1,sharex=True)
    ax = axs[0]
    ax.plot(df1.iloc[:,0],'bo',df1.iloc[:,0])  
    ax.grid(True)
    ax.set_title(legend1)
    ax = axs[1] 
    ax.plot(df2.iloc[:,0],'ro',df2.iloc[:,0],)
    ax.grid(True)
    ax.set_title(legend2)

    plt.show()




