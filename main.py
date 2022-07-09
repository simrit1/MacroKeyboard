import usb.core
import usb.util
import os


VENDOR_ID = 0x413C #Example ID
PRODUCT_ID = 0x2105 #Example ID

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
device.set_configuration()
endpoint = device[0][(0,0)][0]
while True:
    attempts = 10
    data = None
    while data is None and attempts > 0:
        try:
            data = device.read(endpoint.bEndpointAddress,
                               endpoint.wMaxPacketSize)
        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):
                attempts -= 1
                continue

    i = 2 #Might be different for your device
    print(data[i])
    if data[i] != 0: 
        print("Data:", data[i])
        if data[i] == 4:
            os.system("start chrome")
        elif data[i] == 5:
            os.system("start firefox")
        elif data[i] == 6:
            os.system("start https://github.com")
        #Add your functions here

