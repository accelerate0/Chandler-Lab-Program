# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_ExperimentTime = 1800         # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)
const_RIFloat = 30
const_RIAmount = 8
const_CorrectResponse = 3           # Threshold window of opportunity that allows dispensing (sec)
# Global Dynamic Variables:
RI_Float = 0
RI_Pool = 0

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
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Left Lever is Out')
        p_Rig.o_R_Lever_Extension.turnOn() # Turns on right lever
        print('Pretrial: Right Lever is Out')
        p_State.switch(Timer) # Switches to Trial class

# =================+++++++================= #

class Timer:      #StateID = ?
    def s_State_enter():
        global RI_Float, RI_Pool
        print('Trial: Initiating Trial class')
        pyop.rand_int(const_RIFloat, const_RIAmount)
        RI_Pool = pyop.rand_int.output
        RI_Float = int(random.choice(RI_Pool))
        print('Setting up Trial Timer', '\n',
        'Chose', RI_Float, 'sec for the RI30 Timer', '\n',
        'Generated', RI_Pool, 'sec as the pool', '\n',
        'Used mean of', RI_Float, 'sec', '\n')
        p_Timer.Trial_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Trial_T.setRepeats(RI_Float) # Amount of ticks
        p_Timer.Trial_T.start() # Turn on timer
        print('Timer: Trial Timer initiated')
    def s_Trial_T_tick(count):
        if count == RI_Float:
            print('Timer: Trial Timer finished, switching to Event class')
            p_State.switch(Event)

class Event:      #StateID = ?
    def s_State_enter():
        print('Event: Threshold window set to', const_CorrectResponse, 'sec, waiting on left lever press')
    def s_i_L_Lever_Press_rise():
        print('Event: Left Lever (active lever) was pressed, Initiating Dispense')
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Event: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
        p_State.switch(Timer)
    def s_i_R_Lever_Press_rise():
        print('Event: Right Lever (inactive lever) was pressed, nothing happens')

# = #
