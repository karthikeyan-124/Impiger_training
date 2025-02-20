import numpy as np
import time

arr1 = np.random.randint(0, 100, 1000000)
print(arr1)

def add_num(arr):
    sum1 = 0
    for i in arr:
        sum1 += i
    return sum1


start = time.time()
loop_sum = add_num(arr1)
loop_time = time.time() - start
print(f"Manual sum: {loop_sum}")
print(f"Time taken by manual sum: {loop_time:.6f} seconds")


start = time.time()
numpy_sum = np.sum(arr1)
numpy_time = time.time() - start
print(f"NumPy sum: {numpy_sum}")
print(f"Time taken by NumPy sum: {numpy_time:.6f} seconds")


time_difference = loop_time - numpy_time
print(f"Time difference (Manual - NumPy): {time_difference:.6f} seconds")

if loop_time < numpy_time:
    print("loop sum is faster.")
else:
    print("NumPy sum is faster.")



