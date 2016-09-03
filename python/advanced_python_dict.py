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
