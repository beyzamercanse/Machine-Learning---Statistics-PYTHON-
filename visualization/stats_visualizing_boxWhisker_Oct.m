%%
%   
% 
%  SECTION: Visualizing data
%  Box-and-whisker plots

%

%%

% a clear MATLAB workspace is a clear mental workspace
close all; clear
pkg load statistics % load Octave stats package

%% create data for the plot

% data sizes
m = 30; % rows
n =  6; % columns

% generate data
data = bsxfun(@times,30*randn(m,n),linspace(-1,1,n).^2);
data = bsxfun(@plus,data,(1:n).^2);

%% show it!

figure(1), clf

boxplot(data)

boxplot(data)
set(gca,'xtick',1:6,'xticklabel',{'one';'two';'three';'four';'five';'six'})

%% alternative: data in a single column, grouped by a separate variable

dataVect = data(:);
dataGrouping = ceil(linspace(eps,n,m*n));

figure(2), clf
boxplot(dataVect,dataGrouping,'notch','on','labels',{'one';'two';'three';'four';'five';'six'})

% for horizontal orientation
%boxplot(dataVect,dataGrouping,'notch','on','labels',{'one';'two';'three';'four';'five';'six'},'orientation','horizontal')

%% done.
