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

#PYTHON CODE for Q2:
import pandas as pd
df = pd.read_csv('faculty.csv')

df.title = df[df.columns[2]]

df.title = df.title.apply(lambda d: d.strip().replace('is', 'of'))
c =pd.value_counts(df.title)
print
print 'There are', len(df.title), 'professors in the Biostats department.'
print
print 'The title types and tally are:'
print
print c

#OUTPUT for Q2:
>>> runfile('/Users/swatisharma/Documents/find_titles.py', wdir='/Users/swatisharma/Documents')

There are 37 professors in the Biostats department.

The title types and tally are:

Professor of Biostatoftics              13
Assoftant Professor of Biostatoftics    12
Associate Professor of Biostatoftics    12
Name:  title, dtype: int64
____________________________________________
#PYTHON CODE for Q3
import pandas as pd
df = pd.read_csv('faculty.csv')
print
print 'There are', len(df), 'professors in the Biostats department.'
print 'Below is a list of their email addresses.'
print
df.emails = df[df.columns[3]]
print df.emails

#OUTPUT for Q3:
>>> runfile('/Users/swatisharma/Documents/find_emails.py', wdir='/Users/swatisharma/Documents')

There are 37 professors in the Biostats department.
Below is a list of their email addresses.

0     bellamys@mail.med.upenn.edu
1                warren@upenn.edu
2               bryanma@upenn.edu
3              jinboche@upenn.edu
4              sellenbe@upenn.edu
5     jellenbe@mail.med.upenn.edu
6               ruifeng@upenn.edu
7     bcfrench@mail.med.upenn.edu
8              pgimotty@upenn.edu
9         wguo@mail.med.upenn.edu
10        hsu9@mail.med.upenn.edu
11       rhubb@mail.med.upenn.edu
12      whwang@mail.med.upenn.edu
13      mjoffe@mail.med.upenn.edu
14    jrlandis@mail.med.upenn.edu
15            liy3@email.chop.edu
16     mingyao@mail.med.upenn.edu
17              hongzhe@upenn.edu
18             rlocalio@upenn.edu
19    nanditam@mail.med.upenn.edu
20    knashawn@mail.med.upenn.edu
21     propert@mail.med.upenn.edu
22       mputt@mail.med.upenn.edu
23             sratclif@upenn.edu
24             michross@upenn.edu
25       jaroy@mail.med.upenn.edu
26     msammel@cceb.med.upenn.edu
27                shawp@upenn.edu
28        rshi@mail.med.upenn.edu
29       hshou@mail.med.upenn.edu
30     jshults@mail.med.upenn.edu
31    alisaste@mail.med.upenn.edu
32     atroxel@mail.med.upenn.edu
33       rxiao@mail.med.upenn.edu
34        sxie@mail.med.upenn.edu
35                 dxie@upenn.edu
36     weiyang@mail.med.upenn.edu
Name:  email, dtype: object
__________________________________

#PYTHON CODE for Q4
import pandas as pd
df = pd.read_csv('faculty.csv')
print
print 'There are', len(df), 'professors in the Biostats department.'
print 'Below is a list of the different email domains.'
print
df.emails = df[df.columns[3]]
#print df.emails
email_domains = map(lambda x: x.split('@')[-1], df.emails)
#remove email up to @ and keep domain
c =pd.value_counts(email_domains)
print c

#OUTPUT for Q4:
>>> runfile('/Users/swatisharma/Documents/email_domains.py', wdir='/Users/swatisharma/Documents')

There are 37 professors in the Biostats department.
Below is a list of the different email domains.

mail.med.upenn.edu    23
upenn.edu             12
cceb.med.upenn.edu     1
email.chop.edu         1
dtype: int64
_____________________________


