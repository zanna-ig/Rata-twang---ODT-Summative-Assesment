Project by Rhea and Zanna

Our multiplayer, RATA-TWANG!, game requires its players to take out a randomly generated number (1-3) of cards (tracing sheets) while trying not to trigger of Remy the Rat (from Ratatouille). 

Working Principle:
A Neopixel which is directed at an Light Dependent Resistor (LDR). At the beginning of the game, the tracing sheets obscure the light falling on the LDR, keeping the micro servo motor in its initial position. As sheets are removed, more light falls on the resistor until a point where the LDR is triggered leading to Remy popping up and a buzzer going off. 

Components Used:
1 ESP32
1 Breadboard Power Supply
1 Light Dependent Resistor (LDR)/ Light Sensor
1 Neopixel Ring (16 LEDs)
1 Buzzer
1 Micro Servo Motor

Limitations:
We had initially wanted to have different configurations on the Neopixels, however, since we had to supply it with 3.3V instead of 5V (as a result of several mishaps with the Neopixels before and using someone else's), we kept the Neopixel consistent and messed with some values through (R,G,B) ranges instead.
Our codes for the Neopixel, Buzzer, Servo motor and Light sensor were done by us. The file 'combined codes.py', similarly were done by us as well. However, the code with the Neopixel added was synthesised using Chat.GPT. The random Neopixel intensity code was also done by Chat.GPT (though we could not use it successfully).
