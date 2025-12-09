# Positional Arguments: number of arguments in function call should be equal to number of parameters in function definition

def student_info(name, roll_no, branch):             # parameters
    print(f" Student name: {name}")                  # we can access parameters directly using their name.
    print(f" Student roll number: {roll_no}")
    print(f" Branch: {branch}")
    print("*************************")  
student_info("Keerthana G", 1, "CSE")                # arguments
student_info("Adarsh M", 2, "CSE")

# output
        #  Student name: Keerthana G
        #  Student roll number: 1
        #  Branch: CSE  
        # *************************
        #  Student name: Adarsh M               
        #  Student roll number: 2
        #  Branch: CSE
        # *************************

# Keyword Arguments: during function call we can pass the arguments with the parameter name, so the order of arguments doesn't matter

def student_info(name, roll_no, branch):             # parameters
    print(f" Student name: {name}")                  # we can access parameters directly using their name.
    print(f" Student roll number: {roll_no}")
    print(f" Branch: {branch}")
    print("*************************")  
student_info(roll_no=1, branch="CSE", name="Keerthana G")  # arguments
student_info(branch="CSE", name="Adarsh M", roll_no=2)

# output
        #  Student name: Keerthana G
        #  Student roll number: 1
        #  Branch: CSE  
        # *************************
        #  Student name: Adarsh M               
        #  Student roll number: 2
        #  Branch: CSE
        # *************************

# Default Arguments: defining an argument with a default value in function definition, so while function call if we don't pass the argument it takes the default value

def student_info(name, roll_no, branch="CSE"):       # parameters
    print(f" Student name: {name}")                  # we can access parameters directly using their name.
    print(f" Student roll number: {roll_no}")
    print(f" Branch: {branch}")
    print("*************************")          
student_info("Keerthana G", 1)                      # arguments
student_info("Adarsh M", 2, "ECE")

# output
        #  Student name: Keerthana G
        #  Student roll number: 1
        #  Branch: CSE  
        # *************************
        #  Student name: Adarsh M               
        #  Student roll number: 2
        #  Branch: ECE
        # *************************

# orbitory variable arguments:

# during function defination an argument define with a * prefix, 
# so while function call we can pass n number of arguments and it stores all the arguments in the form of tuple

def add(*numbers):                                  # parameters
    print("The sum is:", sum(numbers))              # we can access parameters directly using their name. 
    print(type(numbers)) 
add(5, 10)                                          # arguments
add(20, 30, 40, 50, 60)

# output
        # The sum is: 15 
        # <class 'tuple'>
        # The sum is: 200
        # <class 'tuple'>

def orbi_fun(res,*numbers,a):                             # parameters
    print(numbers,a,res)
orbi_fun("hello",1,2,3,4,5,a=10)                          # arguments

# output
        # (1, 2, 3, 4, 5) 10 hello  

# orbitory keyword variable arguments: 

# during function defination an argument define with a ** prefix, 
# so while function call we can pass n number of keyword arguments and it stores all the arguments in the form of dictionary

def student_info(**info):                            # parameters
    print(info)                                      # we can access parameters directly using their name. 
    print(type(info))       
student_info(name="Keerthana G", roll_no=1, branch="CSE")  # arguments
student_info(name="Adarsh M", roll_no=2, branch="ECE", college="JSS")       

# output
        # {'name': 'Keerthana G', 'roll_no': 1, 'branch': 'CSE'}        
        # <class 'dict'>
        # {'name': 'Adarsh M', 'roll_no': 2, '  branch': 'ECE', 'college': 'JSS'}   
        # <class 'dict'>

def orbi_key_fun(*info,**info2):                        # parameters
    print(info)
    print(info2) 
orbi_key_fun(1,2,3,a=10,b=20)                           # arguments

# output
        # (1, 2, 3) 
        # {'a': 10, 'b': 20}

def orbi_key_fun(a,res,*info,m,**info2):                  # parameters
    print(info)
    print(info2) 
    print(a,res,m)
orbi_key_fun(1,"hello",2,3,m=30,a=10,b=20)              # arguments

# output
        # (2, 3)
        # {'a': 10, 'b': 20}
        # 1 hello 30
        
# Note: In a function we can use only one orbitory variable argument and one orbitory keyword variable argument, but we can use them together in a function.    
# Note: In a function we can use orbitory variable arguments and orbitory keyword variable arguments together but the orbitory variable argument should be in the first place followed by orbitory keyword variable arguments.
# Note: In a function we can use positional arguments, keyword arguments, default arguments, orbitory variable arguments and orbitory keyword variable arguments together but the positional arguments should be in the first place followed by keyword arguments, default arguments, orbitory variable arguments and orbitory keyword variable arguments should be at the last.