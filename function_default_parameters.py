def name(first, last):
    print '%s %s' % (first, last)

name('amey','shitole')


#Function will give defaut vals to parameters which cannot be left empty
def name(first = 'james', last='bond'):
    print '%s %s' % (first, last)


name()
name('amey','shitole') #You can override too
name('amey') #Equiv to name(first = 'amey')
name(last = 'shitole')
