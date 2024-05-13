import threading
import time
import random
import queue

buffer_size = 5
buffer = queue.Queue(buffer_size)
lock = threading.Lock()
items_produced = 0
items_consumed = 0
max_items = 10
empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)

exit_flag = False  # Flag to indicate when to exit the threads

def producer():
    global items_produced, exit_flag
    try:
        while items_produced < max_items:
            if exit_flag:  
                break
            item = random.randint(1, 1000)
            empty.acquire()  
            with lock:
                buffer.put(item)
                print(f"Producer Produced: {item}")
                items_produced += 1
                print(f"\nCurrent Buffer: {list(buffer.queue)}\n")
            full.release()  
            time.sleep(random.random())
    except KeyboardInterrupt:
        exit_flag = True
        print("Producer interrupted. Exiting gracefully...")

def consumer():
    global items_consumed, exit_flag
    try:
        while items_consumed < max_items:
            if exit_flag:  
                break
            full.acquire()  
            with lock:
                item = buffer.get()
                print(f"Consumer consumed: {item}")
                items_consumed += 1
                print(f"\nCurrent Buffer: {list(buffer.queue)}\n")
            empty.release()  
            time.sleep(random.random())
    except KeyboardInterrupt:  
        exit_flag = True
        print("Consumer interrupted. Exiting gracefully...")

try:
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("All items produced and consumed.")
except KeyboardInterrupt:
    exit_flag = True
    print("Program terminated by user. Exiting gracefully...")
