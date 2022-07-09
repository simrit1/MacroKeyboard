# MacroKeyboard #

Turns a second keyboard into a fully customizable macro-keyboard

# **WARNING** #

**!!Might make the keyboard you configure for this unusable!!**

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

## Adding your own Code ##

At the end of the file you can see 3 example functions, to add a new custom function simply 
- copy the elif statement
- append it at the end 
- change the number to the key you want your function to map to
- you can find the value of a key by pressing it on your keyboard and watching the output of the script

Afterwards you can just add code you can add the code you want to be executed whenever that key gets pressed




