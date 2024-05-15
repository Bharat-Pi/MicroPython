import network
import urequests
from mfrc522 import MFRC522
from machine import Pin, SPI
from time import sleep

# RFID pin configuration
SCK = 18
MOSI = 23
MISO = 19
SDA = 21
RST = 27

# Initialize RFID reader
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=Pin(MISO))
rfid = MFRC522(spi, Pin(SDA), Pin(RST))

# Wi-Fi credentials
ssid = "smile123"
password = "123456789"

# ThingSpeak settings
server = "http://api.thingspeak.com/update"
api_key = "1ZQ9LAB3G9CYY6GA"

# Valid UIDs and corresponding student names
valid_uids = [
    [0xA3, 0x57, 0xB3, 0x30],  # UID of card 1
    [0x53, 0x15, 0x57, 0xC8],  # UID of card 2
    # Add more valid UIDs here
]

student_names = [
    "Bharatpi",  # Name of card 1
    "Welcome",   # Name of card 2
    # Add more student names here
]

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        sleep(0.5)
        print("Connecting to WiFi...")
    print("WiFi connected")
    print("IP address:", wlan.ifconfig()[0])

# Send data to ThingSpeak
def send_to_thingspeak(rfid, student_name):
    url = "{}?api_key={}&field1={}&field2={}".format(server, api_key, rfid, student_name)
    response = urequests.get(url)
    print("Response payload:", response.text)
    response.close()

# Read RFID tags
def read_rfid():
    print("Place your card to the reader")
    while True:
        (status, _) = rfid.request(rfid.REQIDL)
        if status == rfid.OK:
            (status, uid) = rfid.anticoll()
            if status == rfid.OK:
                rfid_str = "".join("{:02X}".format(i) for i in uid)
                print("RFID tag:", rfid_str)
                
                # Match the UID
                student_name = "Unknown"
                for i, valid_uid in enumerate(valid_uids):
                    if uid == valid_uid:
                        student_name = student_names[i]
                        break
                print("Student name:", student_name)
                
                # Send data to ThingSpeak
                send_to_thingspeak(rfid_str, student_name)
                sleep(10)  # Wait 10 seconds before next read

# Main function
def main():
    connect_wifi()
    read_rfid()

if __name__ == "__main__":
    main()
