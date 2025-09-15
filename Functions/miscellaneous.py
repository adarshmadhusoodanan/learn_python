# Miscellaneous Functions: defining a new variable which takes the address of a function 
#                          and accessing function through that variable.

def greet():
    print("Hello")
greeting=greet
print(greeting)
greet()
greeting()

# output
        #<function greet at 0x00000182F5CECA40>
        # Hello
        # Hello

