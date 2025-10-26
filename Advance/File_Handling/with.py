# with: with keyword is used in file handling to create with block 
# when with block ends file gets closed automatically

with open('file1.txt','r+') as f:
    print(f.read())
    print()
    print("Inside with block")
    if f.closed:
        print("file is closed ")
    else:
        print("file is open")
print()
print("Outside with block ")
if f.closed:
    print("file is closed ")
else:
    print("file is open")

# I am a good students
# we learn python
# we are idiots

# Inside with block
# file is open

# Outside with block
# file is closed

# f.read()
#     f.read()
# ValueError: I/O operation on closed file.

# ---------------------------------------------------------------------------------------------

# copy from 1 file to another in uppercase

f1=open('file1.txt','r')
f2=open('file6.txt','w')
s=f1.read()
f2.write(s.upper())

# file6 op:
# I AM A GOOD STUDENTS
# WE LEARN PYTHON 
# WE ARE IDIOTS

# -------------------------------------------------------------------------------------------

# count space in file

cnt=s.count(" ")
print(cnt)
# 9
f1.close()
f2.close()

# ------------------------------------------------------------------------------------------