#---------------------------My First Python Program---------------------------
print('Hello, World!') #Hello World!

#-----------------Variables--------------------
# A reserved memory location to store values

# Declare a variable and intialize it
b = 'Favour'
print(b) #Favour
# Re-declaring the variable works
b = '9'
print(b) # Favour, 9

# Concantenate different data types
a = 'Favour'
b = '12'
print (a + str(b)) #Favour12

# Global variable vs Local variable in functions
f = '200'
print(f)
def someFunctions():
    f ='I am learning python'
    print(f)
    someFunctions()
    print(f) # 200

# Chr() and Ord()
print ('The Unicode Character Of The tab is')
Ord = ord('\t')
print(Ord) # 9

Textexample = 'Favour + chr(9) + 99'
print(Textexample)

