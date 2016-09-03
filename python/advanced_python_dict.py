#PYTHON CODE for Q6:
import pandas as pd
import csv

df = pd.read_csv('faculty.csv')
faculty_dict={}
df.name = df[df.columns[0]]
df.name = df.name.apply(lambda x: x.split(' ')[-1])
faculty_dict = df.set_index('name').T.to_dict('list')

print
first3kv = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print first3kv

#OUTPUT for Q6:
>>> runfile('/Users/swatisharma/Documents/testdict.py', wdir='/Users/swatisharma/Documents')

{'Putt': [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'], 'Feng': [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'], 'Bilker': ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']}
_______________________________________
#PYTHON CODE for Q7:
import pandas as pd
import csv

df = pd.read_csv('faculty.csv')
faculty_dict={}
df.name = df[df.columns[0]]
df.lname = df.name.apply(lambda x: x.split(' ')[-1])
df.fname = df.name.apply(lambda x: x.split(' ')[0])
df.fl = df.fname + ', ' + df.lname
faculty_dict = df.set_index(df.fl).T.to_dict('list')

print
first3kv = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print first3kv

#OUTPUT for Q7:
>>> runfile('/Users/swatisharma/Documents/q7.py', wdir='/Users/swatisharma/Documents')

{'Sarah, Ratcliffe': ['Sarah Jane Ratcliffe', ' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu'], 'Yenchih, Hsu': ['Yenchih Hsu', ' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'], 'J., Landis': ['J. Richard Landis', ' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']}
__________________________________________
