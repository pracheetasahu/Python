import threading
import time

def download_file(name):
    print(name, "download started")
    time.sleep(1)
    print(name, "download completed")

thread1 = threading.Thread(target=download_file, args=("File 1",))
thread2 = threading.Thread(target=download_file, args=("File 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All downloads finished")
