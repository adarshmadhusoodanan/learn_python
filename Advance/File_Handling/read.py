# read mode
# establishing stram in read mode
f1=open(r'file1.txt','r')

# reading the data as a single string
s=f1.read()
print(s)

# I am a good students
# we learn python
# we are idiots

# --------------------------------------------------------------------------------------

# read firt 4 charcters
print(f1.read(6))                        
# I am a

# read next 4 characters
print(f1.read(6))
#  good 

print(f1.read(-4))
# I am a good students
# we learn python
# we are idiots

# ---------------------------------------------------------------------------------------

# read a line
print(f1.readline())
print(f1.readline())
# I am a good students
#                                   # provides line gap
# we learn python
# 

# no line gap 
print(f1.readline(),end='')
print(f1.readline(),end='')
# I am a good students
# we learn python 

print(f1.readline(6))
print(f1.readline())
# I am a
#  good students
# 

# ---------------------------------------------------------------------------------------

# reading file as list of string 
l1=f1.readlines()
print(l1)
# ['I am a good students\n', 'we learn python \n', 'we are idiots']
print(l1[1])
# we learn python 
# 
# ----------------------------------------------------------------------------------------

# cursor position
print(f1.tell())
# 0
print(f1.read(4))
print(f1.tell())
# I am
# 4

# moving back the cursor
f1.seek(0)
print(f1.tell())
# 0
f1.seek(5)
print(f1.tell())
# 5
# ----------------------------------------------------------------------------------------

# verify file is readable or not 

if f1.readable():
    print("File one is readable")
else:
    print("file is not readable ")
# File one is readable

# --------------------------------------------------------------------------------------------

# to verify file is closed 
if f1.closed:
    print("file closed")
else:
    print("file not closed")
# file not closed

# closing the file or killing the stream
f1.close()

if f1.closed:
    print("file closed")
else:
    print("file not closed")
# file closed

f2=open("f2.txt",'r')
# f2=open("f2.txt",'r')
#        ^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'f2.txt'