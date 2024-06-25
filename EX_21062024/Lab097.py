import time


def time_taken_decorator(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        tt=end_time-start_time
        print(tt)
    return wrapper()




@time_taken_decorator
def logs_function():
    time.sleep(5)
    print("logs of time taken")
