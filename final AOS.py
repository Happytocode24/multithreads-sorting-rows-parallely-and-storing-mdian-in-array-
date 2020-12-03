from threading import *
import numpy
from time import sleep
import statistics
from array import *

myArray = []
textFile = open("simpleinput.txt", 'r')  #reading input text file
n = (int(textFile.readline()))
m = (int(textFile.readline()))

lines = textFile.readlines()
for line in lines:
    myArray.append(list(map(int, line.rstrip().split())))

A = numpy.array(myArray)


def sort(i):

    for k in range(m - 1):

        for j in range(m - 1):
            if A[i, j] > A[i, j + 1]:
                temp = A[i, j]
                A[i, j] = A[i, j + 1]
                A[i, j + 1] = temp
                print(A, current_thread().getName(), "\n ")#printing thread number of currently thread
                sleep(1)


for i in range(n):
    t1 = Thread(target=sort, args=(i, ))
    t1.start()
t1.join()
print(A, current_thread().getName(), "final matrix", "\n")#printing thread number of currenttly thread
print('above threads running Parallelly', "\n")

