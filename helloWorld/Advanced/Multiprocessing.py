# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

start = time.perf_counter()

def counter(num):
    count = 0
    while count <= num:
        count += 1

def main():

    print(cpu_count())   # if you have more processes than cpu_count than it might run slower

    a = Process(target=counter, args=(125000000,))       # (num,) -> so it counts as a tuple
    b = Process(target=counter, args=(125000000,))  # (num,) -> so it counts as a tuple
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()


    a.join()    # main process will wait for child process (a) to finish before continuing
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    end = time.perf_counter()

    print("Finished in: ", end - start, " seconds")

if __name__ == '__main__':     # only executes if it is in this module, it can still copy, but won't run in other modules

    main()



# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with
# holding down middle mouse button allows me to use more than 1 cursor or whatever I write with


















