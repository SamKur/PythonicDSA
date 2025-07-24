import time
from datetime import datetime, timezone

# Get timestamp
timestamp = time.time()
time.sleep(2)

# Convert to human-readable format
readable_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
print(f"Timestamp: {timestamp}")
print(f"Readable Time: {readable_time}")


# Get time required to run a program (benchmarking)
def gcd(n, m):
    for i in range(n,0,-1):
        if n%i==0 and m%i==0:
            return i
start = time.perf_counter()
print(gcd(48,18))
end = time.perf_counter()
print("time taken to execute the code: ", end-start)