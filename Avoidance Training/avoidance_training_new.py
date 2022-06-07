# Pynapse Source #
# V 6

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables:
const_VISchedule = 30           # Variable interval schedule with mean interval (in sec)
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)
const_ExperimentTime = 3600     # Time of Entire Experiment

ITI_Ticker = 0
ITI_Float = 0
ITI_T_1 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_T = 0
ITI_T_28 = 0
ITI_T_30 = 0

# Creating VI Scheduling
VI1_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # Random number generator via floating point of Gaussian function
VI2_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # (mean average, standard deviation, amount of numbers)
VI3_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # 3 for 3 VI intervals

# Creating ITI Scheduling
ITI_VI1_Float = int(np.round(np.random.normal(const_ITI,5,1)))

#==========================================================#
#                   Actual Program                         #
#==========================================================#
# Always class: Special class for Pynapse where conditionals here is always being checked


class Always:   #StateID = 0
    def s_Mode_recprev():
        print('Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Starting the global experimental 3600 sec timer')
        p_Timer.Global_T.start() # Turn on timer
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_VISchedule =", const_VISchedule, '\n',
        "const_CorrectResponse =", const_CorrectResponse, '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_ITI =", const_ITI, '\n', '\n', '\n',
        "The VI numbers generated are ", VI1_Float, " ", VI2_Float, " ", VI3_Float, " seconds", '\n', '\n'
        )
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        global ITI_Ticker, ITI_Float, ITI_T, ITI_T_28, ITI_T_30
        if count == 900:
            print('15 minutes have passed')
        elif count == 1800:
            print('30 minutes have passed')
        elif count == 2700:
            print('45 minutes have passed')
        elif count == const_ExperimentTime:
            print('60 min has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)
        # ===== Conditional Based ITI Scheduling: 1 Time ===== #
        elif count == ITI_T_1:
            print('ITI 1')
            ITI_T_28 = ITI_T_1 + 28
            ITI_T_30 = ITI_T_1 + 30
            ITI_Ticker = ITI_Ticker + 1
            p_Rig.o_Tone.turnOn()
            print('ITI: Tone On')
        elif count == ITI_T_28:
            p_Rig.o_Shock.turnOn()
            print('ITI: Shock On')
        elif count == ITI_T_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI: Tone & Shock Off')
            ITI_T = ITI_T_30
        # ===== Conditional Based ITI Scheduling: Looping 2-9 ===== #
        elif count == ITI_T:
            ITI_Float = int(np.round(np.random.normal(const_ITI,5,1)))
            ITI_T = ITI_T_30 + ITI_Float
            ITI_T_28 = ITI_T + 28
            ITI_T_30 = ITI_T + 30
            ITI_Ticker = ITI_Ticker + 1
            p_Rig.o_Tone.turnOn()
            print('ITI: Tone On')
        elif count == ITI_T_28:
            p_Rig.o_Shock.turnOn()
            print('ITI: Shock On')
        elif count == ITI_T_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI: Tone & Shock Off')
            ITI_T = ITI_T_30 + ITI_T
        elif ITI_Ticker == 4:
            ITI_T = ITI_T + 300
        elif ITI_Ticker == 7:
            ITI_T = ITI_T + 300
        elif ITI_Ticker == 9:
            print('ITI Finished')

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Lever is Out')
        p_State.switch(VI1_Timer) # Switches to Trial class

# =================+++++++================= #

class VI1_Timer:    #StateID = ?
    def s_State_enter():
        p_Rig.o_L_Lever_Light.turnOff()
        p_Timer.VI_T.setPeriod(1) # First random ~30 sec timer
        p_Timer.VI_T.setRepeats(VI1_Float)
        p_Timer.VI_T.start()
        print('VI 1: Timer Started')
    def s_VI_T_tick(count):
        if count == VI1_Float:
            p_State.switch(VI1_Event)
class VI1_Event:    #StateID = ?
    def s_State_enter():
        print('VI 1: Entering Event')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI 1: Left Lever Light On')
        p_State.setTimeout(const_CorrectResponse, VI2_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        print('VI 1: Lever was pressed')
        p_State.switch(VI1_Reward)
class VI1_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 1: Sucrose dispensed')
        p_State.switch(VI2_Timer)

class VI2_Timer:    #StateID = ?
    def s_State_enter():
        p_Rig.o_L_Lever_Light.turnOff()
        p_Timer.VI_T.setPeriod(1) # Second random ~30 sec timer
        p_Timer.VI_T.setRepeats(VI2_Float)
        p_Timer.VI_T.start()
        print('VI 2: Timer Started')
    def s_VI_T_tick(count):
        if count == VI2_Float:
            p_State.switch(VI2_Event)
class VI2_Event:    #StateID = ?
    def s_State_enter():
        print('VI 2: Entering Event')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI 1: Left Lever Light On')
        p_State.setTimeout(const_CorrectResponse, VI3_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI2_Reward)
        print('VI 2: Lever was pressed')
class VI2_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 2: Sucrose dispensed')
        p_State.switch(VI3_Timer)

class VI3_Timer:    #StateID = ?
    def s_State_enter():
        p_Rig.o_L_Lever_Light.turnOff()
        p_Timer.VI_T.setPeriod(1) # Third random ~30 sec timer
        p_Timer.VI_T.setRepeats(VI3_Float)
        p_Timer.VI_T.start()
        print('VI 3: Timer Started')
    def s_VI_T_tick(count):
        if count == VI3_Float:
            p_State.switch(VI3_Event)
class VI3_Event:    #StateID = ?
    def s_State_enter():
        print('VI 3: Entering Event')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI 1: Left Lever Light On')
        p_State.setTimeout(const_CorrectResponse, VI1_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI3_Reward)
        print('VI 3: Lever was pressed')
class VI3_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 3: Sucrose dispensed')
        p_State.switch(VI1_Timer)







# = #
