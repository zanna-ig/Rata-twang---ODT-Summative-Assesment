from machine import Pin, PWM
import time
import neopixel

# ---------- PINS ----------
LDR = Pin(18, Pin.IN)
Buzzer = Pin(19, Pin.OUT)
servo1 = PWM(Pin(4), freq=50)

# ---------- NEOPIXEL SETUP ----------
NUM_LEDS = 16
np = neopixel.NeoPixel(Pin(22), NUM_LEDS)

# Turn ALL neopixels red (constant)s
np.fill((255, 0, 0))   # (R, G, B)
np.write()

print("All 16 NeoPixels are Red")

# ---------- SERVO FUNCTION ----------
def move_servos(angle):
    duty = int((angle / 180 * 97) + 26)
    servo1.duty(duty)

# ---------- MAIN LOOP ----------
triggered = False

while True:
    sensorTriggered = LDR.value()

    if sensorTriggered == 0 and not triggered:
        triggered = True
        print("Light Detected!")

        # BUZZER
        Buzzer.on()
        time.sleep(0.5)
        Buzzer.off()

        # SERVO MOVE
        move_servos(0)
        time.sleep(0.3)

        move_servos(90)
        time.sleep(4)

        move_servos(0)
        time.sleep(1)

    elif sensorTriggered == 1:
        triggered = False

    time.sleep(0.1)