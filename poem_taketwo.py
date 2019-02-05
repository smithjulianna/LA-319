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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'SCOUNDREL', 'THIEF', 'PICTURE',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'NARROW', 'NEAR',
              'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[ ]:





# In[2]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[3]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[4]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + predicates(choice) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[5]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + predicates(choice) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[6]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[7]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + predicates(choice) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')
print(phrase() + predicates(choice) + choice(conjuctions) +
      phrase() + choice(predicates) + '.')


# In[8]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + predicates(choice) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')


# In[9]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[10]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[11]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[12]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[ ]:





# In[13]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'PRISONER', 'THIEF', 'MADMAN',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'LECHEROUS',
              'VIOLENT', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'FURIOUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[14]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', 'BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[15]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', 'BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[16]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', 'BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[17]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', 'BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[18]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[19]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[20]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[21]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[22]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[23]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[24]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[25]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[26]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[27]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[28]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[29]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[30]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[31]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[32]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[33]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[34]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[35]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'
print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[36]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[37]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[38]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[39]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[40]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[41]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[42]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[43]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[44]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[45]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '
    
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[46]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
      if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[47]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[48]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[49]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if choice(subject) == 'SCOUNDREL':
        choice(predicate) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[50]:





# In[51]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text choice(subjects) == 'SCOUNDREL':
        text choice(predicates) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[52]:





# In[53]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text choice(subjects) == 'SCOUNDREL':
        text choice(predicates) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'#!/usr/bin/python

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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text choice(subjects) == 'SCOUNDREL':
        text choice(predicates) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[54]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text choice(subjects) == 'SCOUNDREL':
        text choice(predicates) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[55]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text choice (subjects) == 'SCOUNDREL':
        text choice (predicates) = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[56]:


C


# In[57]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[58]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

if text = 'SCOUNDREL'
then text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[59]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

if text == 'SCOUNDREL'
then text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[60]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

if text == 'SCOUNDREL':
then text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[61]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

if text == 'SCOUNDREL':
    then text = 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[62]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

if text == 'SCOUNDREL':
    then text == 'SINFUL'

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[63]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[64]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[65]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[66]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[67]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[68]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[69]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[70]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[71]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[72]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[73]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[74]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[75]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[76]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[77]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[78]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[79]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[80]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[81]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[82]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[83]:


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

subjects = ['SCOUNDREL', 'VILLAIN', 'RUFFIAN', 'RASCAL', 'THIEF', 'MADMAN',
            'RAPSCALLION', 'BRUTE', 'WRETCH', 'OUTLAW', 'EVILDOER', 'MISCREANT', 'BEAST',
            'MALEFACTOR', 'KNAVE', 'TRANSGRESSOR']
predicates = ['DESPICABLE', 'ODIOUS', 'CONTENTIOUS', 'MALEVOLENT', 'SINFUL', 'WICKED',
              'VIOLENT', 'CORRUPT', 'EVIL', 'BLACK-HEARTED', 'SAVAGE', 'AMORAL', 'DEPRAVED',
              'DISSOLUTE', 'DEBASED', 'DANGEROUS']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SCOUNDREL':
        text = 'SINFUL'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[84]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED, 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[85]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[86]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[87]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[88]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[89]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[90]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[91]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[92]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[93]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '


print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[94]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '


print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[95]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '


print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[96]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'HOOLIGAN':
        text = 'HELLISH'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[97]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'HOOLIGAN':
        text = 'HELLISH'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[98]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'HOOLIGAN':
        text = 'HELLISH'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'KNAVE':
        text = 'KNIVING'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'LAW-BREAKER':
        text = 'LAWLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'MISCREANT':
        text = 'MALICIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'OUTLAW':
        text = 'ODIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'RAPSCALLION':
        text = 'REPROBATE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SABOTEUR':
        text = 'SAVAGE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'TRANSGRESSOR':
        text = 'THOUGHTLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'VILLAIN':
        text = 'VIOLENT'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'WRETCH':
        text = 'WICKED'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[99]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'HOOLIGAN':
        text = 'HELLISH'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'KNAVE':
        text = 'KNIVING'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'LAW-BREAKER':
        text = 'LAWLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'MISCREANT':
        text = 'MALICIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'OUTLAW':
        text = 'ODIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'RAPSCALLION':
        text = 'REPROBATE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SABOTEUR':
        text = 'SAVAGE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'TRANSGRESSOR':
        text = 'THOUGHTLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'VILLAIN':
        text = 'VIOLENT'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'WRETCH':
        print = 'WICKED'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[100]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'ANTAGONIST':
        text = 'AMORAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'BEAST':
        text = 'BLACK-HEARTED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'CRIMINAL':
        text = 'CONTENTIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'DEBASER':
        text = 'DEPRAVED'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'EVILDOER':
        text = 'EGOTISTICAL'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'HOOLIGAN':
        text = 'HELLISH'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'KNAVE':
        text = 'KNIVING'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'LAW-BREAKER':
        text = 'LAWLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'MISCREANT':
        text = 'MALICIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'OUTLAW':
        text = 'ODIOUS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'RAPSCALLION':
        text = 'REPROBATE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'SABOTEUR':
        text = 'SAVAGE'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'TRANSGRESSOR':
        text = 'THOUGHTLESS'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'VILLAIN':
        text = 'VIOLENT'
    return text + ' IS '

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'WRETCH':
        text = 'WICKED'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[101]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print('')
