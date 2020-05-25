import csv
import plotly.graph_objects as go
import plotly

import pprint

my_printer = pprint.PrettyPrinter()

entering_statistics = True # becomes false to end user input
stats_entered = [] # list of stats user has entered

reference_dictionary = {} # dict to reference which statistic is at which column #

columns_to_read = [] #will list all the cooresponding columns of input stats

years = [] # makes my x axis of years
data_wanted = {} # dict of all the data wanted, based on user input

trace_list = [] #list of traces to plot

file_name = 'professional_baseball.csv'

with open(file_name) as f:
    baseball_file = csv.reader(f, delimiter=',') 

    header = next(baseball_file)

    #build reference dictionary
    for x in range(0, len(header)):
        reference_dictionary[header[x]] = x

    #prompt user what to do

    print("Enter Offensive Baseball Statistical Category (ex: 2B, 3B, HR)")

    #read in user input, put it into list
    while entering_statistics:
        user_input = input("Enter Category, Press 'x' to Finish: ").upper()
        if(user_input != 'X'):
            stats_entered.append(user_input)
            print(stats_entered)
        else:
            entering_statistics = False
    
    #get cooresponding stats by using reference dictionary
    for stat in stats_entered:
        columns_to_read.append(reference_dictionary[stat])
    
   #build data_wanted. start my creating empty lists as values

    for x in range(0, len(columns_to_read)):
        data_wanted[stats_entered[x]] = list()
    
   #key is the stat category and value is a list of stats 
    for row in baseball_file:
        for x in range(0, len(columns_to_read)):
            data_wanted.get(stats_entered[x]).append(row[columns_to_read[x]])
        #creating a years list as my x axis
        #can't do it in a seperate for loop for some reason???
        years.append(row[0]) 
    

#filling trace_list with raw dictionaries with data_needed
for x in range(0, len(stats_entered)):
    trace_list.append({"x": years, 'y' : data_wanted.get(stats_entered[x]), 'name' : stats_entered[x]})


#changing strings to be part of title
title_text = str(stats_entered)
print(title_text)
title_text = title_text.replace('[', '')
title_text = title_text.replace(']', '')
title_text = title_text.replace('\'', '')

file_name = file_name.replace('.csv', '')
file_name = file_name.replace('_', ' ')
file_name = file_name.title()

#seting up title
layout = {'title': title_text + " Over Time - " + file_name}

#setting up data
figure = {'data': trace_list, 'layout': layout}

plotly.offline.plot(figure)
