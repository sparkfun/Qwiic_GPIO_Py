#-----------------------------------------------------------------------------
# qwiic_gpio.py
#
# Python library for the SparkFun qwiic gpio sensor.
#
# This sensor is available on the SparkFun Environmental Combo Breakout board.
#   https://www.sparkfun.com/products/14348
#
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2019
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem 
#
# More information on qwiic is at https:// www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================

"""
qwiic_gpio
============
Python module for the Qwiic GPIO.

This python package is a port of the existing [SparkFun GPIO Arduino Library](https://github.com/sparkfun/SparkFun_gpio_Arduino_Library)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

"""
#-----------------------------------------------------------------------------

import math
import qwiic_i2c

# Define the device name and I2C addresses. These are set in the class defintion 
# as class variables, making them avilable without having to create a class instance.
# This allows higher level logic to rapidly create a index of qwiic devices at 
# runtine
#
# The name of this device 
_DEFAULT_NAME = "Qwiic GPIO"

# Some devices have multiple availabel addresses - this is a list of these addresses.
# NOTE: The first address in this list is considered the default I2C address for the 
# device.
_AVAILABLE_I2C_ADDRESS = [0x27, 0x26, 0x25, 0x24, 0x23, 0x22, 0x21, 0x20]

# define the class that encapsulates the device being created. All information associated with this
# device is encapsulated by this class. The device class should be the only value exported 
# from this module.

