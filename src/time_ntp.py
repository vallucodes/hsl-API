import utime
import network
import ntptime

def sync_time_ntp(timezone_offset=0):
    """
    Synchronize time with NTP server
    timezone_offset: hours from UTC (e.g., +2 for EEST, -5 for EST)
    """
    try:
        print("Synchronizing time with NTP server...")
        ntptime.settime()  # This sets UTC time

        # Adjust for timezone if needed
        if timezone_offset != 0:
            current_time = utime.time()
            adjusted_time = current_time + (timezone_offset * 3600)
            # Note: This is a workaround since MicroPython doesn't have timezone support
            # The proper way would be to use the timezone offset when displaying time

        print("Time synchronized successfully!")
        return True
    except Exception as e:
        print(f"Time sync failed: {e}")
        return False

def get_current_time_info(timezone_offset=0):
    """Get current time with timezone adjustment"""
    current_time = utime.time()
    if timezone_offset != 0:
        current_time += timezone_offset * 3600

    time_tuple = utime.localtime(current_time)
    return time_tuple

def get_seconds_since_midnight(timezone_offset=0):
    """Get seconds since midnight with timezone consideration"""
    time_tuple = get_current_time_info(timezone_offset)
    hour, minute, second = time_tuple[3], time_tuple[4], time_tuple[5]
    return hour * 3600 + minute * 60 + second

def get_time():
    # Set your timezone offset (hours from UTC)
    # Examples:
    # Helsinki/Finland: +2 (EET) or +3 (EEST in summer)
    # New York: -5 (EST) or -4 (EDT in summer)
    # London: 0 (GMT) or +1 (BST in summer)
    TIMEZONE_OFFSET = 3

    # Show time before sync
    print(f"Time before sync: {utime.localtime()}")

    # Sync with NTP
    if sync_time_ntp():
        # Show time after sync
        current_time = get_current_time_info(TIMEZONE_OFFSET)
        print(f"Time after sync (with timezone): {current_time}")
        print(f"Formatted time: {current_time[3]:02d}:{current_time[4]:02d}:{current_time[5]:02d}")

        # Get seconds since midnight
        seconds_now = get_seconds_since_midnight(TIMEZONE_OFFSET)
        print(f"Seconds since midnight: {seconds_now}")
    else:
        print("Failed to sync time - check your internet connection")

def setup_time(wifi_ssid, wifi_password, timezone_offset=0):
    """Simple setup function to sync time"""
    # Connect to WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(wifi_ssid, wifi_password)
        while not wlan.isconnected():
            utime.sleep(1)

    # Sync time
    try:
        ntptime.settime()
        print("Time synced successfully!")

        current_time = utime.time() + (timezone_offset * 3600)
        now = utime.localtime(current_time)
        seconds_now = now[3] * 3600 + now[4] * 60 + now[5]

        print(f"Current time: {now[3]:02d}:{now[4]:02d}:{now[5]:02d}")
        print(f"Seconds since midnight: {seconds_now}")

        return seconds_now
    except Exception as e:
        print(f"Time sync failed: {e}")
        return None
