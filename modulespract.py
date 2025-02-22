# import time
# curr_time=time.localtime()
# curr_clock=time.strftime("%H:%M:%S",curr_time)
# print(curr_clock)


# from datetime import datetime
# import pytz

# # Timezone for India Standard Time (IST)
# IST = pytz.timezone('Asia/Kolkata')

# # Timezone for New York (Eastern Time, USA)
# NYC = pytz.timezone('America/New_York')

# # Get the current time in IST (India)
# datetime_ist = datetime.now(IST)

# # Get the current time in New York
# datetime_nyc = datetime.now(NYC)

# # Display formatted date and time in IST
# print("Date & Time in India (IST):", datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

# # Display formatted date and time in New York
# print("Date & Time in New York (USA):", datetime_nyc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))


from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')
USA = pytz.timezone('America/New_york')
datetime_ist = datetime.now(IST)
datetime_nyc = datetime.now(USA)
print("Date & Time in India (IST):", datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
print("Date & Time in New York (USA):", datetime_nyc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))