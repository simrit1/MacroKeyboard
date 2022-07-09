import usb.core
import usb.util


"""
-Download a program called Zadig(https://zadig.akeo.ie/)
-In Zadig go to Options and enable "List all devices"
-Search for your device and select it
-In the row that says "Driver" choose WinUSB
-Click "Replace driver"
-Write down the first and second Number in the USB ID Row
#The first Number is the Vendor id and the second the product id
-Place the two in the corresponding variables below (add 0x before them)


-if everything worked you should see the output array change as you press keys on your second keyboard
"""


VENDOR_ID = 0x0461 #Example ID
PRODUCT_ID = 0x0010 #Example ID

device = usb.core.find(idVendor=VENDOR_ID,
                       idProduct=PRODUCT_ID)
device.set_configuration() #use the default configuration
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
    print(data) #outputs an array that changes if a key is pressed
