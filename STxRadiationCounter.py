"""
STxRadiationCounter version 1.0
The purpose of this script:
    Provide interfase functionality as a class with functions to communicate with a:
    Spectrum Techniques radiation counter (STx) over a USB com port.
    As described by 'STX_Programming_Guide.pdf' the 'STX Design and Programming Manual'
    

This script was, created for, and tested on:
    Devise:         ST365 radiation counter
    Manufacturer:   Spectrum techniques

This script was created by:
    Jos Luijten (j.luijten87@gmail.com)
    A version of this script was written in C# and in Python
    C# in Git-repository:       https://github.com/Jos-Luijten/STxUSB-Csharp
    Python in Git-repository:   https://github.com/Jos-Luijten/STxUSB-Python

This scripts goals to achieve:
    - autodetection and confirmation of device on port, on Windows and Linux Debian
    - enforce thread serialization to prevent communication collisions, (The com port wil be used as a non-reentrant resource)
    - Able to send a command and wait for repley, wich needs to be returnd
    - enforce only known commands to be send

Noteworthy dependencies:
    - Pyserial (pip3 install pyserial)

"""


import serial
import serial.tools.list_ports

SerialPort : serial

def init(verbose = False):
    global SerialPort
    if verbose: 
        print("STxUSB started, searching port:")
    
    ports = serial.tools.list_ports.comports()                          #gets all ports
    for aPort in ports: 
        print("found: " + str(aPort.device) + " " + str(aPort.hwid))    #show found portnames and device information

    ports = serial.tools.list_ports.grep("0403:6001")                       #searches for a devise with name, vid,pid containing the argument

    no_device_halt = True                                                   #if no port is found, then halt the program

    for aPort in ports:
        no_device_halt = False                                              #port is found, so don't halt
        if verbose: 
            print("found: " + str(aPort.device) + " " + str(aPort.hwid))    #show found portnames and device information

    if no_device_halt == False:
        print("Device not found, check connection, and try again.")         #show error message and halt
        exit()
                 
                                                                            #get serial object to start communicating with last aPort found
    SerialPort = serial(port = aPort.device, baudrate = 115200, bytesize = 8, parity = "N", stopbits = 1,timeout = None, xonxoff = False, rtscts = False, write_timeout = None, dsrdtr = False, inter_byte_timeout = None, exclusive = None)


def send_command(command :str) -> str:
    global SerialPort
    senddata = ">" + command + "\r"
    SerialPort.write(senddata.encode('ascii','ignore'))
    return SerialPort.readline() #.decode('Ascii')) # Print the contents of the serial data

def reset_device_00() -> str:
    return send_command("00")

def start_counter_01() -> str:
    return send_command("01")

def stop_counter_02() -> str:
    return send_command("02")

def request_status_03() -> str:
    return send_command("03")

def request_counts_04() -> str:
    return send_command("04")

def request_parameters_05() -> str:
    return send_command("05")

def request_system_parameters_06() -> str:
    return send_command("06")

def store_current_parameters_07() -> str:
    return send_command("07")

def start_demo_counter_08() -> str:
    return send_command("08")

def high_voltage_on_12() -> str:
    return send_command("12")

def high_voltage_off_13() -> str:
    return send_command("13")

def high_voltage_onewire_on_14() -> str:
    return send_command("14")

def high_voltage_onewire_off_15() -> str:
    return send_command("15")

def request_high_voltage_status_16() -> str:
    return send_command("16")

def read_high_voltage_data_17() -> str:
    return send_command("17")



