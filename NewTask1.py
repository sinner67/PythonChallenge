import sys

def div3(var):
    if float(var) % 3 == 0:
        print(True)
    else:
        print(False)

try:
    div3(sys.argv[1])
except:
    print('Incorrect arguments!')
        
