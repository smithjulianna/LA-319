#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tline = open('renaissancetimeline.txt', 'r')


rline = tline.read()
splittext = rline.split()

dateset = []
for x in range(0,len(splittext)):

    if splittext[x].isdigit() == 1 and int(splittext[x]) < 1601 and int(splittext[x]) > 1299:

        dateset.append(splittext[x])


print(dateset)

