# Pynapse Source #

import numpy as np
import time
import random
import pyopcond_dep as pyop

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_ITI = 180                     # Mean value of ITI (sec)
const_ExperimentTime = 9999         # Time of Entire Experiment (sec)
const_ITISchedule_Amt = 5           # How many ITI number candidates are generated from PyOp
const_ITI_Interval = 20             # Amount of ITI
const_ITI_Delay_Amount = 300        # Delay amount (sec)
const_ITI_Delay_Div = 3             # Divisibility of the ITI delay ("Example: After every 3rd ITI interval is (3)")

# =================+++++++================= #
# ! DO NOT CHANGE ANYTHING HERE !

# Global Dynamic Variables:
ITI_Ticker = 0                      # Tracks amount of time ITI has looped
ITI_T = 0                           # Summated ITI Timer (sec)
ITI_Float = 0                       # ITI Timer (sec)
ITI_Pool = 0                        # Array store of ITI numbers from PyOp
ITI_Ticker_Math = 0                 # Related to finding the divisibility of the ITI for ITI delays

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        global ITI_Pool
        # Setting up Global Timer
        print('Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Starting the global experimental 3600 sec timer')
        p_Timer.Global_T.start() # Turn on timer
        # Printing Experimental Constants on console
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_ITI =", const_ITI, '\n', '\n', '\n')
        # Generating ITI number pool from PyOp
        print('Generating ITI Timer Pools')
        pyop.var_int(const_ITISchedule_Amt, const_ITI)
        ITI_Pool = pyop.var_int.output_straight
        print("ITI: Generated:", ITI_Pool, "ITI Pool from PyOp")
        # Switching to PreTrial Class
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
        p_Rig.o_R_Lever_Extension.turnOn() # Turns on right lever
        print('Pretrial: Left Lever is Out')
        p_State.switch(ITI_Timer) # Switches to Trial class

# =================+++++++================= #

class ITI_Timer:      #StateID = ?
    def s_State_enter():
        global ITI_Float, ITI_Ticker, ITI_T, ITI_Ticker_Math
        # Resetting ITI Variables
        ITI_T = 0
        ITI_Float = 0
        ITI_Ticker = ITI_Ticker + 1
        # Keeping track of ITI iterations
        if ITI_Ticker <= const_ITI_Interval:
            while ITI_Float <= 30:
                # Choosing ITI Number randomly for ITI timer
                print('ITI ', ITI_Ticker,' Timer: Creating ITI Timer')
                ITI_Float = int(random.choice(ITI_Pool))
                print('ITI Timer', ITI_Ticker, ': Generated', ITI_Float, 'sec for ITI')
            print('ITI Timer', ITI_Ticker, ': Chose', ITI_Float, 'sec for ITI')
            # Exceptional case for ITI iterations
            ITI_Ticker_Math = ITI_Ticker - 1
            if ITI_Ticker_Math%const_ITI_Delay_Div==0 and ITI_Ticker > 1:
                print('ITI ', ITI_Ticker,' Extending additional', const_ITI_Delay_Amount,'sec after', const_ITI_Delay_Div,' ITI')
                ITI_T = ITI_Float + const_ITI_Delay_Amount
            else:
                ITI_T = ITI_Float
            # Starting ITI Timer
            print('ITI ', ITI_Ticker,' Timer: Starting ITI Timer')
            p_Timer.ITI_T.setPeriod(1)
            p_Timer.ITI_T.setRepeats(ITI_T)
            p_Timer.ITI_T.start()
        else:
            print('ITI Timer: Ending ITI, Switching to Finish Class')
            p_State.switch(Finish)
    def s_ITI_T_tick(count):
        if count == ITI_T - 30:
            print('ITI ', ITI_Ticker,' Event: Switching to ITI Event')
            p_State.switch(ITI_Event)

class ITI_Event:      #StateID = ?
    def s_State_enter():
        print('ITI ', ITI_Ticker,' Event: Event Started')
        p_Rig.o_R_Lever_Light.turnOn()
        print('ITI ', ITI_Ticker,' Event: Left Lever Light Turned On')
    def s_i_R_Lever_Press_rise():
        print('ITI ', ITI_Ticker,' Event: Left Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI ', ITI_Ticker,' Event: Sucrose Dispensed')
    def s_ITI_T_tick(count):
        if count == ITI_T:
            p_Rig.o_R_Lever_Light.turnOff()
            print('ITI ', ITI_Ticker,' Event: Turn off Left Lever Light')
            print('ITI ', ITI_Ticker,' Event: Completed, switching to ITI Timer Class')
            p_State.switch(ITI_Timer)

# =================+++++++================= #

class Finish:      #StateID = ?
    def s_State_enter():
        print('ITI Finish: ITI Scheduling finished, shutting down')
        syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# = #
