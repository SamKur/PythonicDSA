from datetime import datetime
from zoneinfo import ZoneInfo


# 1. Get current time in UTC
now = datetime.now(ZoneInfo("UTC"))

# 2. Convert to local timezone
local_time = now.astimezone(ZoneInfo("Asia/Kolkata"))

# 3. Format for display
formatted = local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
print(formatted)  # "2023-10-06 12:30:00 IST+0530"

# 4. Store as ISO 8601
iso_str = local_time.isoformat()

# 5. Parse back to datetime
parsed_dt = datetime.fromisoformat(iso_str)

# 6. Calculate time difference
diff = parsed_dt - now
print(diff.total_seconds())  # Time difference in seconds