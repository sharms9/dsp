# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

>>> import datetime
>>> d1 = datetime.datetime(2013, 1, 2)
>>> d2 = datetime.datetime(2015, 7, 28)
>>> (d2-d1).days
937

####b)  
date_start = '12312013'  
date_stop = '05282015'  

>>> import datetime
>>> d1 = datetime.datetime(2013, 12, 31)
>>> d2 = datetime.datetime(2015, 5, 28)
>>> (d2-d1).days
513

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

>>> import datetime
>>> d1 = datetime.datetime(1994, 1, 15)
>>> d2 = datetime.datetime(2015, 7, 14)
>>> (d2-d1).days
7850
