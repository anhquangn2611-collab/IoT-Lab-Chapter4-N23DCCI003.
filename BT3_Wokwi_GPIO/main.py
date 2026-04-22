import machine
import dht
import time

# Cài đặt chân cảm biến
dht_sensor = dht.DHT22(machine.Pin(15))
trigger = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(13, machine.Pin.IN)

def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = time.ticks_us()
    while echo.value() == 1:
        signalon = time.ticks_us()
        
    timepassed = signalon - signaloff
    return (timepassed * 0.0343) / 2

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        dist = get_distance()
        
        # In ra định dạng CSV để khớp với bài 5
        print(f"00:00:00,{temp},{hum},{dist},NORMAL")
        
    except OSError as e:
        print("Failed to read sensor.")
        
    time.sleep(2) 
