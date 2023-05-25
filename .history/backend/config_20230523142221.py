import os 
import sys 




path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(os.path.abspath(sys.argv[0]))

print(os.path.exists(path))



print(path)