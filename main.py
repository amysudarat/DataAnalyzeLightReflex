import pandas as pd
import importData

def main():
    LUXfilePath = r"C:\Users\DSPLab\Research\ExperimentData\LightReflex\LuxMeter_roomLightON_avg.txt"
    KinectfilePath = r"C:\Users\DSPLab\Research\ExperimentData\LightReflex\Kinect_roomLightON_avg.txt"
    LUXdata_df = importData.importLUX(LUXfilePath)
    KinectData_df = importData.importKINECT(KinectfilePath)
    print(LUXdata_df.head(5))
    print(KinectData_df.head(5))

    #plot
    


if __name__ == "__main__":
    main()