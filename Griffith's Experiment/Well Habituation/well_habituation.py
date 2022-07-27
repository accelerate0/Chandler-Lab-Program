# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables that are constant:
const_ExperimentTime = 1800         # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)
const_T = 15                        # Interval in between dispense (sec)

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        p_Timer.Global_T.setPeriod(1)
        p_Timer.Global_T.setRepeats(const_ExperimentTime)
        p_Timer.Global_T.start()
        print('Pretrial: Starting the Global Timer for', const_ExperimentTime,'sec')
        print("Pretrial: EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime (sec)=", const_ExperimentTime, '\n',
        "const_DispenseTime (sec)=", const_DispenseTime, '\n',
        "const_T (sec) =", const_T, '\n',
        '\n')
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
        p_State.switch(Trial) # Switches to Trial class

# =================+++++++================= #

class Trial:      #StateID = ?
    def s_State_enter():
        print('Trial: Initiating Trial class')
        p_Timer.Trial_T.setPeriod(1)
        p_Timer.Trial_T.setRepeats(const_T)
        p_Timer.Trial_T.start()
        print('Trial: Started the Trial Timer for ', const_T,'sec')
    def s_Trial_T_tick(count):
        if count == const_T:
            print('Trial: Trial Timer finished')
            p_State.switch(Reward)

class Reward:      #StateID = ?
    def s_State_enter():
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Reward: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
        p_State.switch(Trial)

# = #
