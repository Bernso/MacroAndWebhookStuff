import time

start = time.time()

while True:
    timeToPrint = round(time.time() - start, 0)
    print(timeToPrint)
    time.sleep(1)