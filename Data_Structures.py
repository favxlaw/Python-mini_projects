#--------------------Tuples---------------------------------------
Tup = ('Jan', 'Feb', 'Mar') # syntax

cars = ('benz','toyota','carmy','corolla') # tuple packing
#(benz, toyota, carmy, corolla) = cars # tuple unpacking
print (cars[2:3])

#comparing
a ='6'
b ='7'
if (a > b): print('a is bigger')
else: print('b is bigger') # b is bigger

a = {'x': 100, 'y': 300}
b = list (a.items())
print (b) #dictionary returning the list of tuples by calling items

#-----------------------------Dictionaries----------------------------------
Dict = {'z':20, 'p':30} # dict syntax
print(Dict['z']) #20
num1 = {'z':20}
num2 ={'p':30}
num1cy = num1.copy() 
num2cy = num2.copy()
print (num1cy)
print (num2cy) #copying in Dict
Dict.update({'H': 40})
print(Dict) #update Dict
del Dict ['p']
print(Dict) # p del

a = '90'
b = '50'
print(a and b is True) #false
print(a or b is True)


#---------------------------Arrays------------------------------
# A collection of common types of data structures having the data types
#arrayName = array.array (type of code for datatype, [array, items]) #syntax
import array as practiceArray
learning = practiceArray.array ('i', [2, 4, 5, 7])
print (learning[2]) # 5
# .insert, .pop(), .del, .remove, .reverse

#Transverse array
import array
balance = array.array('i', [300,200,100])
for x in balance:
	print(x) # 300, 200, 100

#-----------------------------2D Arrays---------------------------------------
# an array inside the array
#[[a,b,c,d], [1,2,3,4]] syntax

#List comprehension 
list_ofsquares = []
for int in range(1, 20) :
    square = int ** 2
    list_ofsquares.append(square)
print(list_ofsquares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]


