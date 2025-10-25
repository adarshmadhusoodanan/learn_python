# append mode(a)
f1=open("file3.txt",'a')
print(f1.tell())
# 7
# File will not be erased instead python starts writing from the end
# initial cursor position will be at last 

# ----------------------------------------------------------------------------------

#  In append mode file is writeable but not readable 

# f1.read()
#     f1.read()
# io.UnsupportedOperation: not readable

f1.write("\nKishan\n")
# keerthi
# Kishan

l1=['keerthi\n','kishan\n','chinmay\n','adarsh\n']
f1.writelines(l1)
# keerthi
# Kishan
# keerthi
# kishan
# chinmay
# adarsh

# ---------------------------------------------------------------------------------

# if file doesnt exist python will create a new file 

f2=open("file4.txt",'a')
f2.write("adarsh")
# adarsh

f2.writelines(l1)
# adarshkeerthi
# kishan
# chinmay
# adarsh

# ----------------------------------------------------------------------------------

f1.close()
f2.close()