class QwiicGPIO(object):
    """
    QwiicGPIO

        :param address: The I2C address to use for the device. 
                        If not provided, the default address is used.
        :param i2c_driver: An existing i2c driver object. If not provided 
                        a driver object is created. 
        :return: The GPIO device object.
        :rtype: Object
    """
    # Constructor
    device_name         = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Registers
    REG_INPUT_PORT = 0x00
    REG_OUTPUT_PORT = 0x01
    REG_INVERSION = 0x02
    REG_CONFIGURATION = 0x03

    # Status/Configuration Flags
    GPIO_IN = 0
    GPIO_OUT = 1

    GPIO_LO = 0
    GPIO_HI = 1
    
    INVERT = True
    NO_INVERT = False

    inversion_0 =   0
    inversion_1 =   0
    inversion_2 =   0
    inversion_3 =   0
    inversion_4 =   0
    inversion_5 =   0
    inversion_6 =   0
    inversion_7 =   0

    mode_0 =        0
    mode_1 =        0
    mode_2 =        0
    mode_3 =        0
    mode_4 =        0
    mode_5 =        0
    mode_6 =        0
    mode_7 =        0

    out_status_0 =  1
    out_status_1 =  1
    out_status_2 =  1
    out_status_3 =  1
    out_status_4 =  1
    out_status_5 =  1
    out_status_6 =  1
    out_status_7 =  1

    in_status_0 =   0
    in_status_1 =   0
    in_status_2 =   0
    in_status_3 =   0
    in_status_4 =   0
    in_status_5 =   0
    in_status_6 =   0
    in_status_7 =   0

    # Constructor
    def __init__(self, address=None, i2c_driver=None):

        # Did the user specify an I2C address?
        self.address = address if address != None else self.available_addresses[0]

        # load the I2C driver if one isn't provided

        if i2c_driver == None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c == None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver
    # ----------------------------------
    # isConnected()
    #
    # Is an actual board connected to our system?

    def isConnected(self):
        """ 
            Determine if a Qwiic GPIO device is connected to the system..

            :return: True if the device is connected, otherwise False.
            :rtype: bool

        """
        return qwiic_i2c.isDeviceConnected(self.address)

    # ----------------------------------
    # begin()
    #
    # Initialize the system/validate the board. 
    def begin(self):
        """ 
            Initialize the operation of the Qwiic GPIO

            :return: Returns true of the initializtion was successful, otherwise False.
            :rtype: bool

        """
        
        return isConnected()

    #----------------------------------------------------------------
    # setMode()
    #
    # Set the mode (input/output) for all GPIO
    def setMode(self):
        """ 
            Sends all 8 pin modes (input or output) to the GPIO to set all 8 pins. Setting the value to input or output is done using myGPIO.mode_0 = myGPIO.GPIO_OUT

            :return: No return value

        """
        tempData = 0
        tempData &= self.mode_0 << 0
        tempData &= self.mode_1 << 1
        tempData &= self.mode_2 << 2
        tempData &= self.mode_3 << 3
        tempData &= self.mode_4 << 4
        tempData &= self.mode_5 << 5
        tempData &= self.mode_6 << 6
        tempData &= self.mode_7 << 7
        self._i2c.writeByte(self.address, self.REG_CONFIGURATION, tempData)

    #----------------------------------------------------------------
    # getMode()
    #
    # Get the mode (input/output) for all GPIO
    def getMode(self):
        """ 
            Updates mode_X variables with values from Qwiic GPIO

            :return: The value of the mode register.
            :rtype: 8 bit unsigned integer

        """
        tempData = self._i2c.readByte(self.address, self.REG_CONFIGURATION)
        self.mode_0 = (tempData & (1 << 0)) >> 0
        self.mode_1 = (tempData & (1 << 1)) >> 1
        self.mode_2 = (tempData & (1 << 2)) >> 2
        self.mode_3 = (tempData & (1 << 3)) >> 3
        self.mode_4 = (tempData & (1 << 4)) >> 4
        self.mode_5 = (tempData & (1 << 5)) >> 5
        self.mode_6 = (tempData & (1 << 6)) >> 6
        self.mode_7 = (tempData & (1 << 7)) >> 7
        return tempData

    #----------------------------------------------------------------
    # setInversion()
    # 
    # Set whether a GPIO will invert an incoming signal

    def setInversion(self):
        """ 
            Send the inversion modes of all pins. This function must be called after editing modes using myGPIO.inversion_0 = myGPIO.INVERT

            :return: No return value

        """
        tempData = 0
        tempData |= self.inversion_0 << 0
        tempData |= self.inversion_1 << 1
        tempData |= self.inversion_2 << 2
        tempData |= self.inversion_3 << 3
        tempData |= self.inversion_4 << 4
        tempData |= self.inversion_5 << 5
        tempData |= self.inversion_6 << 6
        tempData |= self.inversion_7 << 7
        self._i2c.writeByte(self.address, self.REG_INVERSION, tempData)

    #----------------------------------------------------------------
    # getInversion()
    # 
    # Get inversion settings from each GPIO.

    def getInversion(self):
        """ 
            Updates inversion_X variables with values from Qwiic GPIO

            :return: The value of the inversion register.
            :rtype: 8 bit unsigned integer

        """
        tempData = self._i2c.readByte(self.address, self.REG_INVERSION)
        self.inversion_0 = (tempData & (1 << 0)) >> 0
        self.inversion_1 = (tempData & (1 << 1)) >> 1
        self.inversion_2 = (tempData & (1 << 2)) >> 2
        self.inversion_3 = (tempData & (1 << 3)) >> 3
        self.inversion_4 = (tempData & (1 << 4)) >> 4
        self.inversion_5 = (tempData & (1 << 5)) >> 5
        self.inversion_6 = (tempData & (1 << 6)) >> 6
        self.inversion_7 = (tempData & (1 << 7)) >> 7
        return tempData

    #----------------------------------------------------------------
    # setGPIO()
    # 
    # Sends all GPIO outputs to the Qwiic GPIO 

    def setGPIO(self):
        """ 
            Send all current output settings to the GPIO. This should be called after calling myGPIO.out_status_0 = myGPIO.GPIO_HI to set the GPIO.

            :return: No return value

        """
        tempData = 0
        tempData |= self.out_status_0 << 0
        tempData |= self.out_status_1 << 1
        tempData |= self.out_status_2 << 2
        tempData |= self.out_status_3 << 3
        tempData |= self.out_status_4 << 4
        tempData |= self.out_status_5 << 5
        tempData |= self.out_status_6 << 6
        tempData |= self.out_status_7 << 7
        self._i2c.writeByte(self.address, self.REG_OUTPUT_PORT, tempData)


    def getGPIO(self):
        """ 
            Updates mode_X variables with values from Qwiic GPIO

            :return: The value of the mode register.
            :rtype: 8 bit unsigned integer

        """
        tempData = self._i2c.readByte(self.address, self.REG_INPUT_PORT)
        self.in_status_0 = (tempData & (1 << 0)) >> 0
        self.in_status_1 = (tempData & (1 << 1)) >> 1
        self.in_status_2 = (tempData & (1 << 2)) >> 2
        self.in_status_3 = (tempData & (1 << 3)) >> 3
        self.in_status_4 = (tempData & (1 << 4)) >> 4
        self.in_status_5 = (tempData & (1 << 5)) >> 5
        self.in_status_6 = (tempData & (1 << 6)) >> 6
        self.in_status_7 = (tempData & (1 << 7)) >> 7
        return tempData