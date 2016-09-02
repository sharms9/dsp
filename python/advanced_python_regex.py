#PYTHON CODE for Q1:
from collections import Counter
import pandas as pd
df = pd.read_csv('faculty.csv')
#print df
df.degree = df[df.columns[1]]
#print 'raw df.degree'
#print df.degree
df.degree = df.degree.apply(lambda d: d.strip().replace('.', ''))
df.degree_up = df.degree.apply(lambda d: d.upper())
#print 'periods, spaces removed and uppercased'
#print df.degree_up
df.deg = [x.split() for x in df.degree_up if x != '0']
collapse_dfdeg = [i for x in df.deg for i in x]
c = Counter(collapse_dfdeg)
print
print 'There are', len(df.degree), 'faculty members in the Biostats department.'
print
print 'The degree types and tally are:', c

#OUTPUT for Q1:
#(>>> runfile('/Users/swatisharma/Documents/find_degrees.py', wdir='/Users/swatisharma/Documents')
#
#There are 37 faculty members in the Biostats department.
#
#The degree types and tally are: Counter({'PHD': 31, 'SCD': 6, 'MPH': 2, 'MS': 2, 'MD': 1, 'MA': 1, 'BSED': 1, 'JD': 1})
