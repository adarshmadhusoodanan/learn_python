# create mode(x)

f1=open("file5.txt",'x')
print(f1.tell())
# 0
# In create mode initial cursor position will be zero
# If file doesnt exist then python will create new file 

# ------------------------------------------------------------------------

# In create mode file is writeable not readable 

f1.write('adarsh\nkeerthi\n')
# adarsh
# keerthi
# 

print(f1.read())
#     print(f1.read())
#           ^^^^^^^^^
# io.UnsupportedOperation: not readable

# ------------------------------------------------------------------------

# If file exits python will rise file exist error

f1=open("file1.txt",'x')
#     f1=open("file1.txt",'x')
#        ^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: 'file1.txt'

# -------------------------------------------------------------------------

f1.close()