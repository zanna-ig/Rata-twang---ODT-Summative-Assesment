from machine import Pin
import time

LDR = Pin(18, Pin.IN)
Buzzer = Pin(19, Pin.OUT)

while True:
    time.sleep(0.1)
    sensorTriggered = LDR.value()

    if sensorTriggered == 0:
        print("Light Detected")
        Buzzer.on()      # TURN BUZZER ON
        time.sleep(0.2)
        Buzzer.off()      # TURN BUZZER OFF

    else:
        print("Light Not Detected")
        Buzzer.off()
        
#microphone & motion sensor r flakey

#LDR triggering buzzer