dict_name = {'a':50, 'b':100, 'c':15, 'd':2, 'e':23}

print(min(dict_name), '\n')		# Gives the min, sorts by key_name (defualt)


# Sort by VALUES...............

temp = list(zip(dict_name.values(), dict_name.keys()))
print(temp)
print(min(temp), '\n')


# Sort by KEYS.................

temp = list(zip(dict_name.keys(), dict_name.values()))
print(temp)
print(min(temp))