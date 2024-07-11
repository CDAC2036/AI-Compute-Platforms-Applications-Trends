import numpy as np
import time

# Let's Define the no. of elements
N = 1000000000

# Create NumPy arrays for a and b
a = np.arange(N, dtype=np.float32)
b = np.arange(N, dtype=np.float32)

start_time = time.perf_counter()
c = a + b
end_time = time.perf_counter()

print(c)

execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.4f} seconds")