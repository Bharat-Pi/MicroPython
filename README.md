#  Downloading & Installing the uPyCraft IDE – for Windows PC Instructions

There are different firmwares that you can use to program the ESP32 boards. If you want to program the ESP32 board using the MicroPython firmware, we recommend using uPyCraft IDE/Thonny IDE. uPyCraft IDE runs in any major operating system. here we’ll show you how to install the uPyCraft IDE for MicroPython on a Windows PC.

Before installing uPyCraft IDE, make sure you have the latest version of Python installed in your computer. If you don’t, follow the next instructions to install Python.

# you can buy Bharat Pi boards on Bharat pi website --> https://bharatpi.net/shop/ , AND on Amazon website.

# Installing Python – Windows PC

1. Go to the Python Downloads page: www.python.org/downloads and download the installation file.
   
     ![Screenshot (2)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/94663d56-7a77-4d16-895d-08ecf2a1f65c)


2. After a few seconds, you should have a file called python-3.12.1.exe file in your computer. Double-click the file to open it.
3. Enable the option at the bottom "Add Python 3.12 to PATH". Then, press the “Install Now” button.
4. Wait a few seconds while the software completes the installation process....
5. When it’s done, you should see the message "Setup was successful" then you can close that window.

# Installing uPyCraft IDE – Windows PC

As mentioned before,we’ll be using uPyCraft IDE to program the ESP32 or ESP8266 boards using the MicroPython firmware. In our opinion, uPyCraft IDE is the easiest way of programming ESP based boards with MicroPython at the moment.

1. To download uPyCraft IDE for Windows go to this link https://randomnerdtutorials.com/uPyCraftWindows.
2. After a few seconds you should see a similar file (uPyCraft_V1.exe) in your Downloads folder Double-click that file.
3. A new window opens with the uPyCraft IDE software, We’ll be using this software to flash our ESP based boards with MicroPython firmware as well as to program the boards.
   
   ![Screenshot (3)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/136fe4af-e2e1-4e28-9853-c9c754178c42)



   
# Flash/Upload MicroPython Firmware to ESP32

With uPyCraft IDE installed in your computer, you can easily flash your ESP32 boards with the MicroPython firmware.

# Downloading the MicroPython Firmware

1. To download the latest version of MicroPython firmware for the ESP32, go to the MicroPython Downloads page https://micropython.org/download/ and scroll all the way down to the ESP32 section select ESP32/WROOM

   ![Screenshot (4)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/9cd6cc38-47c8-4f29-8c44-27bd2dae44a5)


2. Download the ESP32.bin file – for example: esp32-20181007-v1.9.4-631-g338635ccc.bin.

   ![Screenshot (5)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/e1994fe8-d297-4f1e-9eaa-00ed11dd5ddf)



   
# Selecting Serial Port in uPyCraft IDE
Go to Tools > Serial and select your ESP32 COM port.

   ![Screenshot (6)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/96048276-da8c-4c61-8208-0f8e715e7136)



## Important: if you plug your ESP32 board to your computer, but you can’t find the ESP32 Port available in your uPyCraft IDE, it might be one of these two problems: 1. USB drivers missing OR 2. USB cable without data wires.

# USB drivers for our boards 
-->goto this link and dowload the drivers from here for our BharatPi boards-> https://wch-ic.com/downloads/CH341SER_ZIP.html


1. If you don’t see your ESP’s COM port available: 
--> This means you don’t have the USB drivers installed. Take a closer look at the chip next to the voltage regulator on board and check its name.
--> after checking the name Go to Google and search for your specific chip to find the drivers and install them in your operating system.
--> After they are installed, restart the uPyCraft IDE and you should see the COM port in the Tools menu.
   
2. If you have the drivers installed, but you can’t see your device, double-check that you’re using a USB cable with data wires:
USB cables from powerbanks often don’t have data wires (they are charge only). So, your computer will never establish a serial communication with your ESP32. Using a proper USB cable should solve your problem.


# Selecting the Board in uPyCraft IDE
Go to Tools > Board > so make sure you select the "esp32" option:

 ![Screenshot (7)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/6ab3a565-86f2-48e1-823d-bdbb0b56ec6b)



1. Finally, go to Tools > BurnFirmware menu to flash your ESP32 with MicroPython.

   ![Screenshot (8)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/66f436a0-5ae1-42b2-bc84-cd744ae71e35)


2. Select all these options to flash the ESP32 board:
  --> board: esp32
  --> burn_addr: 0x1000
  --> erase_flash: yes
  --> com: COMX (in our case it’s COM4)
  --> Firmware: Select "Users" and choose the ESP32 .bin file downloads After pressing the "Choose" button, navigate to your Downloads folder and select the ESP32.binfile.

    ![Screenshot (9)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/86cac377-bd3c-4f09-8a1a-7a778cca82cd)



3. Having all the settings selected, hold-down the "BOOT/FLASH" button in your ESP32 board. 
4. While holding down the "BOOT/FLASH", click the "ok" button in the burn firmware window.
5. When the "EraseFlash" process begins, you can release the "BOOT/FLASH" button. After a few seconds, the firmware will be flashed into your ESP32 board.

    ![Screenshot (11)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/607e4890-04e9-485a-a0a8-ad46b74a3cf9)



