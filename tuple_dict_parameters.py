def fool(num, *tup, **dic):
    print(num)
    print(tup)
    print(dic)

#funcion differentiates b/w dict and tuple parametres by the '=' sign
fool(3,'amar','bhargav','tanvi',a=1,b=2,c=3)


def add(a,b,c):
    print(a+b+c)

tup = (1,2,3)
add(*tup)


def family(**fam):		# Dynamic num of variables can be accepted using **dict_var and *tuple_var
    print(fam)

fam = {'mom':40 ,'dad':50 ,'sis':16}
family(**fam)

fam = {'mom':40 ,'dad':50 ,'sis':16, 'bro':20}
family(**fam)