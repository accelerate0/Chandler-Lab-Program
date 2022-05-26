# Pynapse Source #
# V 3

import numpy as np
import sys
import random
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Naming matters as well as presetting certain things in Pynapse+Synapse.
# Therefore the following attributes needs to be declared in the Synapse program:

#  Regarding Timers: (8 Characters max)
#    Global Timer = Global_T
#    VI Timer = VI_T
#    ITI Timer = ITI_T

#  Regarding inputs and outputs: (Variable names must be exact and case sensitive) (3-20 Characters):
#
#      For iH10_1 Controller:
#          Channel 1 = o_L_Lever_Extension
#          Channel 2 = i_L_Lever_Press
#          Channel 3 = o_L_Lever_Light
#          Channel 4 = o_Rew_Recep_Light
#          Channel 5 = o_House_Light
#          Channel 6 = o_Tone
#          Channel 7 = i_Rew_Recep_Beam_Brk
#          Channel 9 = o_Pellet_Dispenser
#          Channel 10 = o_Shock
#      For iH10_2 Controller:
#          Channel 1 = o_R_Lever_Extension
#          Channel 2 = i_R_Lever_Press
#          Channel 3 = o_R_Lever_Light


# Global Variables:
const_SessionLength = 3600      # Length of the entire experiment (in sec)
const_VISchedule = 30           # Variable interval schedule with mean interval (in sec)
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)

# Creating VI Scheduling
float_1 = np.random.normal(const_VISchedule,3,1) # Random number generator via floating point of Gaussian function
float_2 = np.random.normal(const_VISchedule,3,1) # (mean average, standard deviation, amount of numbers)
float_3 = np.random.normal(const_VISchedule,3,1) # 3 for 3 VI intervals
print("The numbers generated for VI are ", float_1, " ", float_2, " ", float_3, " seconds")

# Creating ITI Scheduling
ITI_T_Array = [np.random.normal(const_ITI,3,100)] # (average, standard deviation, amount of numbers)
print("The numbers generated are ", ITI_T_Array, "seconds")
ITI_T1 = np.random.choice(ITI_T_Array, size=1)
ITI_T2 = np.random.choice(ITI_T_Array, size=1)
ITI_T3 = np.random.choice(ITI_T_Array, size=1)
ITI_T4 = np.random.choice(ITI_T_Array, size=1)
ITI_T5 = np.random.choice(ITI_T_Array, size=1)
ITI_T6 = np.random.choice(ITI_T_Array, size=1)
ITI_T7 = np.random.choice(ITI_T_Array, size=1)
ITI_T8 = np.random.choice(ITI_T_Array, size=1)
ITI_T9 = np.random.choice(ITI_T_Array, size=1)

# Displays Set Variables and Presets
print( "EXPERIMENTAL PRESETS:", '\n', '\n',
"const_SessionLength =", const_SessionLength, '\n',
"const_VISchedule =", const_VISchedule, '\n',
"const_CorrectResponse =", const_CorrectResponse, '\n',
"const_ITI =", const_ITI, '\n', '\n', '\n'
)

# Please Read The readme.txt
print( "PLEASE READ THE README.TXT BEFORE CONTINUING", '\n', '\n')

#==========================================================#
#                   Actual Program                         #
#==========================================================#

# Always class is special for Pynapse, everything here is always on(?)
# Set Global 60 minute Timer For Entire Experiment:
class Always:   #StateID = 0
    def s_Mode_recprev():
        p_Timer.Global_T.setPeriod(const_SessionLength) # Length (sec)
        p_Timer.Global_T.setRepeats(1) # Frequency
        p_Timer.Global_T.turnOn() # Turn on timer
    def s_Global_T_tick(count):
        if s_Global_T_tick(count) == const_SessionLength:
            print('60 minute timer finished')
            print('The Experiment is Complete')
            syn.setModeStr('Idle') # Shuts down synapse
        elif s_Global_T_tick(count) == ITI_T1:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4 + ITI_T5:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4 + ITI_T5 + ITI_T6:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4 + ITI_T5 + ITI_T6 + ITI_T7:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4 + ITI_T5 + ITI_T6 + ITI_T7 + ITI_T8:
            p_Rig.o_Tone.turnOn()
        elif s_Global_T_tick(count) == ITI_T1 + ITI_T2 + ITI_T3 + ITI_T4 + ITI_T5 + ITI_T6 + ITI_T7 + ITI_T8 + ITI_T9:
            print ("ITI Intervaling is done")
# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Lever is Out')
        p_State.switch(VI1_Timer) # Switches to Trial class

# =================+++++++================= #

class VI1_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(float_1) # First random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_T.turnOn()
    def s_VI_T_tick(count):
        if def s_VI_T_tick(count) == float_1:
            p_State_switch(VI1_Event)
class VI1_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(const_CorrectResponse, VI2_Timer) # Window Time aka Threshold, Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI1_Reward)
class VI1_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.fire() # Gives sucrose as reward
        print('Lever Was Pressed')
        p_State.switch(VI2_Timer)

class VI2_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(float_2) # Second random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_T.turnOn()
    def s_VI_T_tick(count):
        if def s_VI_T_tick(count) == float_2:
            p_State_switch(VI2_Event)
class VI2_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(const_CorrectResponse, VI3_Timer) # Window Time aka Threshold, Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI2_Reward)
class VI2_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.fire() # Gives sucrose as reward
        print('Lever Was Pressed')
        p_State.switch(VI3_Timer)

class VI3_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(float_3) # Third random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_T.turnOn()
    def s_VI_T_tick(count):
        if def s_VI_T_tick(count) == float_3:
            p_State_switch(VI3_Event)
class VI3_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(const_CorrectResponse, VI1_Timer) # Window Time aka Threshold, Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI3_Reward)
class VI3_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.fire() # Gives sucrose as reward
        print('Lever Was Pressed')
        p_State.switch(VI1_Timer)

# _________________________________________ #

class ITI_Initial:   #StateID = ?
    def s_State_enter():
        ITI_T = np.random.choice(ITI_T_Array, size=1)
        ITI_Ticker = ITI_Ticker + 1
    def s_Mode_standby():
        p_Timer.ITI_T.setPeriod(ITI_T)
        p_Timer.ITI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_T.turnOn()
    def s_ITI_T_tick(count):
        p_State_switch(ITI_Tone)
class ITI_Tone:     #StateID = ?
    def s_State_enter():
        p_Rig.o_Tone.turnOn()
    def s_Mode_standby():
        p_Timer.ITI_T.setPeriod(28)
        p_Timer.ITI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_T.turnOn()
    def s_ITI_T_tick(count):
        p_State_switch(ITI_Shock)
class ITI_Shock:     #StateID = ?
    def s_Mode_standby():
        p_Timer.ITI_T.setPeriod(2)
        p_Timer.ITI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_T.turnOn()
    def s_ITI_T_tick(count):
        p_State_switch(ITI_Off)

class ITI_Off:      #StateID = ?
    def s_State_enter():
        p_Rig.o_Shock.turnOff()
        p_Rig.o_Tone.turnOff()



class ITI_3_Interval:      #StateID = ?
    def s_Mode_standby():
        p_Timer.ITI_T.setPeriod(300)
        p_Timer.ITI_T.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_T.turnOn()
    def s_ITI_T_tick(count):
        p_State_switch(ITI_Initial)

class ITI_9_Interval:      #StateID = ?
    def s_Mode_standby():
        print('ITI operation done')
