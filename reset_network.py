import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# Disconnect from any current network
wlan.disconnect()
print('Disconnected from networks')
# This clears stored credentials
time.sleep(2)
print('Network credentials cleared')


# Disable both interfaces
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
wlan.active(False)
ap.active(False)
print('Network interfaces disabled')
time.sleep(2)
# Re-enable station mode
wlan.active(True)
print('Station mode re-enabled')
time.sleep(2)
print('Network reset complete')