print (phrase() + predicates(choice) + conjuctions(choice) +
       phrase() + predicates(choice) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[102]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[103]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
adjectives = ['WANDERING']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + choice(adjectives) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[104]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
adjectives = ['WANDERING']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + choice(conjuctions) + choice(adjectives) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[105]:


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
predicates = ['AMORAL', 'BLACK-HEARTED', 'CONTENTIOUS', 'DEPRAVED', 'EGOTISTICAL', 'HELLISH',
              'KNIVING', 'LAWLESS', 'MALICIOUS', 'ODIOUS', 'REPROBATE', 'SAVAGE', 'THOUGHTLESS', 'VIOLENT', 'WICKED']
adjectives = ['WANDERING']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + choice(conjunctions) + choice(adjectives) + '.')
print('')

print 'THE STATEMENT ABOVE IS FALSE. THE STATEMENT BELOW IS TRUE.'


# In[106]:


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
moreadjectives = ['WANDERING' 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjuctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[107]:


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
moreadjectives = ['WANDERING' 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjuctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[108]:


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
moreadjectives = ['WANDERING' 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjuctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[109]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[110]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = ['YET']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[111]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[112]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[113]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(comma
                                                                    ) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[114]:


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
moreadjectives = ['...WANDERING', '...LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[115]:


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
moreadjectives = ['...WANDERING', '...LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(conjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[116]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[117]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[118]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[119]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(adjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[120]:


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
moreadjectives = ['WANDERING', 'LONESOME']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# In[122]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

"Helvetica 10 bold italic"


# In[123]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")


# In[124]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

helv36 = Font(family="Helvetica",size=36,weight="bold")


# In[125]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

helv36 = (family="Helvetica",size=36,weight="bold")


# In[126]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

helv36 = (family = "Helvetica",size=36,weight="bold")


# In[127]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

import tkFont
helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")


# In[128]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

import tkFont
helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")


# In[129]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[130]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'THE STATEMENTS ABOVE ARE FALSE. THE STATEMENTS BELOW ARE TRUE.'


# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[131]:


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
moreadjectives = ['WANDERING', 'LONESOME', 'MELANCHOLY', 'MISUNDERSTOOD', 'NEGLECTED']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' ,YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[132]:


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
                'INTRIGUING']
conjunctions = [' AND ', ' OR ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[133]:


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
                'INTRIGUING']
conjunctions = [' AND ', 'THEREFORE,' ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[134]:


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
                'INTRIGUING']
conjunctions = [' AND ', 'THEREFORE,' ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[135]:


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
                'INTRIGUING']
conjunctions = [' AND ', ' ;THEREFORE, ', ' ,BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ', ' AND ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST', 'THE WORST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[136]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2
d = 5

# To ask month and year and day from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# d = int(input("Enter day: "))


# display the calendar
print(calendar.month(yy, mmm, d))


# In[137]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2
d = 5

# To ask month and year and day from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# d = int(input("Enter day: "))


# display the calendar
print(calendar.month(yy, mm, d))


# In[138]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2
d = 5

# To ask month and year and day from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# d = int(input("Enter day: "))


# display the calendar
print(calendar.month(yy, mm, d))


# In[139]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
print('')

print 'IT IS UP TO THE BEHOLDER TO DETERMINE WHETHER OR NOT THE STATEMENTS ABOVE HAVE ANY VALIDITY. THE ONLY TRUTH IN THIS LIFE IS THE PASSING OF TIME.'

# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2019
mm = 2

# To ask month and year and day from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: ")

# display the calendar
print(calendar.month((yy, mmm))


# In[140]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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
print(calendar.month((yy, mmm))


# In[141]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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
print(calendar.month((yy, mm))


# In[142]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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


# In[143]:


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

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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


# In[144]:


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
conjunctions = [' AND ', ' THEREFORE, ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ', ' AND ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST', 'THE WORST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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


# In[145]:


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
conjunctions = [' AND ', ' THEREFORE, ', ' BUT ', ' THUS ', '. ', '. ', '. ', '. ', '. ']
moreconjunctions = [' YET ', ' OR ', ' AND ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY', 'A SINGLE', 'THE BEST', 'THE WORST']

print('')
print(phrase() + choice(adjectives) + choice(conjunctions) +
       phrase() + choice(moreadjectives) + choice(moreconjunctions) + choice(moreadjectives) + '.')
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




