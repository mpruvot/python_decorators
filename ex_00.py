import time

def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
    return wrapper
  
@get_time
def say_hello():
    print("coucou je suis Marius")
    
say_hello()
    