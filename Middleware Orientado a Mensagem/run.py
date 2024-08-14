import multiprocessing
import multiprocessing.process
from producer import producer
from consumer import consumer
from time import sleep

if __name__ == "__main__":
    p = multiprocessing.Process(target=producer)
    c = multiprocessing.Process(target=consumer)

    p.start()
    sleep(2)
    c.start()

    p.join()
    c.join()