Note: if the "EraseFlash" bar doesn’t move and you see an error message saying "erase false/update false", it means that your ESP32 wasn’t in flashing mode. You need to repeat all the steps described earlier and hold the "BOOT/FLASH" button again to ensure that your ESP32 goes into flashing mode.
  
![Screenshot (10)](https://github.com/SnehaChandrashekhar/MicroPython-Projects/assets/159817964/cd60b2e8-01bb-46eb-8979-9fe93b627dea)


## NOTE:if you are not able to download the PyCraft IDE(it will not support for some windows) we have alternative for that i.e Thonny IDE

# THONNY IDE
# Downloading & Installing the Thonny IDE – for Windows PC Instructions

If you want to program your ESP32 board with MicroPython firmware, it’s very handy to use an IDE in this guide, we’ll introduce you to Thonny IDE.
We’ve experimented with several IDEs to program the ESP32 boards using MicroPython, and Thonny seemed a good choice. Although there are some bugs, it is constantly being updated and improved.
It allows you to program your ESP32 boards with MicroPython, and it is compatible with Windows, Mac and Linux.

# you can buy Bharat Pi boards on Bharat pi website --> https://bharatpi.net/shop/ , AND also on Amazon website.

# What is MicroPython?

MicroPython is a Python 3 programming language re-implementation targeted for microcontrollers and embedded systems. MicroPython is very similar to regular Python The most significant difference between Python and MicroPython is that MicroPython was designed to work under constrained conditions.
Because of that, MicroPython does not come with the entire pack of standard libraries and few exceptions. It only includes a small subset of the Python standard libraries, but it includes modules to easily control and interact with the GPIOs, use Wi-Fi, and other communication protocols.

# Installing Thonny IDE :-

To install Thonny on your Windows PC, follow the next instructions:

1. Go to https://thonny.org

![Screenshot (41)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/4a2d69ae-ed29-42d0-b8d3-e5a098879e06)


2. Download the latest version for Windows and wait a few seconds while it downloads.

3. Run the .exe file.

4. Follow the installation wizard to complete the installation process. You just need to click on Next.

5. After completing the installation open Thonny IDE a page should open like below shown.

![image](https://github.com/Bharat-Pi/MicroPython/assets/167289991/77200e24-3e84-4ddc-be4b-c7b323539384)

![Screenshot (53)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/c0adb9e8-2cea-4661-bee2-ff7481f3d4ec)



# How to Flash MicroPython firmware:-

MicroPython isn’t flashed into the ESP32 boards by default. The first thing you need to do is to start programming your boards with MicroPython flash/upload/burn the firmware.

There are different ways in which you can do that:
Thonny IDE comes with a tool that allows you to quickly install MicroPython firmware on your board. 

# Downloading MicroPython Firmware :-

1. To download the latest version of MicroPython firmware for the ESP32, go to the MicroPython Downloads page https://micropython.org/download/ and scroll all the way down to the ESP32 section.
2. Select the type of board you’re using select ESP32/WROOM.

![Screenshot (39)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/110c6a20-327e-4b33-aa4d-d2f4c50807a6)

You should see a similar web page (see figure below) with links to download .bin files. Download the latest release.

![Screenshot (40)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/7e23ab61-a235-4fbb-9632-253066b527eb)

The downloaded file will go to the Downloads folder, Continue reading to learn how to flash the firmware on your boards.


# Flashing MicroPython Firmware using Thonny IDE :-

In this section you’ll learn how to flash MicroPython firmware on your boards using Thonny IDE, Follow the next steps:

1. Connect your ESP32 board to your computer.

2. Open Thonny IDE, Go to Tools -> Options -> Interpreter.
   
![Screenshot (54)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/42b022b7-a2fd-46c5-99b5-32159c782f56)

3) Select the interpreter you want to use accordingly to the board you’re using and select the COM port your board is connected to and Finally, click on the link Install or update firmware.

![Screenshot (55)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/869053d6-65e2-40f3-9eb9-014280a199ff)

4) Select the port once again, and then click on the Browse button to open the .bin file with the firmware you’ve downloaded on the previous step. Select the options as shown in the picture below and finally click on Install.After a few seconds, the installation should be completed.

![Screenshot (46)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/5f65b9e8-33af-47b3-bcbe-f8a702cc78ee)

(OR)
You can do this steps using -> configure interpreter in the bottom of the thonny ide screen as shown in the image below.

 ![Screenshot (47)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/b78debbc-8dff-4fcc-bae1-d7f1b37e0972)

# Testing the Installation :-

## Important: before testing the installation, your ESP32 board needs to be flashed with MicroPython firmware (see the above steps for flashing).

Connect the board to your computer using a USB cable.
To test the installation, you need to tell Thonny that you want to run MicroPython Interpreter and select the board you are using.

1. Go to Tools > Options and select the Interpreter tab. Make sure you’ve selected the right interpreter for your board as well as the COM port.
You can also select the "Try to detect automatically"  option, but only if you just have one board connected to your computer at a time. Otherwise, select the specific port for the board you’re using.
2. Thonny IDE should now be connected to your board and you should see the prompt on the Shell.
3. Type the command help() in the Shell and see if it responds back.
If it responded back, everything is working fine. Now, you can send a few more commands to test.

![Screenshot (52)](https://github.com/Bharat-Pi/MicroPython/assets/167289991/b408781c-94ec-401c-93d1-e11b530abb5d)
