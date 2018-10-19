%% Import
clear
Kinect = importf_kinect('C:\Users\DSPLab\Research\DataAnalyzeLightReflex\Data\Kinect_lightON_avg.txt');
LUXmeter = importf_lux('C:\Users\DSPLab\Research\DataAnalyzeLightReflex\Data\LUXmeter_lightON_avg.txt');
%% Plot Before time compensating
% figure (1);
% subplot(2,1,1);plot(Kinect.DateTime,Kinect.Illumination);
% subplot(2,1,2);plot(LUXmeter.DateTime,LUXmeter.Illumination);

%% Find delay and synchronize time
% D = finddelay(Kinect{:,2},LUXmeter{:,2});  // -285
SynchronizeTable = synchronize(LUXmeter,Kinect,'regular','linear','TimeStep',seconds(1));


%% Plot After Shifting
% figure (1);
% subplot(2,1,1);plot(Kinect.DateTime,Kinect.Illumination);
% subplot(2,1,2);plot(LUXmeter.DateTime,LUXmeter.Illumination);