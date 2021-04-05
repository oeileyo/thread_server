import time

numb = int(input("Число шагов : "))
tsec = int(input("Сколько секунд ждать : "))

for i in range(numb):
    print("Ждем", tsec, "; шаг", i)
    time.sleep(tsec)

