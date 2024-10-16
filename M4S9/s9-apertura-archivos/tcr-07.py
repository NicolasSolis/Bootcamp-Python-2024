file = open("sample.txt") 
print(file.read()) 
file.close()
file.write(" Attempt to write on a closed file !") ## ValueError