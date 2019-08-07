#Author: Shiyan Zhang
import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
import os
from ggplot import *
import seaborn
os.chdir("C:\\GWU\\2016\\DataMining\\Project\\")
#%%
#I have four tables as my original data, I need to read them in and doing all kinds of data cleaning process bofore data visualization
MST = pd.read_excel("MspendTotal.xlsx")#MST stands for Military Spending Total
MSP = pd.read_excel("MspendPer.xlsx")#MSP stands for Military Spending Per Person
GDPT = pd.read_excel("GDPTotal.xlsx")#GDPT stands for GDP Total
GDPP = pd.read_excel("GDPPer.xlsx")#GDPP stands for GDP Per Person
#%%
#Only slect indentity column and 5 years
MST5 = MST[['Country',2006, 2007, 2008, 2009, 2010]]
MSP5 = MSP[['Country',2006, 2007, 2008, 2009, 2010]]
GDPT5 = GDPT[['Country',2006, 2007, 2008, 2009, 2010]]
GDPP5 = GDPP[['Country',2006, 2007, 2008, 2009, 2010]]
#%%
#change column names
MST5.columns = ['Country', 'MilitarySpending2006', 'MilitarySpending2007', 'MilitarySpending2008', 
                   'MilitarySpending2009', 'MilitarySpending2010']
MSP5.columns = ['Country', 'MSPer2006', 'MSPer2007', 'MSPer2008', 
                   'MSPer2009', 'MSPer2010']
GDPT5.columns = ['Country', 'NationGDP2006', 'NationGDP2007', 'NationGDP2008', 
                   'NationGDP2009', 'NationGDP2010']
GDPP5.columns = ['Country', 'PersonGDP2006', 'PersonGDP2007', 'PersonGDP2008', 
                   'PersonGDP2009', 'PersonGDP2010']
MST5s = MST5.sort('MilitarySpending2010', ascending=False)#Sort the total mili-spending by a year
MST5sh = MST5s.head(10)#Pick the top ten countries
#%%
#Format the Country variable to make it indentical throughout all the 4 dataframe
MST5sh['Country'] = [str(i).strip() for i in MST5sh['Country']]
MSP5['Country'] = [str(i).strip() for i in MSP5['Country']]
GDPT5['Country'] = [str(i).strip() for i in GDPT5['Country']]
GDPP5['Country'] = [str(i).strip() for i in GDPP5['Country']]
#%%
#Join the dataframes together
MSTP = MST5sh.merge(MSP5, on='Country', how='left')
MSTP_GDPT = MSTP.merge(GDPT5, on='Country', how='left')
AllinOne = MSTP_GDPT.merge(GDPP5, on='Country', how='left')
#%%
#Convert the wide table to long table, make only one column for one variable and save it
LongTable = pd.wide_to_long(AllinOne, ['MilitarySpending', 'MSPer', 'NationGDP', 'PersonGDP'], i='Country', j='year')
LongTable['NationGDP'] = LongTable['MilitarySpending'] / LongTable['NationGDP']
LongTable.to_csv('LongTable.csv')



