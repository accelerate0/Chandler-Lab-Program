# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables that are constant:
const_ExperimentTime = 900          # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)
const_Float = 30                    # Median of the floating point number randomly generated (sec)
const_CorrectResponse = 3           # Threshold window of opportunity that allows dispensing (sec)
const_Reinforcers = 0               # Involved in calculating the "J Factor" which is done automatically

# Global Variables that are dyanmic (Do Not Change):
J = 0 # The "J Factor", or Variable for Interval

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        print('Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Starting the global experimental', const_ExperimentTime,'sec timer')
        p_Timer.Global_T.start() # Turn on timer
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n')
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        if count == const_ExperimentTime:
            print(const_ExperimentTime, 'sec has passed and experiment is completed, shutting down')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        global J
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Left Lever is Out')
        p_Rig.o_R_Lever_Extension.turnOn() # Turns on right lever
        print('Pretrial: Right Lever is Out')
        # Calculating J Factor
        J = (30/const_Reinforcers)*60
        print('J Factor (Variable for Interval) calculated to be', J)
        # Switches to Timer class
        p_State.switch(Timer)

# =================+++++++================= #

class Timer:      #StateID = ?
    def s_State_enter():
        p_Timer.Trial_T.setPeriod(1)
        p_Timer.Trial_T.setRepeats(J)
        p_Timer.Trial_T.start() # Turn on timer
    def s_Trial_T_tick(count):
        if count == J:
            print('Timer: Trial Timer finished, switching to Event class')
            print('Event: Left Lever (active lever) was pressed, Initiating Dispense')
            p_Rig.o_Liq_Dispenser.turnOn()
            time.sleep(const_DispenseTime)
            p_Rig.o_Liq_Dispenser.turnOff()
            print('Event: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
            p_State.switch(Event)


# = #
