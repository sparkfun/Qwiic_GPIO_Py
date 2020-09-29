#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qwiic_gpio_ex1.py
#
# Simple Example for the Qwiic GPIO Device, toggles GPIO 0 on and off.
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2019
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
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
# Example 1
#

from __future__ import print_function
import qwiic_gpio
import time
import sys

def runExample():

    print("\nSparkFun Qwiic GPIO Example 1\n")
    myGPIO = qwiic_gpio.QwiicGPIO()

    if myGPIO.isConnected() == False:
        print("The Qwiic GPIO isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return

    myGPIO.begin()
    myGPIO.mode_0 = myGPIO.GPIO_OUT
    myGPIO.mode_1 = myGPIO.GPIO_OUT
    myGPIO.mode_2 = myGPIO.GPIO_OUT
    myGPIO.mode_3 = myGPIO.GPIO_OUT
    myGPIO.mode_4 = myGPIO.GPIO_OUT
    myGPIO.mode_5 = myGPIO.GPIO_OUT
    myGPIO.mode_6 = myGPIO.GPIO_OUT
    myGPIO.mode_7 = myGPIO.GPIO_OUT
    myGPIO.setMode()

    while True:
        myGPIO.out_status_0 = myGPIO.GPIO_HI
        myGPIO.out_status_1 = myGPIO.GPIO_HI
        myGPIO.out_status_2 = myGPIO.GPIO_HI
        myGPIO.out_status_3 = myGPIO.GPIO_HI
        myGPIO.out_status_4 = myGPIO.GPIO_HI
        myGPIO.out_status_5 = myGPIO.GPIO_HI
        myGPIO.out_status_6 = myGPIO.GPIO_HI
        myGPIO.out_status_7 = myGPIO.GPIO_HI
        myGPIO.setGPIO()
        print("set hi")
        time.sleep(1)
        myGPIO.out_status_0 = myGPIO.GPIO_LO
        myGPIO.out_status_1 = myGPIO.GPIO_LO
        myGPIO.out_status_2 = myGPIO.GPIO_LO
        myGPIO.out_status_3 = myGPIO.GPIO_LO
        myGPIO.out_status_4 = myGPIO.GPIO_LO
        myGPIO.out_status_5 = myGPIO.GPIO_LO
        myGPIO.out_status_6 = myGPIO.GPIO_LO
        myGPIO.out_status_7 = myGPIO.GPIO_LO
        myGPIO.setGPIO()
        print("set lo")
        time.sleep(1)


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)