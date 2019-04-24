import threading
import time

def thread_function():
	for i in range(5):
		time.sleep(1)
		print('Hola5')

th1 = threading.Thread(target=thread_function)
th1.start()

