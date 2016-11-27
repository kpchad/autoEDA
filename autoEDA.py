#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:05:30 2016

@author: kylechadwick
"""

import pandas as pd

#load dataset
df = pd.read_csv('Meteorite_Landings.csv')

#print feature names and describe each
print(df.columns)
print(df.describe())

#print details of each feature
for i in df.columns:
    print('column ' + i + ' is of type:', df.ix[:,i].dtype)
    print('number of nans in series:', sum(df.ix[:,i].isnull()))
    
#drop all rows with nans
df = df.dropna(axis=0).reset_index()

#replace all nans with zero
#df = df.fillna(0)


