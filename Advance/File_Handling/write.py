# write mode(w)
f1=open(r'file2.txt','w')
print(f1.tell())        
# 0

# Intial cursor position will be zero if we establish the stream in write mode
# and if the file is already existing python will over write the file that will 
# erase the data and start writing from begining 

# ----------------------------------------------------------------------------------
print(f1.read())
#  print(f1.read())
#           ^^^^^^^^^
# io.UnsupportedOperation: not readable

# ----------------------------------------------------------------------------------

f1.write("we are ")
# we are is overwritten in fil2.txt

# ----------------------------------------------------------------------------------

l1=['keerthi\n','kishan\n','chinmay\n','adarsh\n']
f1.writelines(l1)

# keerthi
# kishan
# chinmay
# adarsh 
# Writing multiple lines into file 

# -----------------------------------------------------------------------------------

f1.write(l1)
# f1.write(l1)
# TypeError: write() argument must be str, not list

# -----------------------------------------------------------------------------------

l1=['keerthi','kishan','chinmay','adarsh']
f1.writelines(l1)
# keerthikishanchinmayadarsh

# -----------------------------------------------------------------------------------

if f1.writable():
    print("File one is writeable")
else:
    print("file is not writeable ")

# File one is writeable

# ------------------------------------------------------------------------------------

# if file is not existing python will create new file and starts writing in it 

f2=open("file3.txt",'w')
f2.write("keerthi")
# keerthi

# --------------------------------------------------------------------------------

f1.close()
f2.close()