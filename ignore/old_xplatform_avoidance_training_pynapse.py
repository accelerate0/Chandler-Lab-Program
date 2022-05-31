# Pynapse Source #
# V 1.5
# WORKING ON STATE INTEGRATION

import numpy # For Zero Arrays, Mathematical Functions, Optimizations, etc
import time # For timer and time functions

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables
const_SessionLength = 3600 # Length of the entire experiment in sec
const_VISchedule = 30 # Variable interval schedule with mean interval of 30sec
const_ITI = 180 # Mean Intertrial Interval in seconds

# Creating VI Timer
import numpy as np
float_1 = np.random.normal(const_VISchedule,3,1) # Random number generator via floating point of Gaussian function
float_2 = np.random.normal(const_VISchedule,3,1) # (mean average, standard deviation, amount of numbers)
float_3 = np.random.normal(const_VISchedule,3,1) # 3 for 3 VI intervals
print("The numbers generated for VI are ", VI_Timer.float_1, " ", VI_Timer.float_2, " ", VI_Timer.float_3, " seconds")

# Creating ITI Timer
ITI_Timer_Array = [np.random.normal(const_ITI,3,100)] # average, standard deviation, amount of numbers
print("The numbers generated are ", ITI_Timer_Array, "seconds")
ITI_Ticker = 0

#==========================================================#
#                Program: Preliminary                      #
#==========================================================#

# Program Information
print("Platform Avoidance Test", '\n', "Version 1", '\n', "By Erick Won", '\n', "Dr L Chandler Lab 2022", '\n', '\n', '\n')

# Displays Set Variables and Presets
print( "EXPERIMENTAL PRESETS:", '\n', '\n',
"const_SessionLength =", const_SessionLength, '\n',
"const_VISchedule =", const_VISchedule, '\n',
"const_ITI =", const_ITI, '\n'
)


#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_standby():
        p_Timer.GlobalTimer.setPeriod(const_SessionLength)
        p_Timer.GlobalTimer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.GlobalTimer.turnOn()
    def s_GlobalTimer_tick(count):
        print('done')
        syn.setModeStr('Idle')

# =================+++++++================= #

class PreTrial:     #StateID = ?
    def s_State_enter():
        p_Rig.output_House_Light.turnOn()
        print('Light is On')
        p_Rig.output_Left_Lever_Extension.turnOn()
        print('Lever is Out')
        p_State.switch(VI1_Timer)

# =================+++++++================= #

class VI1_Timer:    #StateID = ?
    def s_Mode_standby():
        p_Timer.VI_Timer.setPeriod(float_1)
        p_Timer.VI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_Timer.turnOn()
    def s_VI_Timer_tick(count):
        p_State_switch(VI1_Event)
class VI1_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(3, VI2_Timer) # Delay Time , Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI1_Reward)
class VI1_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.output_Pellet_Dispenser.fire()
        print('Lever Was Pressed')
        p_State.switch(VI2_Timer)

class VI2_Timer:    #StateID = ?
    def s_Mode_standby():
        p_Timer.VI_Timer.setPeriod(float_2)
        p_Timer.VI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_Timer.turnOn()
    def s_VI_Timer_tick(count):
        p_State_switch(VI2_Event)
class VI2_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(3, VI3_Timer) # Delay Time , Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI2_Reward)
class VI2_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.output_Pellet_Dispenser.fire()
        print('Lever Was Pressed')
        p_State.switch(VI3_Timer)

class VI3_Timer:    #StateID = ?
    def s_Mode_standby():
        p_Timer.VI_Timer.setPeriod(float_3)
        p_Timer.VI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.VI_Timer.turnOn()
    def s_VI_Timer_tick(count):
        p_State_switch(VI3_Event)
class VI3_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimout(3, VI1_Timer) # Delay Time , Goto Class
    def s_LeverPress_rise():
        p_State_switch(VI3_Reward)
class VI3_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.output_Pellet_Dispenser.fire()
        print('Lever Was Pressed')
        p_State.switch(VI1_Timer)

# =================+++++++================= #


class ITI_Initial:
    def s_State_enter():
        ITI_Timer = np.random.choice(ITI_Timer_Array, size=1)
        ITI_Ticker = ITI_Ticker + 1
    def s_Mode_standby():
        p_Timer.ITI_Timer.setPeriod(ITI_Timer)
        p_Timer.ITI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_Timer.turnOn()
    def s_ITI_Timer_tick(count):
        p_State_switch(ITI_Tone)
class ITI_Tone:
    def s_State_enter():
        p_Rig.output_Tone.turnOn()
    def s_Mode_standby():
        p_Timer.ITI_Timer.setPeriod(28)
        p_Timer.ITI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_Timer.turnOn()
    def s_ITI_Timer_tick(count):
        p_State_switch(ITI_Shock)
class ITI_Shock:
    def s_Mode_standby():
        p_Timer.ITI_Timer.setPeriod(2)
        p_Timer.ITI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_Timer.turnOn()
    def s_ITI_Timer_tick(count):
        p_State_switch(ITI_Event)
class ITI_Off:      #StateID = ?
    def s_State_enter():
        p_Rig.output_Shock.turnOff()
        p_Rig.output_Tone.turnOff()
        p_State_switch(ITI_Ticker_Check)

class ITI_Ticker_Check:
    def s_State_enter():
        if ITI_Ticker = 3 or 6:
            p_State_switch(ITI_3_Interval)
        elif ITI_Ticker = 9:
            p_State_switch(ITI_9_Interval)
        else:
            p_State_switch(ITI_Initial)

class ITI_3_Interval:
    def s_Mode_standby():
        p_Timer.ITI_Timer.setPeriod(300)
        p_Timer.ITI_Timer.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.ITI_Timer.turnOn()
    def s_ITI_Timer_tick(count):
        p_State_switch(ITI_Initial)

class ITI_9_Interval:
    def s_Mode_standby():
        print('ITI operation done')








#
