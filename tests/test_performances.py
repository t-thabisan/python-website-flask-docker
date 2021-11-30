import pytest, threading
from app import app
from time import perf_counter

list_times = []

def thread_task(lock):
    # ACQUIRE
    lock.acquire()
    # START CLOCK
    start = perf_counter()
    # GET REQUEST
    app.test_client().get('/the_mean?the_list=1,2,3')
    # END CLOCK
    end = perf_counter()
    # RELEASE LOCK
    lock.release()
    # ADD REQUEST TIME 
    list_times.append(end-start)
    
def test_the_mean_response_time():
    # CREATING A LOCK
    lock = threading.Lock()
    
    # START COUNTER
    start = perf_counter()
    
    # creating threads
    for _ in range(1000):
        t = threading.Thread(target=thread_task, args=(lock,))
        t.start()
        t.join()
    
    # END COUNTER
    end = perf_counter()
    
    # PERFORMANCES
    total_duration = end-start
    average_time = sum(list_times)/ len(list_times)
    total_request = len(list_times)
    
    # AVERAGE RESPONSE TIME < 100 MS : 0.1s = 100ms
    assert average_time < 0.1
    
    # 1000 REQUESTS IN A SECOND
    assert total_duration < 1
    assert total_request == 1000