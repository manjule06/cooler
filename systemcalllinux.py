import os


# Process related system calls: fork, wait, exec*, kill
def process_related_system_calls():
    pid = os.fork()

    if pid == 0:
        print("Child process with PID:", os.getpid())
        os.execlp("ls", "ls", "-l")  
        os._exit(0)
    else:
        print("Parent process with PID:", os.getpid())
        os.wait()
        print("Child process finished")
        
       
    
# File related system calls: open, read, write, close
def file_related_system_calls():
    file_name = "test.txt"
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

    os.write(fd, b"Hello, World!\n")
    os.lseek(fd, 0, os.SEEK_SET)

    data = os.read(fd, 100)
    print("Data read from file:", data.decode())

    os.close(fd)


# Protection system call: chmod
def protection_system_call():
    file_name = "test.txt"
    mode = 0o644  
    os.chmod(file_name, mode)
    print("Changed permissions of", file_name, "to", oct(os.stat(file_name).st_mode)[-3:])


if __name__ == "__main__":
    print("Demonstrating process related system calls:")
    process_related_system_calls()

    print("\nDemonstrating file related system calls:")
    file_related_system_calls()

    print("\nDemonstrating protection system call:")
    protection_system_call()
