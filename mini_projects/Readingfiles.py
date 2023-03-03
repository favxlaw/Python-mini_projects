class_file = open("classlist.txt", "r") # open the file
print(class_file.readlines())
class_file.close() #close the file 

#Writing And Appending To Files
class_file = open("classlist.txt", "a") # open the file
print(class_file.write("\nFavour--- CEO"))
class_file.close() 