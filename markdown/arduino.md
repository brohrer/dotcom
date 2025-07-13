# Getting started with Arduino

## Why Arduino?

Arduino gives builders a gift--a way to bridge the gap between
code and the physical world. At the heart of every Arduino board is a
programmable [microcontroller](https://en.wikipedia.org/wiki/Microcontroller)
chip with names like
[ATMega2560](http://www.atmel.com/Images/Atmel-2549-8-bit-AVR-Microcontroller-ATmega640-1280-1281-2560-2561_datasheet.pdf)
and
[ARM-Cortex-M](https://en.wikipedia.org/wiki/ARM_Cortex-M).
If you imagine a laptop, take away the screen and the keyboard, and
shrink everything else down to a miniature scale, you won't be too far away
from a microcontroller. 

Microcontrollers com in a single integrated circuit, like this.

![Renesas RA4M1, a.k.a. Arm® Cortex®-M4](images/arduino/arm_cortex_m4.png "Renesas RA4M1, a.k.a. Arm® Cortex®-M4")

Arduino helps out hobbyists by putting them on a larger board like this.

![Arm Cortex microcontroller in its native environment, an Arduino UNO R4 Minima
](images/arduino/arduino_uno_r4.png "Arm Cortex microcontroller in its native environment, an Arduino UNO R4 Minima")

The Arduino board gives easy access to the tiny pins of the IC and makes it
possible to plug in standard connectors for power and USB communications.

What makes the microcontroller so powerful isn't its computational capabilities
(they are pretty pathetic compared to the processor in your phone). What makes
it special is the large collection of input/output pins.

- **Digital I/O** pins which can pass high (3.3 or 5 Volts
depending on the board) and low (0 Volt) signals
to another circuit, as well as read high and low signals from them.
- **Analog input** pins, which use an analog-to-digital converter to read
the voltage from an outside source to a fine resolution.
- **Analog output** (DAC) pins, which use a digital-to-analog converter to sustain
a pin at any voltage from a near-continuous range.
- **PWM** ([Pulse-width modulated](https://en.wikipedia.org/wiki/Pulse-width_modulation))
pins, which approximate an analog voltage by rapidly switching
back and forth between high and low voltages. For example, to maintain an
average voltage of 2.2 Volts, a PWM signal will switch between 0 and 3.3 Volts,
spending two-thirds of its time at 3.3 V and one-third of its time at 0 V.
- Specialized communication protocol pins, like UART, CAN, I2C, and SPI.

### Shields and Carriers

A microcontroller on its own is cool in concept, but isn't particularly useful.
Arduino makes it easy to extend them by adding on other components.
These extension boards can be stacked below (**carriers**) or above
(**shields**) the Arduino boards on rows of carefully laid out pins.
Shields seem to be much more common than carriers.

![A stack of Arduino boards
](images/data_eng_for_beginners/arduino_stack.jpg "from https://www.detailedpedia.com/wiki-Arduino")

Shields give you a huge Swiss Army knife of tools

- Ethernet
- WiFi (although some boards come with this)
- Extra memory
- Relay switches
- Motor controllers
- Temperature other environmental sensors
- Inertial measurement units
- Microphone and some speech processing
- Camera and some vision processing
- LED and LCD displays

### Models and form factors

There are a handful of different form factors with names like UNO, MKR,
Portenta, Nano, and Giga. 
Here is [a really helpful breakdown of the different boards
](https://www.pleasedontcode.com/blog/arduino-boards-comparison-a-selection-guideline)
and some of the shields and carriers that go with them.
When in doubt, start with
[the latest UNO base](https://store.arduino.cc/collections/uno/products/uno-r4-minima)
and build from there. UNO
is meant to be a somewhat universal starting point.

Most Arduino boards and shield are physically compatible, although
[this post on the Arduino forum
](https://arduino.stackexchange.com/questions/4456/are-all-arduino-shields-compatible-with-all-arduino-boards)
strong encourages us to check the voltage (3.3 V vs 5 V) compatibility
and the software library compatibility as well.

Because all Arduino designs are open, there are a large number of
[Arduino-compatible
](https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems),
Arduino-adjacent, and Arduino spinoff boards and shields.
It can all get a little overwhelming. It's the downside of not having a
single corporate overlord dictating a conveniently consumable lineup
of marketing-approved SKUs. Read item descriptions and blog posts carefully,
prepare for some thoughtful trial and error, and embrace the anarchy.

### The IDE

The easiest way to start giving the microprocessor instructions to execute
is to use the Arduino Integrated Development Environment (IDE).
You can [download it](https://www.arduino.cc/en/software/) for Linux, MacOS,
and Windows. It's free thanks to the generous folks behind it, but consider
leaving a donation to keep the lights on.

After you install and open it, the IDE takes you right to a code editor
window.

![Screenshot of the Arduino IDE showing a code editing window
](images/arduino/arduino_ide.png "The starting screen on the Arduino IDE")

There are two major versions of IDE - 1.x and 2.x.
Version 1 is a little more bare bones, version 2 has fancy touches
like autocomplete, function definitions, and dark mode. They'll both let you
do what you need to do. You can try either or both and switch between them.

I also recommend bookmarking 
[the Arduino IDE documentation page](https://docs.arduino.cc/software/ide/),
which covers both versions.

![Screenshot of the Arduino IDE documentation page
](images/arduino/arduino_ide_docs.png)


