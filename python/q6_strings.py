# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError

#PYTHON CODE FOR donuts(count):
>>> def donuts(count):
...     if count >= 10:
...         print 'Number of donuts: many'
...     else:
...         print 'Number of donuts: ',count
... 
>>> donuts(4)
Number of donuts:  4
>>> donuts(9)
Number of donuts:  9
>>> donuts(10)
Number of donuts: many
>>> donuts(99)
Number of donuts: many
________________

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError
    
#PYTHON CODE FOR both_ends(s):    
>>> def both_ends(s):
...     if len(s) < 2:
...         print
...     else:
...         front = s[0:2]
...         end = s[-2:len(s)]
...         both = front + end
...         print both
... 
>>> both_ends('spring')
spng
>>> both_ends('Hello')
Helo
>>> both_ends('a')

>>> both_ends('xyz')
xyyz
>>>
_______________________

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError

#PYTHON CODE FOR fix_start(s):
>>> def fix_start(s):
...     first = 0
...     letter = s[first]
...     s1 = s[1:].replace(letter, '*') 
...     print letter + s1[:]
... 
>>> fix_start('babble')
ba**le
>>> fix_start('aardvark')
a*rdv*rk
>>> fix_start('google')
goo*le
>>> fix_start('donut')
donut
____________________


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError
    
#PYTHON CODE mix_up(a,b):
>>> def mix_up(a,b):
...     first = 0
...     second = 1
...     
...     aletters = a[first] + a[second]
...     bletters = b[first] + b[second]
...     
...     aleftover = a[2: ]
...     bleftover = b[2: ]
...     
...     a1 = a[ 0: 2].replace(aletters, bletters)
...     a11 = a1+aleftover
...     b1 = b[ 0:2 ].replace(bletters, aletters)
...     b11 = b1+bleftover
...     
...     ab = a11 + ' ' + b11
...     print ab
... 
>>> mix_up('mix', 'pod')
pox mid
>>> mix_up('dog', 'dinner')
dig donner
>>> mix_up('gnash', 'sport')
spash gnort
>>> mix_up('pezzy', 'firm')
fizzy perm
_____________________________

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError

#PYTHON CODE verbing(s):
>>> def verbing(s):
...     if len(s) > 2: 
...         if s[(-3): ] == 'ing':
...             s1 = s + 'ly'
...             print s1
...         else:
...             s1 = s + 'ing'
...             print s   
...     else:
...         s1 = s
...         print s1
... 
>>> verbing('hail')
hail
>>> verbing('swiming')
swimingly
>>> verbing('do')
do
__________________________________

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError

#PYTHON CODE FOR not_bad(s):
>>> def not_bad(s):
...     
...     index_not = s.find('not')
...     index_bad = s.find('bad')
...     
...     if index_bad > index_not:
...         s1 = s[ :index_not] + 'good' + s[index_bad+3: ]
...         print s1 
...     else:
...         s1 = s
...         print s1
... 
>>> not_bad('This movie is not so bad')
This movie is good
>>> not_bad('This dinner is not that bad!')
This dinner is good!
>>> not_bad('This tea is not hot')
This tea is not hot
>>> not_bad("It's bad yet not")
It's bad yet not
__________________________________________________

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
    
    #PYTHON CODE FOR front_back(a,b)
    >>> import math
>>> 
>>> def front_back(a,b):
...     
...     if (len(a)%2) == 0:
...         mid_a = len(a)/2
...         a_front = a[ :mid_a]
...         a_back = a[mid_a: ]
...         
...     else:
...         mid_a = int(math.ceil(len(a)/2.0))
...         a_front = a[ :mid_a]
...         a_back = a[mid_a: ]
...         
...     if (len(b)%2) == 0:
...         mid_b = len(b)/2
...         b_front = b[ :mid_b]
...         b_back = b[mid_b: ]
...         
...     else:
...         mid_b = int(math.ceil(len(b)/2.0))
...         b_front = b[ :mid_b]
...         b_back = b[mid_b: ]
...     
...     new_string = a_front + b_front + a_back + b_back
...     print(new_string)
... 
>>> front_back('abcd', 'xy')
abxcdy
>>> front_back('abcde', 'xyz')
abcxydez
>>> front_back('Kitten', 'Donut')
KitDontenut
