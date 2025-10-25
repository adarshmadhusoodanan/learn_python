# File handling: In order do read data from a file or write data into a file or
#                manupulate the data of a file or create a file we perform file 
#                handling operations using python 
# Serialization: Sending data from python file to other file 

# variable=open('filename','mode') Text to wrapper 

# ------------------------------------------------------------------------------------

# Modes

# Basic:                    combined:                      Binary:

# read -> 'r'               r+ -> read+write               rb -> read to binary
# write -> 'w'              w+ -> write+read               wb -> write to binary
# append -> 'a'             a+ -> write+read
# create -> 'x'             x+ -> write+read
# text -> 't'               t+ -> write+read

# --------------------------------------------------------------------------------------

# r+ (read+write)

# If we establish a stream in r+ mode file is both readable and writeable
# The file must already exist otherwise, it will throw an error
# Initial cursor position will be zero 
# if we write something python will overwrite that many characters in the file

# --------------------------------------------------------------------------------------

#  w+ (write+read)

# If we establish a stream in w+ mode file is both writeable and readable
# If file is already exist its contents are erased
# If file doesnt exist it is created
# Initial cursor position will be zero

# ---------------------------------------------------------------------------------------

# a+ (write+read)

# If we establish a stream in a+ mode file is both writeable and readable
# If file is already exist file will not be erased instead python starts writing from the end
# If file doesnt exist it is created
# Initial cursor position will be at last
# To read we should use seek

# -----------------------------------------------------------------------------------------

# x+ (write+read)

# If we establish a stream in x+ mode file is both writeable and readable
# If file is already exist python will rise file exist error 
# If file doesnt exist it is created
# Initial cursor position will be zero