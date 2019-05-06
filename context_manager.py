"""illustrates the concept of context managers:"""
import datetime
class TimerContextManager(object):
    """create a context that returns the current time
    a context manager must implement __enter__ and __exit__
    """

    def __init__(self):
        """return a generator that yields the current datetime"""
        self.timer = self.getTimer()


    def getTimer(self):
        """yield the current time"""
        while True:
            yield datetime.datetime.now()

    def __enter__(self):
        """this function is executed when the context is initialized"""
        print('welcome to the Timer context manager')
        
        # we should return an object here which is used in the context
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """this function is execute when the code block that the 
        context manager wraps exit.
        the params are set depending on how the code block exited,
        if there is an exception then the three position params would be passed"""
    
        if exc_type is not None:
            print("\nThe code block exited due to an exception, here are the details \n exc_type: {} \n exc_value: {} \n traceback: {} \n".format(exc_type, exc_value, traceback))
        print('Thanks for using the Timer context manager')



# play with TimerContextManager

with TimerContextManager() as timerContext:
    for i in range(10):
        print("Current Time: {}".format(next(timerContext.timer)))


with TimerContextManager() as timerContext1:
    a/1