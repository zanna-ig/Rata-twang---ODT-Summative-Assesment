from machine import Pin, PWM
import time

# Initialize PWM on GPIO 4 and 5 at 50Hz
servo1 = PWM(Pin(4), freq=50)

def move_servos(angle):
    # Map 0-180 degrees to ~26-123 duty cycle
    duty = int((angle / 180 * 97) + 26)
    servo1.duty(duty)

try:
    # 1. Move to 0 degrees
    print("Moving to 0°")
    move_servos(0)
    time.sleep(1) # Wait for physical movement
    
    # 2. Move to 180 degrees
    print("Moving to 90°")
    move_servos(90)
    time.sleep(3)
    
    # 3. Move back to 0 degrees
    print("Returning to 0°")
    move_servos(0)
    time.sleep(1)
 
finally:
    # Turn off PWM to save power and stop jitter
    servo1.deinit()
    servo2.deinit()
    print("Done.")
