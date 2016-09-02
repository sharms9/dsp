#PYTHON CODE for Q1:
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
c = pd.value_counts(collapse_dfdeg)
print
print 'There are', len(df.degree), 'faculty members in the Biostats department.'
print
print 'The degree types and tally are:'
print c

#OUTPUT for Q1:
>>> runfile('/Users/swatisharma/Documents/q1.py', wdir='/Users/swatisharma/Documents')

There are 37 faculty members in the Biostats department.

The degree types and tally are:
PHD     31
SCD      6
MPH      2
MS       2
BSED     1
JD       1
MA       1
MD       1
dtype: int64
__________________________________

