# -*- coding: utf-8 -*-
#"""
#Created on Tue Jan 28 17:43:59 2020

#@author: Jewett Lab
#"""

#first save this script in the folder that contains all of your raw data
import pandas as pd
import matplotlib.pyplot as plt
import glob

# we like arial fonts...
plt.rcParams['font.sans-serif']='Arial'
plt.rcParams['font.family']='sans-serif'
plt.rcParams.update({'font.size': 8})

# setting up figure parameters
plt.rcParams["figure.figsize"] = [1,0.5]
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

# get filenames. 
proteins = glob.glob('./*.xlsx')

#grab data from excel files
dict = {}
for x in proteins:
    dict[x] = pd.read_excel ('%s' %x, usecols = [1,2], skiprows = 1)

#peak finder settings and initialization.
#you can change the peak threshhold, which just means the script will 
#only look at peaks above a certain intensity
peaks = {}
peak_threshhold = 25000

count = 0
## setting up peak finder script
for y in proteins:
    slope = 0
    peaklist = []
    intensitylist = []
    for i in range (0, len(dict[y]) - 1):
        new_slope = (dict[y]['Y(Counts)'][i + 1] - dict[y]['Y(Counts)'][i]) / (dict[y]['X(Minutes)'][i + 1] - dict[y]['X(Minutes)'][i])
        ### my conditions for identifying a peak are if the slope value changes from + to -, indicating a maximum and if peak height > peak threshhold.
        if (dict[y]['Y(Counts)'][i] > peak_threshhold) and (new_slope < 0) and (slope > 0):
            peaklist.append(dict[y]['X(Minutes)'][i])
            intensitylist.append(dict[y]['Y(Counts)'][i])
        slope = new_slope
    tuple = (peaklist, intensitylist)
    peaks[y] = tuple
    
    ###ploting. using plt.figure() to clear plot for each loop
    name = y[2:-5]
    plt.figure()
    plt.plot(dict[y]['X(Minutes)'], dict[y]['Y(Counts)'], color = 'gray', linewidth = 0.5)
    plt.title(name)
    ####labelling peaks within the graph. 
    for x in range(0,len(peaks[y][0])):
        point = (peaks[y][0][x] + 0.2, peaks[y][1][x])
        plt.annotate('%.2f' %peaks[y][0][x], 
                      point, 
                      ha = 'left')
    plt.xlim(0.5,1.5)
    plt.ylim(0,1.1*max(dict[y]['Y(Counts)']))
    plt.xlabel('Time (min)')
    plt.ylabel('Ion Counts')
    plt.savefig('Filename' %name, bbox_inches = 'tight') 
    
    count = count + 1