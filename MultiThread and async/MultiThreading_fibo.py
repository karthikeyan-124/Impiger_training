import threading
import time

def fibo(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(f"Fibonacci sequence for {n}: {fib}")

#----Method-1----
# thread_1 = threading.Thread(target=fibo, args=(10,))
# thread_2 = threading.Thread(target=fibo, args=(15,))
# thread_3 = threading.Thread(target=fibo, args=(20,))
# thread_4 = threading.Thread(target=fibo, args=(25,))
# thread_5 = threading.Thread(target=fibo, args=(30,))

# thread_1.start()
# thread_2.start()
# thread_3.start()
# thread_4.start()
# thread_5.start()
#
# thread_1.join()
# thread_2.join()
# thread_3.join()
# thread_4.join()
# thread_5.join()
#
# print("program executed successfully")

#----method-2----

def main():
    values=[10,15,20,25,30]

    for i in values:
        thread = threading.Thread(target=fibo, args=(i,))
        thread.start()
        thread.join()
print(main())



