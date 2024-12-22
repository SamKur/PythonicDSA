from datetime import datetime, timedelta
import pytz

dt = datetime.now()
print(dt)  # e.g., 2024-12-21 10:00:00.123456
# Set time zone
timezone = pytz.timezone("Asia/Kolkata")
localized_dt = timezone.localize(dt)
print(localized_dt)  # e.g., 2024-12-21 10:00:00+05:30



# Define the timezone
timezone = pytz.timezone("America/New_York")
# A datetime just before DST transition
# On 2024-03-10, DST starts in New York, and clocks jump from 02:00 to 03:00
dt = datetime(2024, 3, 10, 1, 30, 0)
localized_dt = timezone.localize(dt)
# Add 2 hours (crossing the DST boundary)
new_dt = localized_dt + timedelta(hours=2)
print("Without normalize:", new_dt)  # DST not applied
# Normalize to apply the correct DST adjustment
normalized_dt = timezone.normalize(new_dt)
print("With normalize:", normalized_dt)  # Correct DST adjustment
