# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables that are constant:
const_ExperimentTime = 1800         # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)

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
        p_Rig.o_R_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Right Lever is Out')
        p_State.switch(Trial) # Switches to Trial class

# =================+++++++================= #

class Trial:      #StateID = ?
    def s_State_enter():
        print('Trial: Initiating Trial class')
    def s_i_L_Lever_Press_rise():
        print('Trial: Left Lever (active lever) was pressed, switching to Reward class')
        p_State.switch(Reward)
    def s_i_R_Lever_Press_rise():
        print('Trial: Right Lever (inactive lever) was pressed, switching back to Trial class')
        p_State.switch(Trial)

class Reward:      #StateID = ?
    def s_State_enter():
        print('Reward: Initiating Dispense')
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Reward: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
        p_State.switch(Trial)

# = #