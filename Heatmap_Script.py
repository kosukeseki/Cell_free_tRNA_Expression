# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:04:53 2020

@author: Kosuke
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='Arial'
plt.rcParams['font.family']='sans-serif'
plt.rcParams['font.size'] = 7
plt.rcParams["figure.figsize"] = [2,2]


#copy dataframe structure from excel and import as 'data'
data = pd.read_clipboard()

ax = sns.heatmap(data, cmap = "GnBu", 
                 square = True,
                 cbar_kws={'label':'sfGFP ($\mu$g/mL)', 'shrink':0.6},
                 linewidths = 0.5, 
                 linecolor = 'black')
plt.xlabel('ng/$\mu$L PJL1-1TAG-sfGFP')
plt.ylabel('ng/$\mu$L tRNA Plasmid')
plt.tight_layout()
plt.savefig('Filename.pdf')