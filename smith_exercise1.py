#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['ANTAGONIST', 'BEAST', 'CRIMINAL', 'DEBASER', 'EVILDOER', 'HOOLIGAN',
            'KNAVE', 'LAW-BREAKER', 'MISCREANT', 'OUTLAW', 'RAPSCALLION', 'SABOTEUR', 'TRANSGRESSOR',
            'VILLAIN', 'WRETCH']
adjectives = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED', 'MYSTERIOUS', 
                'INTRIGUING', 'CONFUSED', 'STARRY-EYED']
conjunctions = [' AND ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ', ' AND ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST', 'THE WORST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) + phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year and day from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[ ]:




