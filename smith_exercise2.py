#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=25

def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

def quadruple(sequence):
    result = []
    for element in sequence:
        result = result + [element * 4]
    return result

def addSeq(sequenceA, sequenceB):
    i = 0
    for element in sequenceA:
        i = i + element
    for element in sequenceB:
        i = i + element
    return i

addSeq(double([34, 6, 6, x]), quadruple([57, 4, 3, x]))


# In[ ]:




