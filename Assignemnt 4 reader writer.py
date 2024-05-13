import threading
import time

lock = threading.Lock()

waiting_threads = []

def reader(num, filename):
    global waiting_threads
    with lock:
        print(f"\nReader are reading the file.")
        print(f"\nReader {num} acquired lock")
        with open(filename, 'r') as file:
            data = file.read()
        print(f"\nReader {num} reading data: {data.strip()}")
        if threading.current_thread() in waiting_threads:
            waiting_threads.remove(threading.current_thread())

def writer(num, filename):
    global waiting_threads
    with lock:
        print(f"\nWriter {num} acquired lock")
        print(f"\nWriter {num} is writing...")
        with open(filename, 'a') as file:
            file.write(f"\nData written by writer {num}")
        print(f"\nWriter {num} wrote to file")
        if threading.current_thread() in waiting_threads:
            waiting_threads.remove(threading.current_thread())
    print(f"\nWriter {num} released lock")

def main():
    global waiting_threads
    filename = "sample.txt"
    reader_threads = []
    writer_threads = []

    # Ensure file exists and is empty
    open(filename, 'w').close()

    for i in range(5):
        print(f"\nWriter {i} is waiting")  # Print waiting statement
        writer_thread = threading.Thread(target=writer, args=(i, filename))
        if threading.current_thread() not in waiting_threads:  # Exclude main thread
            writer_thread.start()
        time.sleep(0.1)  # Introduce a small delay between starting writer threads
        waiting_threads.append(writer_thread)

    reader_threads = [threading.Thread(target=reader, args=(i, filename)) for i in range(5)]

    for thread in reader_threads:
        thread.start()
        waiting_threads.append(thread)

    for thread in writer_threads:
        thread.join()

    for thread in reader_threads:
        thread.join()

if __name__ == "__main__":
    main()
