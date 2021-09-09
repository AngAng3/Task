import numpy as np
import sys

def printResult(file_path):
    array = np.loadtxt(file_path)       # Создали новый массив из данных файла
    print("%.2f" % np.nanpercentile(array, 90))  # 90 перцентиль
    print("%.2f" % np.median(array))             # Медиана
    print("%.2f" % np.amax(array))               # Максимальное значение
    print("%.2f" % np.amin(array))               # Минимальное значение
    print("%.2f" % np.mean(array))               # Среднее значение 


if __name__ == '__main__':
    try:
        printResult(sys.argv[1])
    except FileNotFoundError:
        print(f"File open failed")
