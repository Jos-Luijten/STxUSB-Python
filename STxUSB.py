"""
STxUSB version 1.0
The purpose of this script:
    A console application to communicate and operate a:
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
    - application works from command line, so that it can be called and used by other programs and users
    - application contains "STxRadiationCounter" class with public functions so that the code can implemented in other projects

Noteworthy dependencies:
    - Pyserial (pip3 install pyserial)

"""


import serial.tools.list_ports
import sys
import STxRadiationCounter




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Step 0 :




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Step 1 : Define used functions

def ShowHelp():                                                             #Print out help info in console envirnoment
    print("")
    print("STx USB console aplication")
    print("==============================================================")
    print("")
    print("USAGE:>Python STxUSB.py -option1 -option2 -option3 .....")
    print("")
    print("Where options are:")
    print("     -? or -h or -help       Display this help message")
    print("     -00 or -reset           Reset device")
    print("     -01 or -start           Start counter")
    print("     -02 or -stop            Stop counter")
    print("     -03 or -status          Request Status")
    print("     -04 or -counts          Request Counts")
    print("     -05 or -param           Request parameters")
    print("     -06 or -system          Request system parameters")
    print("     -07 or -store           Store current parameters to eeprom")
    print("     -08 or -demo            Start demo counter")     
    print("     -12 or -hvon            High voltage on command")   
    print("     -13 or -hvoff           High voltage off command")   
    print("     -14                     High voltage one-wire on command")   
    print("     -15                     High voltage one-wire off command")   
    print("     -16 or -hvstatus        High voltage status request")   
    print("     -17 or -hvdata          Read high voltage data")   
    print("     -e or -exit             exit / terminate this program")
    print("     -v or -verbose          turn on verbose, show more output,")
    print("")
    print("If options are given, the program will execute those and terminate / exit")
    print("The default behaviour (without options) is:")
    print("     the program will ask and wait for an command (input by user)")
    print("     after a response, the program will ask for the next command ")
    print("")
    print("Returns:")
    print("     On possible return values and interpretation read:")
    print("     'STX_Programming_Guid.pdf'")
    print("")
    print("Examples:")
    print("     -01                   start counter")
    print("     -04 -v                Show detailed information and ask for status")




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Step 2 : Prepare program assignment, by pre-prosessing command-line arguments.

verbose = False                                                         #used to deside wich information is printed out into the console
commands = []                                                           #List of known commands to execute in given order
unknown_arguments = []                                                  #List of not recognised arguments that ware given in order to give feedback when verbose is set to true

for argument in sys.argv[1:]:                                           #Skip first argument, and check others to recognize, or store given commands / arguments
    argument = argument.lower()
    if argument == "-v" or "-verbose":
        verbose = True
    elif argument == "-?" or argument == "-h" or argument == "-help" or argument == "-info" or argument == "/help" or argument == "/?" or argument == "/h" or argument == "?" or argument == "help":
        ShowHelp()
    elif argument == "-00" or argument == "-reset":
        commands.append("-00")
    elif argument == "-01" or argument == "-start":
        commands.append("-01")
    elif argument == "-02" or argument == "-stop":
        commands.append("-02")
    elif argument == "-03" or argument == "-status":
        commands.append("-03")
    elif argument == "-04" or argument == "-counts":
        commands.append("-04")
    elif argument == "-05" or argument == "-param":
        commands.append("-05")
    elif argument == "-06" or argument == "-system":
        commands.append("-06")
    elif argument == "-07" or argument == "-store":
        commands.append("-07")
    elif argument == "-08" or argument == "-demo":
        commands.append("-08")

    elif argument == "-12" or argument == "-hvon":
        commands.append("-12")
    elif argument == "-13" or argument == "-hvoff":
        commands.append("-13")
    elif argument == "-14":
        commands.append("-14")
    elif argument == "-15":
        commands.append("-15")
    elif argument == "-16" or argument == "-hvstatus":
        commands.append("-16")
    elif argument == "-17" or argument == "-hvdata":
        commands.append("-17")
    elif argument == "-e" or argument == "-exit":
        commands.append("exit")
    else:
        unknown_arguments.append(argument)
    

if verbose and len(unknown_arguments) > 0:                              #show all unknow command line arguments that where given if verbose is regognised 
    print("")
    print("Unknown commands given: ")
    for x in unknown_arguments: print("  " + x)
    

if len(sys.argv) > 1:
    commands.append("exit") 	                                        #the last command should be exit, to exit end the program automaticly
   



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Step 3: prepere serial port connection by searching for connected USB devise wid PID and VID equal to the ST365 radiation counter

STxRadiationCounter.init(verbose)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Step 4: execute commands

for command in commands:
    if command == "exit": exit()
    if command == "-00": print(STxRadiationCounter.reset_device_00())
    if command == "-01": print(STxRadiationCounter.start_counter_01())
    if command == "-02": print(STxRadiationCounter.stop_counter_02())
    if command == "-03": print(STxRadiationCounter.request_status_03())
    if command == "-04": print(STxRadiationCounter.request_counts_04())
    if command == "-05": print(STxRadiationCounter.request_parameters_05())
    if command == "-06": print(STxRadiationCounter.request_system_parameters_06())
    if command == "-07": print(STxRadiationCounter.store_current_parameters_07())
    if command == "-08": print(STxRadiationCounter.start_demo_counter_08())
    if command == "-12": print(STxRadiationCounter.high_voltage_on_12())
    if command == "-13": print(STxRadiationCounter.high_voltage_off_13())
    if command == "-14": print(STxRadiationCounter.high_voltage_onewire_on_14())
    if command == "-15": print(STxRadiationCounter.high_voltage_onewire_off_15())
    if command == "-16": print(STxRadiationCounter.request_high_voltage_status_16())
    if command == "-17": print(STxRadiationCounter.read_high_voltage_data_17())
    



