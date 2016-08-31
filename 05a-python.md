# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A list is a sequence of values.  The values can be of any type.  Also lists are mutable - they can be altered.  A tuple is also a sequence of values, and these values can be of any type.  The main difference between lists and tuples is that tuples are immutable, whereas lists are mutable.  Tuples cannot be changed.  It is common to use tuples as keys in dictionaries because they are immutable (strings also).  Lists cannot be used as keys in dictionaries.  Dictionaries have a method called items that returns a list of tuples - where each tuple is a key-value pair.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an unordered collection of unique elements.  Lists are ordered collections of elements (duplicates are acceptable).  Sets do not allow indexing are utilize hash tables.  Lists are variable length arrays and the values are accessed by indices.  An example of a set:  I need a set of all eyecolors of Metis Bootcamp students.  An example of a list:  I need a list of phone numbers for each Metis Bootcamp student.  Some sort of order must be maintained in order to access each student's phone number.  Hashing allows high performance where large amounts of data is stored and must be accessed quickly. Each value in a set has a memory position allocated.  The memory position is refered to by its hash value.  Hash values do not change during the lifetime of the set.  Lists are not hashable and values are accessed by indices.  In order to find a value in a set, one would need to go one by one to find that value.  This is time consuming if the list contains large amounts of data.  Python will jump to the memory location and retrieve the value when using a set.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is a one-statement function that returns something.  For example there is a tuple:


    tups = [(1,3,-2), (3,2,1), (-1,0,4), (0,-1,3), (-2,6,-5)]
    
    
  I would like to sort this tuple.  This is done by:
  
  
    sorted(tups)
    
    
  The output is:
  
  
    [(-2, 6, -5), (-1, 0, 4), (0, -1, 3), (1, 3, -2), (3, 2, 1)]
    
    
  The tuple is sorted by the first value.  If I would like to sort by the second value, I need to use key to define a function.
  
  
    def sortkey(tup):
    
...     return tup[1]

... 
    sorted(tups, key = sortkey)
    
    
  The output is:
  
  
    [(0, -1, 3), (-1, 0, 4), (3, 2, 1), (1, 3, -2), (-2, 6, -5)]
    
    
  The tuple is sorted by the second value.  To simplify this process and to save lines and memory, the lambda function is utilized.
  
  
    sorted(tups, key = lambda tup:tup[1])
    
    
  The output is:
  
  
    [(0, -1, 3), (-1, 0, 4), (3, 2, 1), (1, 3, -2), (-2, 6, -5)]
    

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a way to create lists.  Typical applications are to make new lists where each element is the result of some operations applied to each member of another sequence.

>>> squares = [ ]

>>> for x in range (10):

>>>     squares.append(x**2)

 

>>> squares

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> 

>>> # using a list comprehension:

 

>>> squares = [x**2 for x in range (10)]

>>> squares

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

A list comprehension consists of brackets containing an expression followed by for or if.  This results in a new list from evaluating the expression in the brackets.  The map function applies a function to every member of an iterable and returns the result.

>>> def square(x):

>>>     return x**2
>>>

>>> squares = map(square, range(10))

>>> print squares

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Lambda and map can be used together.

>>> squares = map(lambda x:x**2, range(10))

>>> print squares

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Filter takes a function returning True or False and applies it to a sequence.  A list of members for which the function returned True are returned in the list.  Lambda can also be used with the filter function.  We will filter the list of squares according to wheter the entries are >5 and <50.

>>> squares = map(lambda x:x**2, range(10))

>>> special_squares = filter(lambda x:x>5 and x<50, squares)

>>> print special_squares

[9, 16, 25, 36, 49]

Set comprehensions have similar syntax as list comprehensions and consist of values

>>> a_set = set(range(10))

>>> a_set

set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> 

>>> {x**2 for x in a_set}

set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])

Set comprehension can use if to filter the values before returning it in the result set.

>>> {x for x in a_set if x%2 == 0}

set([0, 8, 2, 4, 6])

Dictionary comprehensions are also like list comprehensions but a dictionary is created instead of a list.  A dictionary comprehension uses curly braces instead of square brackets.  A single expression actually consists of two expressions separated by a colon.  Before the colon is the dictionary key and after the colon is the value.  Also a dictionary comprehension returns a dictionary.  This example takes dictionary a_dict and switches the key and value.

>>> a_dict = {'a':1, 'b':2, 'c':3}

>>> {value:key for key, value in a_dict.items()}

{1: 'a', 2: 'b', 3: 'c'}



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





