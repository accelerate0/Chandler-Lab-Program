import numpy # For Zero Arrays, Mathematical Functions, Optimizations, etc
import sys # For Program Exiting
import random # For random number generator and random choices
import time # For timer and time functions
import multiprocessing # For parallel running VI and ITI

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

class Presets:
    const_SessionLength = 3600 # Length of the entire experiment in sec
    const_VISchedule = 30 # Variable interval schedule with mean interval of 30sec
    const_CorrectResponse = 3 # Right lever press following the end of the VI timer
    const_ITI = 180 # Mean Intertrial Interval in seconds

# Reference Table at the moment, Will Either Delete Soon or Use to Robustly Integrate Pynapse Settings
def Channel()
    class iH10_1:
        output_Left_Lever_Extension = Channel.1a
        input_Left_Lever_Press = Channel.2a
        output_Left_Lever_Light	= Channel.3a
        output_Reward_Receptacle_Light = Channel.4a
        output_House_Light = Channel.5a
        output_Tone = Channel.6a
        input_Reward_Receptacle_Beam_Break = Channel.7a
        output_Pellet_Dispenser = Channel.9a
        output_Shock = Channel.10a
    class iH10_2:
        output_Right_Lever_Extension = Channel.1b
        input_Right_Lever_Press = Channel.2b
        output_Right_Lever_Light = Channel.3b

#==========================================================#
#                Program: Preliminary                      #
#==========================================================#

# Program Information
print("Platform Avoidance Test", '\n', "Version 1.0", '\n', "By Erick Won", '\n', "Dr L Chandler Lab 2022", '\n', '\n', '\n')

# Displays Set Variables and Presets
print( "KEY VARIABLES:", '\n', '\n',
"EXPERIMENTAL PRESETS:", '\n',
"const_SessionLength =", Presets.const_SessionLength, '\n',
"const_VISchedule =", Presets.const_VISchedule, '\n',
"const_CorrectResponse =", Presets.const_CorrectResponse, '\n',
"const_ITI =", Presets.const_ITI, '\n',
"const_Shutdown =", Presets.const_Shutdown, '\n'
)

# User Double Check Measure via yes/no
y_n_1_answer = input("Would you like to continue [y/n]?" + '\n')
if y_n_1_answer == "y":
    print('Proceeding on', '\n')
elif y_n_1_answer == "n":
    sys.exit()
else:
    print("Please enter y or n")

#==========================================================#
#      Program Execution of VI Schedule & ITI Timer        #
#==========================================================#

# Turning On Light and Lever
class Always: # Special Pynapse Function 'Always'
    p_Rig.output_House_Light.turnOn()
    print('Light is On')
    p_Rig.output_Left_Lever_Extension.turnOn()
    print('Lever is Out')

# Setting Up Parallel Execution of VI_Schedule and ITI_Timer
from multiprocessing import Process

# =================+++++++================= #

# Defining VI Scheduling Sub-Program
def Process_VI_Schedule():
    print ("Execute VI Schedule")
    class VI_Timer:
        import numpy as np
        float_1 = np.random.normal(Presets.const_VISchedule,3,1) # Random number generator via floating point of Gaussian function
        float_2 = np.random.normal(Presets.const_VISchedule,3,1) # (mean average, standard deviation, amount of numbers)
        float_3 = np.random.normal(Presets.const_VISchedule,3,1) # 3 for 3 VI intervals
        print("The numbers generated are ", VI_Timer.float_1, " ", VI_Timer.float_2, " ", VI_Timer.float_3, " seconds")
        # VI Schedule Interval 1
        time.sleep(VI_Timer.float_1) # Delay
        def s_1_input_Left_Lever_Press():
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 1')
        # VI Schedule Interval 2
        time.sleep(VI_Timer.float_2) # Delay
        def s_2_input_Left_Lever_Press():
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 2')
        # VI Schedule Interval 3
        time.sleep(VI_Timer.float_3) # Delay
        def s_3_input_Left_Lever_Press():
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 3')
    # Creating Loop For VI Schedule Interval 1,2,3 inside 60 minute timer
    VI_start_time = time.time() # Starting 60 minute timer of the entire VI_Schedule
    VI_seconds = Presets.const_SessionLength
    while True: # Loops Until 60 minute runs out
        VI_current_time = time.time()
        VI_elapsed_time = VI_current_time - VI_start_time
        time.sleep(0.01) # Optimization of CPU Usage because "while" sucks
        s_1_input_Left_Lever_Press()
        ### INSERT TTL PULSE EVENT ###
        s_2_input_Left_Lever_Press()
        ### INSERT TTL PULSE EVENT ###
        s_3_input_Left_Lever_Press()
        ### INSERT TTL PULSE EVENT ###
        if VI_elapsed_time > VI_seconds:
            print("Finished iterating in: " + str(int(VI_elapsed_time))  + " seconds")
            break
# End of VI_Schedule Portion

# =================+++++++================= #

# Defining ITI Timer Sub-Program
def Process_ITI_Timer():
    print ("Execute ITI Timer")
    # Generate Random Number For Timer
    class ITI_Timer:
        import numpy as np
        ITI_Timer_Array = [np.random.normal(Presets.const_ITI,3,100)] # average, standard deviation, amount of numbers
        print("The numbers generated are ", ITI_Timer_Array, "seconds")
    # Declaring ITI Experimental Set Up
    def ITI_Timer_Event_Reg(): # Regular ITI Event
        ITI_Timer = np.random.choice(VI_Timer_Array, size=1)
        time.sleep(ITI_Timer)
        p_Rig.output_Tone.turnOn() # Starting Tone
        time.sleep(28)
        p_Rig.output_Shock.turnOn() # Starting Shock
        time.sleep(2)
        p_Rig.output_Shock.turnOff() # Stopping Shock
        p_Rig.output_Tone.turnOff() # Stopping Tone
    # Declaring Special Case of ITI Experiment on Third Interval
    def ITI_Timer_Event_Third():
        Interblock_Interval = 300 # 5 minutes
        time.sleep(Interblock_Interval)
        ITI_Timer = np.random.choice(VI_Timer_Array, size=1) # Redeclare Variable
    # Wrapping Into 9 Intervals With A Special Instance After Every 3rd ITI Execution
    def ITI_Intervaling_SetUp():
        for _ in range(3): # Executing ITI 3 Times
            ITI_Timer_Event_Reg()
        ITI_Timer_Event_Third() # Execute Special Case Right After
    def ITI_Intervaling_Exec(): # Executing ITI_Intervaling_SetUp 3 Times, So ITI is Executed 9 Times
        for _ in range(3):
            ITI_Intervaling_SetUp()
    # Actual Code Execution of ITI
    ITI_Intervaling_Exec()

# End of ITI Section

# =================+++++++================= #

# Parallel Execution of Both Programs
Exec_Process_VI_Schedule = Process(target=Process_VI_Schedule)
Exec_Process_VI_Schedule.start()
Exec_Process_ITI_Timer = Process(target=Process_ITI_Timer)
Exec_Process_ITI_Timer.start()
