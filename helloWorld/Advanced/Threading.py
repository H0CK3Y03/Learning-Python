# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading
# each thread does it's own thing


import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

start = time.perf_counter()

x = threading.Thread(target=eat_breakfast, args=())   # target has to be without parenthesis (), or else it'll take the same amount of time
x.start()     #thread 1

y = threading.Thread(target=drink_coffee, args=())
y.start()     #thread 2

z = threading.Thread(target=study, args=())
z.start()     #thread 3

x.join()     # the main thread waits for the new threads to finish and join the main thread
y.join()     # they deactivate as soon as they are done
z.join()     # so the last active thread is the main thread

# eat_breakfast()                           # without threading (x,y,z) this program does tasks sequentially som it takes 12 seconds
# drink_coffee()                            # with threading (x,y,z) it will take 5 seconds
# study()

# main thread creates 3 new threads(x,y,z) and then prints the stuff below this message
# each new thread was assigned it's own function / task to complete

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

end = time.perf_counter()

print("Time elapsed:", end - start)













































