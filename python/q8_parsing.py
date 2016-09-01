# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd #need pandas for data structures
def difference(frame, gfor, gagainst, result): #function statement
    data = pd.read_csv(frame) #call the file
    difference = abs(data[gfor] - data[gagainst]) #take ABSOLUTE VALUE of difference of goals
    smallest = data[difference == difference.min()] #find minimum difference
    return smallest[result].values[0]
print
print 'Team =', difference('football.csv', 'Goals', 'Goals Allowed', 'Team')
>>> runfile('/Users/swatisharma/Documents/smallest_gap.py', wdir='/Users/swatisharma/Documents')

Team = Aston_Villa #NOTE: If I do not take the ABSOLUTE VALUE of the difference then the answer is Leicester, question asks to simply find smallest difference so that is why abs() is implemented


