#MEDIAN OF ROWS

arr1 = array('f', [])


def median(x):
    arr = array('f', [])

    for j in range(m):

        val = A[x][j]
        arr.append(val)

    arr1.append(statistics.median(arr))
    print(arr1, current_thread().getName(), "\n")
    


for x in range(n):
    t2 = Thread(target=median, args=(x, ))
    t2.start()
t2.join()
print('median', arr1)
