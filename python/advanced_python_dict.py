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
#PYTHON CODE for Q8:
import pandas as pd
import csv


df = pd.read_csv('faculty.csv')
faculty_dict={}
fac_dict = {}
df.name = df[df.columns[0]]
df.lname = df.name.apply(lambda x: x.split(' ')[-1])
print
faculty_dict = df.set_index(df.lname).T.to_dict('list')
for key, value in sorted(faculty_dict.items()):
	print(key,value)
	
#OUTPUT for Q8:
>>> runfile('/Users/swatisharma/Documents/q8.py', wdir='/Users/swatisharma/Documents')

('Bellamy', ['Scarlett L. Bellamy', ' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu'])
('Bilker', ['Warren B. Bilker', 'Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'])
('Bryan', ['Matthew W Bryan', ' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu'])
('Chen', ['Jinbo Chen', ' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu'])
('Ellenberg', ['Jonas H. Ellenberg', ' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu'])
('Feng', ['Rui Feng', ' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu'])
('French', ['Benjamin C. French', ' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu'])
('Gimotty', ['Phyllis A. Gimotty', ' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu'])
('Guo', ['Wensheng Guo', ' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu'])
('Hsu', ['Yenchih Hsu', ' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'])
('Hubbard', ['Rebecca A Hubbard', ' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu'])
('Hwang', ['Wei-Ting Hwang', ' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu'])
('Joffe', ['Marshall M. Joffe', ' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu'])
('Landis', ['J. Richard Landis', ' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu'])
('Li', ['Hongzhe Li', ' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'])
('Localio', ['A. Russell Localio', ' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu'])
('Mitra', ['Nandita Mitra', ' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu'])
('Morales', ['Knashawn H. Morales', ' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu'])
('Propert', ['Kathleen Joy Propert', ' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu'])
('Putt', ['Mary E. Putt', ' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu'])
('Ratcliffe', ['Sarah Jane Ratcliffe', ' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu'])
('Ross', ['Michelle Elana Ross', ' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu'])
('Roy', ['Jason A. Roy', ' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu'])
('Sammel', ['Mary D. Sammel', ' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu'])
('Shaw', ['Pamela Ann Shaw', ' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu'])
('Shinohara', ['Russell Takeshi Shinohara', '0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu'])
('Shou', ['Haochang Shou', ' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu'])
('Shults', ['Justine Shults', ' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'])
('Stephens', ['Alisa Jane Stephens', ' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu'])
('Troxel', ['Andrea Beth Troxel', ' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu'])
('Xiao', ['Rui Xiao', ' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu'])
('Xie', ['Dawei Xie', ' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu'])
('Yang', ['Wei (Peter) Yang', ' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu'])
