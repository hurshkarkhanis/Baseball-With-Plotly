import csv
import plotly.graph_objects as go
import plotly

years = [] # makes my x axis of years
stat_indexes = {} # dictionary so I know which stat is at which index of the header

so_list = [] #17th index
hits_list = [] #9th index


with open('baseball.csv') as baseball_file: # opens csv, doesnt read anything
    reader = csv.reader(baseball_file, delimiter=',') # actually reads it
    
    #build stat_indexes
    header = next(reader)
    for x in range (0, len(header)):
        stat_indexes[x] = header[x]
    
    for row in reader:
        years.append(row[0])
        if row[17] != '':  
            so_list.append(float(row[17])) #adding strikeout data to strikeout list
        else:
           so_list.append('')

        hits_list.append(float(row[9])) #adding hits data to hits list


#creating strikeout and hits traces with data
so_trace = {'x': years, 'y': so_list, 'name': "Strikeouts"}
hits_trace = {'x': years,'y': hits_list,  'name': "Hits"}

#title
layout = {'title': 'How Our Pasttime Has Changed | Big Swings Lead to an Increasingly Stagnant Game'}

figure = {'data': [so_trace, hits_trace], 'layout': layout}

plotly.offline.plot(figure)
