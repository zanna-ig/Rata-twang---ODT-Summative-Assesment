from machine import Pin
import neopixel
import time
import random

# ---------- NEOPIXEL ----------
NUM_LEDS = 16
np = neopixel.NeoPixel(Pin(22, Pin.OUT), NUM_LEDS)

MIN_BRIGHTNESS = 1
MAX_BRIGHTNESS = 20

active_leds = []

# ---------- PICK RANDOM LEDS ----------
def choose_random_leds():
    global active_leds

    np.fill((0, 0, 0))

    num_on = random.randint(1, NUM_LEDS)
    active_leds = []

    # create unique random indices (replacement for random.sample)
    while len(active_leds) < num_on:
        r = random.randint(0, NUM_LEDS - 1)
        if r not in active_leds:
            active_leds.append(r)

    print("LEDs chosen:", active_leds)

# ---------- CHANGE INTENSITY ----------
def update_random_intensity():
    brightness = random.randint(MIN_BRIGHTNESS, MAX_BRIGHTNESS)

    for i in active_leds:
        np[i] = (brightness, 0, 0)

    np.write()
    print("Brightness:", brightness)

# ---------- MAIN LOOP ----------
choose_random_leds()

while True:
    update_random_intensity()
    time.sleep(3)