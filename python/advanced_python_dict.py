#PYTHON CODE for Q6:
import pandas as pd
import csv

df = pd.read_csv('faculty.csv')
faculty_dict={}

faculty_dict = df.set_index('name').T.to_dict('list')

first3kv = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print first3kv

#OUTPUT for Q6:
>>> runfile('/Users/swatisharma/Documents/testdict.py', wdir='/Users/swatisharma/Documents')
{'Yimei Li': [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], 'Mingyao Li': [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu'], 'Jonas H. Ellenberg': [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu']}
_______________________________________________________

