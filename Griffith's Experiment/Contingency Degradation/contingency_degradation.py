# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables that are constant:
const_ExperimentTime = 900          # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)
const_Float = 30                    # Median of the floating point number randomly generated (sec), PyOp Related
const_Reinforcers = 90              # Involved in calculating the "J Factor" which is done automatically


# Global Variables that are dyanmic (!Do Not Change!):
J = 0 # The "J Factor", or Variable for Interval

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        p_Timer.Global_T.start() # Turn on timer
        print('Pretrial: Started the Global Timer at', const_ExperimentTime,'sec')
        print("Pretrial: EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime (sec) =", const_ExperimentTime, '\n',
        "const_DispenseTime (sec) =", const_DispenseTime, '\n',
        "const_Float (sec) =", const_Float, '\n',
        "const_Reinforcers =", const_Reinforcers, '\n',
        '\n')
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
        # Calculating J Factor
        J = (30/const_Reinforcers)*60
        print('Pretrial: J Factor (Variable for Interval) calculated to be', J)
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
            print('Timer: Trial Timer finished')
            p_Rig.o_Liq_Dispenser.turnOn()
            time.sleep(const_DispenseTime)
            p_Rig.o_Liq_Dispenser.turnOff()
            print('Event: Dispended at', const_DispenseTime, 'sec, reinitializing Trial Timer')
            p_State.switch(Loop)

class Loop:      #StateID = ?
    def s_State_enter():
        p_State.switch(Timer)


# = #
