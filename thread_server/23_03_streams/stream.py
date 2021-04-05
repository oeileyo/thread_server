import time
import threading

def proc(n, tsec):
    print("Ждем", tsec, "; шаг", i)

myp = []

npt = int(input("Число шагов: "))
tsec = int(input("Сколько секунд ждать : "))

for i in range(npt):
    myp.append(threading.Thread(target=proc, name=str(i), args=[str(i), tsec]))

for i in range(npt):
    myp[i].start()

