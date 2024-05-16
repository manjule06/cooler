import threading

mutex = threading.Lock()
count_mutex = threading.Lock()

def reader(num, filename):
    if(mutex):
        print(f"Reader {num} is Checking for lock...")
        print("\n")
    with mutex:
        with open(filename, 'r') as file:
            data = file.read()
        print(f"Reader {num} acquired lock, reading data: \n{data.strip()}")
        print(f"Reader {num} released the lock")
        print("\n")

def writer(num, filename):
    with mutex:
        print(f"Writer {num} is Checking for lock...")
        with open(filename, 'a') as file:
            file.write(f"\nData written by writer {num} Hello there this is writer {num}")
        print(f"Writer {num} acquired lock and wrote to file")
        print(f"Writer {num} released the lock")
        print("\n")

def main():
    filename = "sample.txt"
    reader_threads = []
    writer_threads = []

    # Ensure file exists and is empty
    open(filename, 'w').close()

    for i in range(5):
        writer_threads.append(threading.Thread(target=writer, args=(i, filename)))
        reader_threads.append(threading.Thread(target=reader, args=(i, filename)))
    
    reader_threads[0].start()
    reader_threads[0].join()
    
    writer_threads[0].start()
    writer_threads[0].join()

    writer_threads[1].start()
    writer_threads[1].join()

    reader_threads[1].start()
    reader_threads[2].start()
    reader_threads[1].join()
    reader_threads[2].join()  

    writer_threads[2].start()
    writer_threads[3].start()
    writer_threads[2].join()
    reader_threads[3].start()
    reader_threads[3].join()
    writer_threads[3].join()

if __name__ == "__main__":
    main()
