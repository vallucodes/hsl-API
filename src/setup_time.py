
import ntptime
import utime

def setup_time(timezone_offset=0):
    try:
        ntptime.settime()

        current_time = utime.time() + (timezone_offset * 3600)
        now = utime.localtime(current_time)
        seconds_now = now[3] * 3600 + now[4] * 60 + now[5]

        print(f"Current time: {now[3]:02d}:{now[4]:02d}:{now[5]:02d}")

        return seconds_now
    except Exception as e:
        print(f"Time sync failed: {e}")
        return None
