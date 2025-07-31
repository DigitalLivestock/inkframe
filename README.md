# InkFrame: a Wireless Photo Frame enabled by a Pimoroni's Inky Impression and Raspberry Pi Zero 2W written in Python

## Introduction

## Hardware Setup
This section presents the involved hardware and assembly instructions.

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
4. Prepare MicroSD card and insert into RPI, as instructed again in the following link: https://learn.pimoroni.com/article/getting-started-with-inky-impression. I'm using the Raspberry Pi OS 32-bit ported from Debian Bookworm. Ensure a WiFi connection will be established are and SSH is enabled.
5. Power the system with the AC/DC adapter.

## System Configuration
This section presents the instructions for how to install required software and how to configure the linux environment.
1. Connect to the RPI via SSH. Instructions are given here again: https://learn.pimoroni.com/article/getting-started-with-inky-impression
2. To the usual sudo apt update and sudo apt upgrade
3. Install git: sudo apt install git
4. Continue following the link above to install the Inky Impression required software.
5. Clone this repository: git clone https://github.com/DigitalLivestock/inkframe.git
6. Enter directory: cd inkframe
7. Activate venv: source ~/.virtualenvs/pimoroni/bin/activate
8. Install dependencies: python -m install -r requirements.txt
9. Create folder for images: mkdir images
10. Add images to folder from new terminal session on host PC: scp \[image folder path on host PC\]pi@\[address\]:\[path to images on pi\] 
11. Test inkframe: python main.py
12. Wait for image to be written on display. Can take some time. Be patient.
13. Systemd setup using the following instructions: https://www.donskytech.com/raspberry-pi-how-to-start-python-script-on-boot/. Instead of led-blink.service, use inkframe.service prepared in the inkframe-directory.

## Functions
This section goes over the available functions of the system.

### Behaviour
- Inkframe program reloads automatically after boot.
- Shuffles images in folder at every restart.
- New image every 30 min. Can be re-configured in src/config.ini
- Shows tempererature and humidity.
- Takes input from Inky Impression display buttons.

### Buttons
- Button A: Move to next image.
- Button B: Re-shuffle images.
- Button C: Reserved.
- Button D: Toggle temperature and humidity HUD visibility.

## References
