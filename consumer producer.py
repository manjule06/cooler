

import queue
import random
import threading
import time


class ProducerConsumer:
    def __init__(self, buffer_size=5, max_items=10):
        self.buffer = queue.Queue(buffer_size)
        self.lock = threading.Lock()
        self.empty = threading.Semaphore(buffer_size)
        self.full = threading.Semaphore(0)
        self.exit_flag = False
        self.items_produced = 0
        self.items_consumed = 0
        self.max_items = max_items

    def produce_item(self):
        """Simulate producing an item."""
        return random.randint(1, 1000)

    def producer(self):
        """Producer thread function."""
        try:
            while self.items_produced < self.max_items:
                if self.exit_flag:
                    break
                item = self.produce_item()
                self.empty.acquire()  # Wait for an empty slot in the buffer
                with self.lock:
                    self.buffer.put(item)
                    print(f"Producer Produced: {item}")
                    self.items_produced += 1
                    print(f"Current Buffer: {list(self.buffer.queue)}")
                self.full.release()  # Signal that a slot is filled
                time.sleep(random.random())
        except KeyboardInterrupt:
            self.exit_flag = True
            print("Producer interrupted. Exiting gracefully...")

    def consume_item(self):
        """Simulate consuming an item."""
        with self.lock:
            if not self.buffer.empty():
                return self.buffer.get()
            else:
                return None

    def consumer(self):
        """Consumer thread function."""
        try:
            while self.items_consumed < self.max_items:
                if self.exit_flag:
                    break
                self.full.acquire()  # Wait for a filled slot in the buffer
                item = self.consume_item()
                if item is not None:
                    print(f"Consumer consumed: {item}")
                    self.items_consumed += 1
                    print(f"Current Buffer: {list(self.buffer.queue)}")
                self.empty.release()  # Signal that a slot is emptied
                time.sleep(random.random())
        except KeyboardInterrupt:
            self.exit_flag = True
            print("Consumer interrupted. Exiting gracefully...")

    def run_threads(self):
        """Create and start producer and consumer threads."""
        producer_thread = threading.Thread(target=self.producer)
        consumer_thread = threading.Thread(target=self.consumer)

        producer_thread.start()
        consumer_thread.start()

        producer_thread.join()
        consumer_thread.join()

        print("All items produced and consumed.")

if __name__ == "__main__":
    try:
        pc = ProducerConsumer(buffer_size=5, max_items=10)
        pc.run_threads()
    except KeyboardInterrupt:
        print("Program terminated by user. Exiting gracefully...")

