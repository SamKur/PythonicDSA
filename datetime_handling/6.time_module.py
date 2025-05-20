import time
from datetime import datetime, timezone

# Get timestamp
timestamp = time.time()
time.sleep(2)

# Convert to human-readable format
readable_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
print(f"Timestamp: {timestamp}")
print(f"Readable Time: {readable_time}")