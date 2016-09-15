[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Swati Sharma
>> Exercise 3-1
>> Tasks:
>> Deterimine and plot actual and biased distributions
>> Compute means for actual and biased distributions
>> In [1]:
>>
>>%matplotlib inline
>>​
>>import chap01soln
>>resp = chap01soln.ReadFemResp()
>>In [2]:
>>
>>import thinkstats2
>>pmf = thinkstats2.Pmf(resp.numkdhh)
>># probability mass function for numkdh, numkdh is the respondant variable and provides data on how many
>># children < 18 years old.
>>In [3]:
>>
>>import thinkplot
>>​
>>thinkplot.Pmf(pmf, label='actual')
>>thinkplot.Show()
>>
>><matplotlib.figure.Figure at 0x115bd1b90>
>>Plot of actual distribution for number of children < 18 years in a household
>>In [4]:
>>
>>def BiasPmf(pmf, label=''):
>>    bpmf = pmf.Copy(label=label)
>>​
>>    for x, p in pmf.Items():
>>        bpmf.Mult(x, x)
>>        
>>    bpmf.Normalize()
>>    return bpmf
>>In [5]:
>>
>>biased = BiasPmf(pmf, label='biased')
>>​
>>In [6]:
>>
>>thinkplot.PrePlot(2)
>>thinkplot.Pmfs([pmf, biased])
>>thinkplot.Show()
>>
>><matplotlib.figure.Figure at 0x11c0f1d10>
>>Plot of actual and biased distributions for number of children < 18 in a household
>>In [7]:
>>
>>m_act = pmf.Mean()
>>print 'Mean of actual distribution =', m_act
>>m_bias = biased.Mean()
>>print 'Mean of biased distribution', m_bias
>>Mean of actual distribution = 1.02420515504
>>Mean of biased distribution 2.40367910066
>>In [ ]:
>>
>>​

