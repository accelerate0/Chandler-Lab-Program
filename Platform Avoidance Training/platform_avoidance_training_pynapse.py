# Pynapse Source #
# V 1.5
# WORKING ON STATE INTEGRATION

import numpy # For Zero Arrays, Mathematical Functions, Optimizations, etc
import sys # For Program Exiting
import random # For random number generator and random choices
import time # For timer and time functions
import multiprocessing # For parallel running VI and ITI

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables
const_SessionLength = 3600 # Length of the entire experiment in sec
const_VISchedule = 30 # Variable interval schedule with mean interval of 30sec
const_CorrectResponse = 3 # Right lever press following the end of the VI timer
const_ITI = 180 # Mean Intertrial Interval in seconds

#==========================================================#
#                Program: Preliminary                      #
#==========================================================#

# Program Information
print("Platform Avoidance Test", '\n', "Version 1", '\n', "By Erick Won", '\n', "Dr L Chandler Lab 2022", '\n', '\n', '\n')

# Displays Set Variables and Presets
print( "EXPERIMENTAL PRESETS:", '\n', '\n',
"const_SessionLength =", const_SessionLength, '\n',
"const_VISchedule =", const_VISchedule, '\n',
"const_CorrectResponse =", const_CorrectResponse, '\n',
"const_ITI =", const_ITI, '\n'
)

#==========================================================#
#                   Actual Program                          #
#==========================================================#

# Turning On Light and Lever
class Always:   #StateID = 0
    # Special Pynapse Function 'Always'
    p_Rig.output_House_Light.turnOn()
    print('Light is On')
    p_Rig.output_Left_Lever_Extension.turnOn()
    print('Lever is Out')

# =================+++++++================= #


class PreTrial:   #StateID = ?
    # Defining VI Scheduling Sub-Program
    def Process_VI_Schedule_SetUp():
        print ("Execute VI Schedule")
        class VI_Timer:
            import numpy as np
            float_1 = np.random.normal(const_VISchedule,3,1) # Random number generator via floating point of Gaussian function
            float_2 = np.random.normal(const_VISchedule,3,1) # (mean average, standard deviation, amount of numbers)
            float_3 = np.random.normal(const_VISchedule,3,1) # 3 for 3 VI intervals
            print("The numbers generated are ", VI_Timer.float_1, " ", VI_Timer.float_2, " ", VI_Timer.float_3, " seconds")
        # VI Schedule Interval 1
        def First_input_Left_Lever_Press():
            time.sleep(VI_Timer.float_1) # Delay
            s_
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 1')
        # VI Schedule Interval 2
        def Second_input_Left_Lever_Press():
            time.sleep(VI_Timer.float_2) # Delay
            s_
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 2')
        # VI Schedule Interval 3
        def Third_input_Left_Lever_Press():
            time.sleep(VI_Timer.float_3) # Delay
            s_
            p_Rig.output_Pellet_Dispenser.turnOn()
            p_Rig.output_Pellet_Dispenser.turnOff()
            print('Lever Was Pressed & Logged For Float 3')
        # Creating Loop For VI Schedule Interval 1,2,3 inside 60 minute timer
        VI_start_time = time.time() # Starting 60 minute timer of the entire VI_Schedule
        VI_seconds = const_SessionLength
    def Process_VI_Schedule_Exec():
        while True: # Loops Until 60 minute runs out
            VI_current_time = time.time()
            VI_elapsed_time = VI_current_time - VI_start_time
            time.sleep(0.01) # Optimization of CPU Usage because "while" sucks
            ### Replace With Pynapse Timer Function at some point ###
            First_input_Left_Lever_Press()
            ### INSERT TTL PULSE EVENT ###
            Second_input_Left_Lever_Press()
            ### INSERT TTL PULSE EVENT ###
            Third_input_Left_Lever_Press()
            ### INSERT TTL PULSE EVENT ###
            if VI_elapsed_time > VI_seconds:
                print("Finished iterating in: " + str(int(VI_elapsed_time))  + " seconds")
                break

    # Defining ITI Timer Sub-Program
    def Process_ITI_Timer_SetUp():
        print ("Execute ITI Timer")
        # Generate Random Number For Timer
        class ITI_Timer:
            import numpy as np
            ITI_Timer_Array = [np.random.normal(const_ITI,3,100)] # average, standard deviation, amount of numbers
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
    def Process_ITI_Timer_Exec(): # Executing ITI_Intervaling_SetUp 3 Times, So ITI is Executed 9 Times with Special Case every 3 ITI
        for _ in range(3):
            ITI_Intervaling_SetUp()

class Trial:   #StateID = ?
    Process_VI_Schedule_SetUp()
    Process_ITI_Timer_SetUp()

    # Parallel Execution of Both Programs

    Exec_Process_VI_Schedule = Process(target=Process_VI_Schedule_Exec)
    Exec_Process_VI_Schedule.start()

    Exec_Process_ITI_Timer = Process(target=Process_ITI_Timer_Exec)
    Exec_Process_ITI_Timer.start()




#
