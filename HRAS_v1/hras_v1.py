#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:53:21 2020

@author: kye
"""

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import sys
import json

from .sort import *

args = sys.argv

csv_file = args[1]
grph = args[2]
sort = args[3]
save = args[4]

def header(msg):
    header('H.R.A.S. - Household Relief Assistance System')

with open(csv_file, 'r', newline='') as csv_file:
    reader = csv.reader(line.replace('  ', ',') for line in csv_file)
    data = list(reader)


df = pd.DataFrame(data,
                  columns = ['HIN','Surname', 'First_name', 'Barangay', 
                             'District', 'Sex', 'Daily', 'Monthly', 
                             'Electricity', 'Water'])

colors = ['salmon','tomato','orangered','darkorange','orange','goldenrod'
          ,'gold','khaki','green','mediumaquamarine','turquoise','aqua','royalblue']

df['Daily'] = df['Daily'].astype(int)
df['Monthly'] = df['Monthly'].astype(int)
df['Electricity'] = df['Electricity'].astype(int)
df['Water'] = df['Water'].astype(int)

if  grph == "pie":
    if sort == "gen":
        sort.gen()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('plot.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "district":
        df_size = len(df[df['District'].isin(['Dalahican'])])
        df_size1 = len(df[df['District'].isin(['San Roque'])])
        df_size2 = len(df[df['District'].isin(['San Antonio'])])
        df_size3 = len(df[df['District'].isin(['Caridad'])])
        df_size4 = len(df[df['District'].isin(['Santa Cruz'])])
        dis_sizes = [df_size, df_size1, df_size2, df_size3, df_size4]
        dis_labels = ['Dalahican','San Roque', 'San Antonio', 'Caridad', 'Santa Cruz']
        explode = (0,0,0.2,0,0)
        plt.figure(figsize=(15,6))
        plt.pie(dis_sizes, explode=explode, labels=dis_labels, colors=colors,
        autopct='%1.0f%%', shadow=True, startangle=120, textprops={'size': 'xx-large'})
        plt.title('Household Relief Assistance System', fontsize=24)
        print('Dalahican: ', df_size,
              '\nSan Roque: ', df_size1,
              '\nSan Antonio: ', df_size2,
              '\nCaridad: ', df_size3,
              '\nSanta Cruz: ', df_size4)
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('plot.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "barangay":
        brgy = 0
        brgy_sizes = []
        brgy_labels = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_s = len(df[df['Barangay'].isin([bargy])])
            brgy_sizes.append(brgy_s)
            brgy_labels.append(bargy)
            print('Barangay ', brgy, ': ', brgy_s)
        explode = (0,0,0.2,0,0,0,0,0)
        plt.figure(figsize=(15,6))
        plt.pie(brgy_sizes, explode=explode, labels=brgy_labels, colors=colors,
        autopct='%1.0f%%', shadow=True, startangle=120, textprops={'size': 'xx-large'})
        plt.title('Household Relief Assistance System', fontsize=24)
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('plot.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "daily-b":
        brgy = 0
        brgy_labels = []
        Daily_min = []
        Daily_max = []
        Daily_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(bargy)
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Daily
            
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
                    
            Daily_min.append(con_min)
            Daily_max.append(con_max)
            Daily_mean.append(con_mean)
            print('Minimum Daily Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Daily Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Daily Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Daily_min, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Daily_max, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Daily_mean, labels=brgy_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS DAILY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
            
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Daily_brgy_pie.png')
        else:
            print('Error: Cannot Perform.')
        
        
    elif sort == "monthly-b":
        brgy = 0
        brgy_labels = []
        Monthly_min = []
        Monthly_max = []
        Monthly_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(bargy)
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Monthly
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Monthly_min.append(con_min)
            Monthly_max.append(con_max)
            Monthly_mean.append(con_mean)
            print('Minimum Monthly Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Monthly Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Monthly Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Monthly_min, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Monthly_max, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Monthly_mean, labels=brgy_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS MONTHLY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')

        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Monthly_brgy_pie.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "electric-b":
        brgy = 0
        brgy_labels = []
        Electricity_min = []
        Electricity_max = []
        Electricity_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(bargy)
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Electricity
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Electricity_min.append(con_min)
            Electricity_max.append(con_max)
            Electricity_mean.append(con_mean)
            print('Minimum Electricity Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Electricity Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Electricity Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Electricity_min, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Electricity_max, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Electricity_mean, labels=brgy_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS ELECTRICITY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Electric_brgy_pie.png')
        else:
            print('Error: Cannot Perform.')
    
        
    elif sort == "water-b":
        brgy = 0
        brgy_labels = []
        Water_min = []
        Water_max = []
        Water_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(bargy)
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Water
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Water_min.append(con_min)
            Water_max.append(con_max)
            Water_mean.append(con_mean)
            print('Minimum Water Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Water Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Water Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Water_min, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Water_max, labels=brgy_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Water_mean, labels=brgy_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS WATER EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('water_brgy_pie.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "daily-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Daily
        con_dis1 = con1.Daily
        con_dis2 = con2.Daily
        con_dis3 = con3.Daily
        con_dis4 = con4.Daily
        
        Daily_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Daily_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Daily_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Daily_min_d = [0 if math.isnan(i) else i for i in Daily_min_d]
        Daily_max_d = [0 if math.isnan(i) else i for i in Daily_max_d]
        Daily_mean_d = [0 if math.isnan(i) else i for i in Daily_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Daily Expense (District) :', Daily_min_d,
              '\nMaximum Daily Expense (District) :', Daily_max_d,
              '\nAverage Daily Expense (District) :', Daily_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Daily_min, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Daily_max, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Daily_mean, labels=dis_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS DAILY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Daily_dis_pie.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "monthly-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Monthly
        con_dis1 = con1.Monthly
        con_dis2 = con2.Monthly
        con_dis3 = con3.Monthly
        con_dis4 = con4.Monthly
        
        Monthly_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Monthly_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Monthly_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Monthly_min_d = [0 if math.isnan(i) else i for i in Monthly_min_d]
        Monthly_max_d = [0 if math.isnan(i) else i for i in Monthly_max_d]
        Monthly_mean_d = [0 if math.isnan(i) else i for i in Monthly_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Monthly Expense (District) :', Monthly_min_d,
              '\nMaximum Monthly Expense (District) :', Monthly_max_d,
              '\nAverage Monthly Expense (District) :', Monthly_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Monthly_min, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Monthly_max, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Monthly_mean, labels=dis_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS MONTHLY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Monthly_dis_pie.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "electric-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Electricity
        con_dis1 = con1.Electricity
        con_dis2 = con2.Electricity
        con_dis3 = con3.Electricity
        con_dis4 = con4.Electricity
        
        Electricity_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Electricity_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Electricity_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Electricity_min_d = [0 if math.isnan(i) else i for i in Electricity_min_d]
        Electricity_d = [0 if math.isnan(i) else i for i in Electricity_max_d]
        Electricity_mean_d = [0 if math.isnan(i) else i for i in Electricity_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Electricity Expense (District) :', Electricity_min_d,
              '\nMaximum Electricity Expense (District) :', Electricity_max_d,
              '\nAverage Electricity Expense (District) :', Electricity_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Electricity_min, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Electricity_max, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Electricity_mean, labels=dis_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS ELECTRICITY EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Electric_dis_pie.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "water-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Water
        con_dis1 = con1.Water
        con_dis2 = con2.Water
        con_dis3 = con3.Water
        con_dis4 = con4.Water
        
        Water_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Water_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Water_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Water_min_d = [0 if math.isnan(i) else i for i in Water_min_d]
        Water_d = [0 if math.isnan(i) else i for i in Water_max_d]
        Water_mean_d = [0 if math.isnan(i) else i for i in Water_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Water Expense (District) :', Water_min_d,
              '\nMaximum Water Expense (District) :', Water_max_d,
              '\nAverage Water Expense (District) :', Water_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(133)
        plt.pie(Water_min, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Minimum', fontsize=20, y=0.9)
        plt.axis('equal')        
        
        plt.subplot(132)
        plt.pie(Water_max, labels=dis_labels, colors=colors, 
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Maximum', fontsize=20, y=0.9)
        plt.axis('equal')
                
        plt.subplot(131)
        plt.pie(Water_mean, labels=dis_labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=120, radius=3, textprops={'size':'x-large'})
        plt.title('Average', fontsize=20, y=0.9)
        plt.suptitle('HRAS WATER EXPENSE OF BARANGAYS', fontsize=28)
        plt.axis('equal')
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Water_dis_pie.png')
        else:
            print('Error: Cannot Perform.')
    
    else: 
        print('Error: Cannot perform.')
        
elif grph == "cat":
    if sort == "daily-b":
        brgy = 0
        brgy_labels = []
        Daily_min = []
        Daily_max = []
        Daily_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Daily
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Daily_min.append(con_min)
            Daily_max.append(con_max)
            Daily_mean.append(con_mean)
            print('Minimum Daily Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Daily Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Daily Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(brgy_labels, Daily_min)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(brgy_labels, Daily_max)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(brgy_labels, Daily_mean)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS DAILY EXPENSE OF BARANGAYS', y=1)
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Daily_brgy_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "monthly-b":
        brgy = 0
        brgy_labels = []
        Monthly_min = []
        Monthly_max = []
        Monthly_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Monthly
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Monthly_min.append(con_min)
            Monthly_max.append(con_max)
            Monthly_mean.append(con_mean)
            print('Minimum Monthly Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Monthly Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Monthly Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(brgy_labels, Monthly_min)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(brgy_labels, Monthly_max)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(brgy_labels, Monthly_mean)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS MONTHLY EXPENSE OF BARANGAYS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Monthly_brgy_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "electric-b":
        brgy = 0
        brgy_labels = []
        Electricity_min = []
        Electricity_max = []
        Electricity_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Electricity
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Electricity_min.append(con_min)
            Electricity_max.append(con_max)
            Electricity_mean.append(con_mean)
            print('Minimum Electric Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Electric Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Electric Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(brgy_labels, Electricity_min)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(brgy_labels, Electricity_max)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(brgy_labels, Electricity_mean)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS ELECTRICITY EXPENSE OF BARANGAYS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Electric_brgy_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "water-b":
        brgy = 0
        brgy_labels = []
        Water_min = []
        Water_max = []
        Water_mean = []
        while (brgy < 8):
            brgy = brgy + 1    
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con = con_bargy.Water
            con_min = con.min()
            con_max = con.max()
            con_mean = con.mean()
            
            if str(con_min) == 'nan' or str(con_min) == 'inf':
                con_min = 0
            if str(con_max) == 'nan' or str(con_max) == 'inf':
                con_max = 0
            if str(con_mean) == 'nan' or str(con_mean) == 'inf':  
                con_mean = 0
            
            Water_min.append(con_min)
            Water_max.append(con_max)
            Water_mean.append(con_mean)
            print('Minimum Water Expense of Barangay ', brgy, ': ', con_min,
                  '\nMaximum Water Expense of Barangay ', brgy, ': ', con_max,
                  '\nAverage Water Expense of Barangay ', brgy, ': ', con_mean,'\n')
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(brgy_labels, Water_min)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(brgy_labels, Water_max)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(brgy_labels, Water_mean)
        plt.xlabel('Barangay')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS WATER EXPENSE OF BARANGAYS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Water_brgy_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "daily-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Daily
        con_dis1 = con1.Daily
        con_dis2 = con2.Daily
        con_dis3 = con3.Daily
        con_dis4 = con4.Daily
      
        
        Daily_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Daily_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Daily_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Daily_min_d = [0 if math.isnan(i) else i for i in Daily_min_d]
        Daily_max_d = [0 if math.isnan(i) else i for i in Daily_max_d]
        Daily_mean_d = [0 if math.isnan(i) else i for i in Daily_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Daily Expense (District) :', Daily_min_d,
              '\nMaximum Daily Expense (District) :', Daily_max_d,
              '\nAverage Daily Expense (District) :', Daily_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(dis_labels, Daily_min_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(dis_labels, Daily_max_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(dis_labels, Daily_mean_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS DAILY EXPENSE OF DISTRICTS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Daily_dis_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "monthly-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Monthly
        con_dis1 = con1.Monthly
        con_dis2 = con2.Monthly
        con_dis3 = con3.Monthly
        con_dis4 = con4.Monthly
      
        
        Monthly_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Monthly_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Monthly_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Monthly_min_d = [0 if math.isnan(i) else i for i in Monthly_min_d]
        Monthly_max_d = [0 if math.isnan(i) else i for i in Monthly_max_d]
        Monthly_mean_d = [0 if math.isnan(i) else i for i in Monthly_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Daily Expense (District) :', Monthly_min_d,
              '\nMaximum Daily Expense (District) :', Monthly_max_d,
              '\nAverage Daily Expense (District) :', Monthly_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(dis_labels, Monthly_min_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(dis_labels, Monthly_max_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(dis_labels, Monthly_mean_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS MONTHLY EXPENSE OF DISTRICTS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Monthly_dis_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "electric-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Electricity
        con_dis1 = con1.Electricity
        con_dis2 = con2.Electricity
        con_dis3 = con3.Electricity
        con_dis4 = con4.Electricity
      
        
        Electricity_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Electricity_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Electricity_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Electricity_min_d = [0 if math.isnan(i) else i for i in Electricity_min_d]
        Electricity_max_d = [0 if math.isnan(i) else i for i in Electricity_max_d]
        Electricity_mean_d = [0 if math.isnan(i) else i for i in Electricity_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Electricity Expense (District) :', Electricity_min_d,
              '\nMaximum Electricity Expense (District) :', Electricity_max_d,
              '\nAverage Electricity Expense (District) :', Electricity_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(dis_labels, Electricity_min_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(dis_labels, Electricity_max_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(133)
        plt.title('Average', fontsize=10)
        plt.plot(dis_labels, Electricity_mean_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS ELECTRICITY EXPENSE OF DISTRICTS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Electric_dis_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "water-d":
        dis_labels = ['Dalahican', 'San Roque', 'San Antonio', 'Santa Cruz', 'Caridad']
        con = df[df['District'].isin(['Dalahican'])]
        con1 = df[df['District'].isin(['San Roque'])]
        con2 = df[df['District'].isin(['San Antonio'])]
        con3 = df[df['District'].isin(['Santa Cruz'])]
        con4 = df[df['District'].isin(['Caridad'])]
        con_dis = con.Water
        con_dis1 = con1.Water
        con_dis2 = con2.Water
        con_dis3 = con3.Water
        con_dis4 = con4.Water
      
        
        Water_min_d = [con_dis.min(), con_dis1.min(), con_dis2.min(), con_dis3.min(), con_dis4.min()]
        Water_max_d = [con_dis.max(), con_dis1.max(), con_dis2.max(), con_dis3.max(), con_dis4.max()]
        Water_mean_d = [con_dis.mean(), con_dis1.mean(), con_dis2.mean(), con_dis3.mean(), con_dis4.mean()]
        
        Water_min_d = [0 if math.isnan(i) else i for i in Water_min_d]
        Water_max_d = [0 if math.isnan(i) else i for i in Water_max_d]
        Water_mean_d = [0 if math.isnan(i) else i for i in Water_mean_d]
        
        print('Districts:', dis_labels, 
              '\nMinimum Water Expense (District) :', Water_min_d,
              '\nMaximum Water Expense (District) :', Water_max_d,
              '\nAverage Water Expense (District) :', Water_mean_d)
        
        plt.figure(figsize=(15, 7))
        plt.subplot(131)
        plt.title('Minimum', fontsize=10)
        plt.bar(dis_labels, Water_min_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        
        plt.subplot(132)
        plt.title('Maximum', fontsize=10)
        plt.scatter(dis_labels, Water_max_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
    
        plt.subplot(133)
        plt.title('Average',fontsize=10)
        plt.plot(dis_labels, Water_mean_d)
        plt.xlabel('District')
        plt.ylabel('Expense (PHP)')
        plt.suptitle('HRAS WATER EXPENSE OF DISTRICTS')
        plt.tight_layout()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Water_dis_cat.png')
        else:
            print('Error: Cannot Perform.')
        
    else:
        print('Error: Cannot perform.')

elif grph == "table":
    if sort == "overall":
        if save == "display":
            print(df)
        elif save == "save":
            df.to_csv('HRAS_DataFrame.csv')
        else:
            print('Error: Cannot Perform.')
        
        
    elif sort == "stat-all":
        if save == "display":
            print(df.describe())
        elif save == "save":
            df_des = df.describe()
            df_des.to_csv('HRAS_stat_all.csv')
        else:
            print('Error: Cannot Perform.')
        
    
    elif sort == "stat-d":
        stat_d = df.query('District == "Dalahican"')
        stat_d1 = df.query('District == "Santa Cruz"')
        stat_d2 = df.query('District == "San Roque"')
        stat_d3 = df.query('District == "San Antonio"')
        stat_d4 = df.query('District == "Caridad"')
        
        stat_dis = stat_d.describe().fillna(0)
        stat_dis1 = stat_d1.describe().fillna(0)
        stat_dis2 = stat_d2.describe().fillna(0)
        stat_dis3 = stat_d3.describe().fillna(0)
        stat_dis4 = stat_d4.describe().fillna(0)
        
        stat = ('STAT SUMMARY OF DALAHICAN:\n', stat_dis, '\n', 
              '\nSTAT SUMMARY OF SANTA CRUZ:\n', stat_dis1, '\n',
              '\nSTAT SUMMARY OF SAN ROQUE:\n', stat_dis2, '\n',
              '\nSTAT SUMMARY OF SAN ANTONIO:\n', stat_dis3, '\n',
              '\nSTAT SUMMARY OF CARIDAD:\n', stat_dis4)
        if save == "display":
            print(stat)
        elif save == "save":
            stat.to_csv('HRAS_stat_dis.csv')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "stat-b":
        if save == "display":
            brgy = 0
            while (brgy < 8):
                brgy = brgy + 1    
                bargy = 'Barangay ' + str(brgy)
                con_bargy = df[df['Barangay'].isin([bargy])]
                stat_bargy = con_bargy.describe().fillna(0)
                print('STAT SUMMARY OF BARANGAY ', brgy,':\n', stat_bargy, '\n')
        elif save == "save":
            brgy = 0
            while (brgy < 8):
                brgy = brgy + 1    
                bargy = 'Barangay ' + str(brgy)
                con_bargy = df[df['Barangay'].isin([bargy])]
                stat_bargy = con_bargy.describe().fillna(0)
                stat = ('STAT SUMMARY OF BARANGAY ', brgy,':\n', stat_bargy, '\n')
                
                stat.to_csv('HRAS_stat_brgy.csv')
        else:
            print('Error: Cannot Perform.')
        
    else:
        print('Error: Cannot perform.')

elif grph == "bar-ver":
    if sort == "gen-all":
        n_groups = 1
        male_size = [len(df[df['Sex'].isin(['Male'])])]
        female_size = [len(df[df['Sex'].isin(['Female'])])]
        
        
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 5
        opacity = 1
        
        rects1 = plt.bar(index, male_size, bar_width,
                         alpha=opacity, color= 'mediumaquamarine', label='Male')
        rects2 = plt.bar(index + bar_width, female_size, bar_width,
                         alpha=opacity, color= 'salmon', label='Female')
        print('Male: ', male_size,
              '\nFemale: ', female_size)
        
        plt.xlabel('Cavite City')
        plt.ylabel('Population')
        plt.title('HRAS POPULATION BY GENDER')
        plt.xticks(index+2.5, (['Gender']))
        plt.tight_layout()
        plt.legend()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Gen_all_bar-ver.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "gen-perb":
        Male = []
        Female = []
        brgy_labels = []
        brgy = 0
        while (brgy < 8):
            brgy = brgy + 1
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con_fem = len(con_bargy.query('Sex == "Female"'))
            Female.append(con_fem)
            con_male = len(con_bargy.query('Sex == "Male"'))
            Male.append(con_male)
            print('No. of Male in ', bargy,':   ', con_male,
                  '\nNo. of Female in ', bargy, ': ', con_fem, '\n')
        n_groups = 8   
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.5
        opacity = 1
        
        rects1 = plt.bar(index, Male, bar_width,
                         alpha=opacity, color= 'mediumaquamarine', label='Male')
        rects2 = plt.bar(index + bar_width, Female, bar_width,
                         alpha=opacity, color= 'salmon', label='Female')
        
        plt.xlabel('Cavite City')
        plt.ylabel('Population')
        plt.title('HRAS POPULATION BY BARANGAY')
        plt.xticks(index, (brgy_labels))
        plt.tight_layout()
        plt.legend()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Gen_perbrgy_bar-ver.png')
        else:
            print('Error: Cannot Perform.')
            
    elif sort == "brgy-pop":
        brgy_labels = []
        pop_brgy = []
        brgy = 0
        while (brgy < 8):
            brgy = brgy + 1
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            pop_bargy = len(con_bargy)
            pop_brgy.append(pop_bargy)
            print('Population in ', bargy,':   ', pop_bargy,'\n')
        n_groups = 8   
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.5
        opacity = 1
        
        rects1 = plt.bar(index, pop_brgy, bar_width,
                         alpha=opacity, color='royalblue', label='Male')
        
        plt.xlabel('Cavite City')
        plt.ylabel('Population')
        plt.title('HRAS POPULATION BY BARANGAY')
        plt.xticks(index+1, (brgy_labels))
        plt.tight_layout()
        plt.legend()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Pop_brgy_bar-ver.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "district":
        pop_dis = (len(df[df['District'].isin(['Dalahican'])]))
        pop_dis1 = (len(df[df['District'].isin(['San Antonio'])]))
        pop_dis2 = (len(df[df['District'].isin(['Santa Cruz'])]))
        pop_dis3 = (len(df[df['District'].isin(['San Roque'])]))
        pop_dis4 = (len(df[df['District'].isin(['Caridad'])]))
        
        n_groups = 1 
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.5
        opacity = 1
        
        rects1 = plt.bar(index, pop_dis, bar_width,
                         alpha=opacity, color= 'mediumaquamarine', label='Dalahican')
        rects2 = plt.bar(index + bar_width, pop_dis1, bar_width,
                         alpha=opacity, color= 'salmon', label='San Antonio')
        rects3 = plt.bar(index + bar_width*2, pop_dis2, bar_width,
                         alpha=opacity, color= 'gold', label='Santa Cruz')
        rects4 = plt.bar(index + bar_width*3, pop_dis3, bar_width,
                         alpha=opacity, color= 'green', label='San Roque')
        rects5 = plt.bar(index + bar_width*4, pop_dis4, bar_width,
                         alpha=opacity, color= 'royalblue', label='Caridad')
        
        plt.xlabel('Cavite City')
        plt.ylabel('Population')
        plt.title('HRAS POPULATION BY DISTRICT')
        plt.xticks(index+1, (['Districts']), fontsize=8.8)
        plt.tight_layout()
        plt.legend()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('Pop_dis_bar-ver.png')
        else:
            print('Error: Cannot Perform.')
        
    elif sort == "barangay":
        brgy = 0
        while (brgy < 8):
            brgy = brgy + 1
            bargy = 'Barangay ' + str(brgy)
            brgy_labels.append(str(brgy))
            con_bargy = df[df['Barangay'].isin([bargy])]
            con_fem = len(con_bargy.query('Sex == "Female"'))
            Female.append(con_fem)
            con_male = len(con_bargy.query('Sex == "Male"'))
            Male.append(con_male)
        n_groups = 1  
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.5
        opacity = 1
        
        rects1 = plt.bar(index, pop_dis, bar_width,
                         alpha=opacity, color= 'mediumaquamarine', label='Dalahican')
        rects2 = plt.bar(index + bar_width, pop_dis1, bar_width,
                         alpha=opacity, color= 'salmon', label='San Antonio')
        rects3 = plt.bar(index + bar_width*2, pop_dis2, bar_width,
                         alpha=opacity, color= 'gold', label='Santa Cruz')
        rects4 = plt.bar(index + bar_width*3, pop_dis3, bar_width,
                         alpha=opacity, color= 'green', label='San Roque')
        rects5 = plt.bar(index + bar_width*4, pop_dis4, bar_width,
                         alpha=opacity, color= 'royalblue', label='Caridad')
        
        plt.xlabel('Cavite City')
        plt.ylabel('Population')
        plt.title('HRAS SYSTEM')
        plt.xticks(index + 1, (['Districts']))
        plt.tight_layout()
        plt.legend()
        
        if save == "display":
            plt.show()
        elif save == "save":
            plt.savefig('plot.png')
        else:
            print('Error: Cannot Perform.')
        
        
    else:
        print('Error: Cannot perform.')
        

else:
    print('Error: Cannot perform.')
        
        
       

