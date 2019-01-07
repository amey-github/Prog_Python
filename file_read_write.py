#********** WRITING/ CREATING FILE

# file_write : object to write into file_name

file_write = open('file_name.txt', 'w')		# open() : prepares a file to be written/created, 'w' : permission to write

file_write.write('Write to file\n')			# Typing into a file
file_write.write('Blah blah \nMore blah')

file_write.close()			# Frees up computer memory, closes file object

#********** READING FILE

# file_read : object to read data from file_name

file_read = open('file_name.txt', 'r')

read_var = file_read.read()					# Reads data from file_name
print (read_var)

file_read.close()