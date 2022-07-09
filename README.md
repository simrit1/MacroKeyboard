# MacroKeyboard #
## Setup ##

1. Download [Zadig](https://zadig.akeo.ie/)
2. In Zadig go to Options and enable "List all devices"
3. Search for your device and select it
4. In the row that says "Driver" choose WinUSB
5. Click "Replace driver"
6. Write down the first and second Number in the USB ID Row (The first Number is the Vendor id and the second the product id)
7. Place the two in the corresponding variables in main.py (add 0x before them)

- if everything worked you should see the output array change as you press keys on your second keyboard
- now you can catch that output and add your own functions and the end of the code
