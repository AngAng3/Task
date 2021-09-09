import numpy as np
import sys

def getMaxInterval(path):
    array_sum_client = np.loadtxt(path +"\Cash1.txt")
    for i in range(2,6):
        fname = path +"\Cash"+str(i)+".txt"
        array_sum_client += np.loadtxt(fname)
    print(np.argmax(array_sum_client)+1)

if __name__ == '__main__':
    try:
        getMaxInterval(sys.argv[1])
    except FileNotFoundError:
        print(f"File open failed")
