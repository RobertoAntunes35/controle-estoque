import os 
import sys 




path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(os.path.abspath(sys.argv[0]))

file = path + '\D01_Cliente.xls'

print(os.path.exists(file))



print(path)