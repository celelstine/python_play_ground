"""play with decorators"""

def safe_execution(func):
    """run a function in safe mode"""

    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("An exception occcurred, details:{}".format(e))

    return inner_func



@safe_execution
def divide(a,b):
    return a/b


# divide(2,0)


# inner function
def power_of(x):
    """create a inner function to return the power of x"""

    def inner_func(y):
        return x**y

    return inner_func


power_5 = power_of(5)
print(power_5(4))
power_2 = power_of(2)
print(power_2(4))



def disable(func):
    """decorator to disable a function"""

    def inner_func(*args, **kwargs):
        print('This function ({}) is diabled'.format(func.__name__))

    return inner_func


@disable
def test_func(arg):
    print(arg)

test_func(3)


import datetime

def disable_for_n_minutes(minutes):
    """disable a function for n minutes"""

    start_time = datetime.datetime.now()

    def decorator(func):
        """the inner decorator"""

        def inner_func(*args, **kwargs):
            current_time = datetime.datetime.now()
            elapsed_time = current_time - start_time
            elapsed_time_seconds = elapsed_time.total_seconds()


            if elapsed_time_seconds >= minutes * 60:
                print("Function is enabled")
                return func(*args, **kwargs)
            else:
                remaining_time = minutes * 60 - elapsed_time_seconds
                print("Function ({}) is disabled, would be active in {}".format(
                    func.__name__,remaining_time))
        
        return inner_func
    return decorator


@disable_for_n_minutes(0.5)
def test_func1(arg):
    return arg

import time


output = None
while output is None:
    output = test_func1('function is active')
    time.sleep(10)

test_func1('function is active')
