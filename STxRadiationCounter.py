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






def init(verbose = False):
    
def reset_device_00():

def start_counter_01():

def stop_counter_02():

def request_status_03():

def request_counts_04():

def request_parameters_05():

def request_system_parameters_06():

def store_current_parameters_07():

def start_demo_counter_08():

def high_voltage_on_12():

def high_voltage_off_13():

def high_voltage_onewire_on_14():

def high_voltage_onewire_off_15():

def request_high_voltage_status_16():

def read_high_voltage_data_17():



