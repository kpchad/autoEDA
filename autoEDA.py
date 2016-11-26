#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:05:30 2016

@author: kylechadwick
"""

import pandas as pd

#load dataset
df = pd.read_csv('direct_marketing.csv')

#print feature names and describe each series
print(df.columns)
print(df.describe())

#print each features datatype
for i in df.columns:
    print('column ' + i + ' is of type:')
    print(df.ix[:,i].dtype)

