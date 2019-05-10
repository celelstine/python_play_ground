"""illustrate python global Interpreter Lock (GIL)"""

"""
GIL is a mutex that allow only one thread to hold control of the python interpreter at a given time.
With GIL (which leaves only in cpython), multithreading would not add an enhance,
the way to increase efficiency of heavy program is to use MUltiprocess module
"""


import time
from threading import Thread

COUNT = 5000000


def timer(func):
    """time how long a function run"""

    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print("{} ran for {} seconds".format(func.__name__, duration))
        return result
    return inner_function


@timer
def single_thread_count(n):
    while n > 0:
        n -= 1
    return "run loop {} times \n".format(n)


@timer
def multi_thread_count(n):
    def inner_function(count):
        while count > 0:
            count -= 1
    
    # run inner function in multiple thread
    thread1 = Thread(target=inner_function, args=(n//2,))
    thread2 = Thread(target=inner_function, args=(n//2,))


    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return "run loop {} times \n".format(n)


import os
from multiprocessing import Pool


@timer
def multi_processes_count(n):
    def inner_function(count):
        while count > 0:
            count -= 1

    """
    run inner function in multiple processes
    a process has its own interpreter and memory space, so no GIL problems
    in some OS, each process runs on a processor
    a pool is use to create processes that can run in parallel, they can share the execution of a function via data parallelism
    """
    pool = Pool(processes=2)
    process1 = pool.apply_async(inner_function, [n//2])
    process2 = pool.apply_async(inner_function, [n//2])
    pool.close()
    pool.join()
    return "run loop {} times \n".format(n)






print(single_thread_count(COUNT)) 
print(multi_thread_count(COUNT))
# observation: both single_thread_count and multi_thread_count run at almost the same time no advantage was agained

print(multi_processes_count(COUNT)) # runs within halve the time of single_thread_count and multi_thread_count

 
# more with multiprocesses

# communication between process

# one way communication via queue

from multiprocessing import Process, Queue


def one_way_connection(*args, **kwargs):

    def inner_function(q):
        # fetch params from args and kwargs
        # perfform some logic and with result, assume result = [1, 'Animal', 'Dog']
        q.put([1, 'Animal', 'Dog'])
    
    q = Queue()
    process = Process(target=inner_function, args=(q,)) # args must be an iterable
    # start the process
    process.start()
    # fetch message from queue
    # Note: enusre that the items ina queue are read before you join the process else the queue would 
    print(q.get())
    # end process
    process.join()

# test 
one_way_connection()
        

# two way communication with pipe
from multiprocessing import Pipe


def two_way_connection(*args, **kwargs):

    def inner_function(connection):
        # fetch params from args and kwargs
        # perfform some logic and with result, assume result = [2, 'Plant', 'Beans']
        connection.send([2, 'Plant', 'Beans'])
        # close the connection
        connection.close()
    
    parent_conn, child_conn = Pipe()
    process = Process(target=inner_function, args=(child_conn,)) # args must be an iterable
    # start the process
    process.start()
    # fetch message from parent connection
    # recv() automatically unpickle the data received, its recommended to always authenticate the send
    print(parent_conn.recv())
    # end process
    process.join()


two_way_connection()


# use pool to create multiple process that handle http request from a socket

