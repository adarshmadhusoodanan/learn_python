import time 
import threading
start=time.time()
def anything():
    for i in range(5):
        print('Do anything')
        time.sleep(2)
def something():
    for i in range(5):
        print('Do something')
        time.sleep(1)
t1=threading.Thread(target=anything)
t2=threading.Thread(target=something)
t1.start()
t2.start()
t1.join()
t2.join()
end=time.time()
print("Total time taken",end-start)

# Do anything
# Do something
# Do something
# Do anything
# Do something
# Do something
# Do anything
# Do something
# Do anything
# Do anything
# Total time taken 10.00681734085083