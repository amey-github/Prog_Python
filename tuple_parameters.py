def name(num, *tup):

    print num, 'tup', '\n'

    for i in range(len(tup)):
        print i, tup[i]

#takes everthing after 3 as part of tuple
tup = ('amar','bhargav','tanvi')
name(3, tup[0], tup[1], tup[2])
