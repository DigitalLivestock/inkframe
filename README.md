# InkFrame: a Smart Photoframe enabled by a Pimoroni's Inky Impression and Raspberry Pi Zero 2 W written in Python

## Introduction

## Hardware & Setup

### Recomended/Required Hardware
- Photo frame: LOMVIKEN 10x15 cm, IKEA (https://www.ikea.com/se/sv/p/lomviken-ram-svart-80518206/)
- E-Ink display: Inky Impression 5.7", Pimoroni (https://shop.pimoroni.com/products/inky-impression-5-7?variant=32298701324371)
- Temperature and Humidity Sensor: DHT11 (https://www.digikey.se/en/products/detail/adafruit-industries-llc/386/5356713)
- Controller: RPI Zero 2 W, Raspberry Pi (https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
- MicroSD card: Any

### Construction
1. Follow the instructions provided by Pimoroni for connecting RPI Zero 2 W with display here: https://learn.pimoroni.com/article/getting-started-with-inky-impression
2. Remove the backside of the LOMVIKEN photo frame and cut it with a blade knife to ensure flat contact between the Inky Impression PCB and backside. Ensure the buttons are exposed.
3. Connect the DHT11 sensor to the breakout header on the Inky Impression, using direct soldering or with flat cables. I used a small cut prototyping board with headers for a neat and modular fit in the narrow space between the frame and breakout. Connect pins in the following order: RPI-PIN#4 -> DHT11-DATA, RPI-3.3V -> DHT11-VCC and RPI-GND -> DHT11-GND.
4. Prepare MicroSD card and insert into RPI, as instructed in the following link: https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system. I'm using the Raspberry Pi OS 32-bit ported from Debian Bookworm.

## Software & Setup

### Required Software

## Functions

## References
