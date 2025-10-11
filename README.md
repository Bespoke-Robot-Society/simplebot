# SimpleBot

Bespoke Robot Society's original design for kids, students, or cost-sensitive tinkerers.

![Image of SimpleBot](https://raw.githubusercontent.com/Bespoke-Robot-Society/simplebot/refs/heads/master/images/simplebot.jpeg)

Goals:

* Control a basic, multipurpose teaching robot with the Pi Pico (or Pico W).
* Demonstrate **optical odometry** - measuring the distance wheels turn by counting pulses on light sensors.
* Demonstrate **line following** - steer the robot in response to reflectance sensors that give the position of the line.
* Leave pins open on the microcontroller for additional upgrades.
* **Do not exceed $20 in price, with batteries included.**

## Hardware

Simplebot is based on the "Arduino Smart Car" kit that can be found on Amazon or Aliexpress. This provides a caster wheel, two yellow "TT" motors with optical encoder wheels and actual wheels, a power switch, and a 4xAA battery case. (~$6)

For line detectors, a generic "Infrared Obstacle Avoidance Sensor" module can be found in the US for 20 for $10 - SimpleBot requires two ($1).

Microcontroller - Raspberry Pi Pico ($4) or Raspberry Pi Pico W ($6).

Motor Controller - The TB6612FNG dual H-bridge module. You might be able to find this for $1 or less from overseas, but 3 for $9 is available in the US. ($3)

The optical encoder module requires one LED, one photoresistor, five resistors, and one LM393 chip for both. I don't know the prices for these, as I had them on hand.

an MPU6050 (Accelerometer/gyroscope) and nRF24l01 (2.4GHz radio module) are included on the circuit board, but haven't been tested or programmed yet. These occupy the I2C and SPI buses respectively, and would play well with some additional sensors (at the cost of spare pins for more SPI devices).

## Circuit Board

A through-hole (THT) PCB design is available for easy assembly.

![PCB Schematic](https://raw.githubusercontent.com/Bespoke-Robot-Society/simplebot/refs/heads/master/images/PCB_schematic.png)

The PCB integrates:
- Raspberry Pi Pico microcontroller (or compatible)
- TB6612FNG motor driver (or external H-bridge support)
- Buck converter for power regulation
- LM393-based optical encoder circuit
- Headers for nRF24L01 radio and MPU6050 IMU
- 4 sensor headers for expansion
- Analog and digital GPIO breakouts

See [PCB_GUIDE.md](PCB_GUIDE.md) for detailed PCB documentation.

See [ASSEMBLY_GUIDE.md](ASSEMBLY_GUIDE.md) for mechanical assembly instructions. 

## Software

Copy the included files to your Pi Pico by USB cable. I used Thonny to test the robot's programs.

# Future Work

Should I switch to an off-the-shelf optical encoder module, or should I build a custom line detecting sensor?

Printed circuit boards:

* Through hole soldering kit
* a board-on-board PCB - same layout as the protoboard, but soldered flat together.
* a custom PCB that uses the ICs from the modules directly

SimpleBot is unfortunately too large for standard micromouse mazes, so a "simplebot mini" seems to be in order.
