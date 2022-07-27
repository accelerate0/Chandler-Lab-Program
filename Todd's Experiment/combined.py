# Pynapse Source #

# NOTE THIS IS A WORK IN PROGRESS
# Combination of Reward Training, Conflict Test, and Conflict Training with additional customizable functions


import logging
# Testing Logging
import numpy as np
import time
import random
import pyopcond_dep as pyop

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# =================Global Static Variables================= #

# Experimental Variables:
const_ExperimentTime = 9999         # Time of Entire Experiment (sec) for the global timer
                                    # Setting this to a large number means finishing ITI's will close the program instead

# PyOp Related Variables:
const_ITI = 180                     # Mean value of ITI (sec) for PyOp
const_ITISchedule_Amt = 5           # How many ITI number candidates are generated from PyOp

# ITI Delay Related Variables:
const_ITI_Delay_Control = 1         # Enable (1) or Disable (0) additional delay after certain ITI's
const_ITI_Delay_Amount = 300        # Delay amount (sec)
const_ITI_Delay_Div = 3             # Divisibility of the ITI delay ("Example: After every 3rd ITI interval is (3)")

# Logging Console Output
const_Log_Name = "log.log"          # Name of the log for console output, do not delete "" and must end in .log

# =================Program Mode Selection================= #

# Set the mode of the Program
const_Mode = 2
# 1 = Custom Mode
# 2 = Reward Training
# 3 = Conflict Test
# 4 = Conflict Training

# =================Custom Mode Related================= #
const_ITI_Interval = 20             # Amount of ITI Intervals (Only in Custom Mode)
# Edit "pass" function with desired triggers


# =================Dynamic Variables================= #
# ! DO NOT CHANGE ANYTHING HERE !

# Global Dynamic Variables:
ITI_Ticker = 0                      # Tracks amount of time ITI has looped
ITI_T = 0                           # Summated ITI Timer (sec)
ITI_Float = 0                       # ITI Timer (sec)
ITI_Pool = 0                        # Array store of ITI numbers from PyOp
ITI_Ticker_Math = 0


#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        global ITI_Pool, const_ITI_Interval
        # Setting up Global Timer
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        p_Timer.Global_T.start() # Turn on timer
        print('PreTrial: Started the global timer')
        # Option switching
        if const_Mode > 0:
            if const_Mode == 1:
                print('PreTrial: Mode set to 1 (Custom Mode))')
            if const_Mode == 2:
                const_ITI_Interval = 20
                print('PreTrial: Mode set to 2 (Reward Training)')
            if const_Mode == 3:
                const_ITI_Interval = 9
                print('PreTrial: Mode set to 3 (Conflict Test)')
            if const_Mode == 4:
                const_ITI_Interval = 9
                print('PreTrial: Mode set to 4 (Conflict Training)')
        # Printing Experimental Constants on console
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime (sec) = ", const_ExperimentTime, '\n',
        "const_ITI (sec) = ", const_ITI, '\n',
        "const_ITISchedule_Amt (PyOp) = ", const_ITISchedule_Amt, '\n',
        "const_ITI_Interval (Amount of ITI) = ", const_ITI_Interval, '\n',
        '\n', '\n', '\n')
        # Generating ITI number pool from PyOp
        pyop.var_int(const_ITISchedule_Amt, const_ITI)
        ITI_Pool = pyop.var_int.output_straight
        print("PreTrial (PyOp): Generated:", ITI_Pool, "ITI Pool from PyOp")
        # Logging Functionality
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        logger = logging.getLogger()
        logger.addHandler(logging.FileHandler(const_Log_Name, 'a'))
        print = logger.info
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
        # Resetting and Configuring ITI Related Variables
        ITI_T = 0
        ITI_Float = 0
        ITI_Ticker = ITI_Ticker + 1
        ITI_Ticker_Math = ITI_Ticker - 1
        # Keeping track of ITI iterations
        if ITI_Ticker <= const_ITI_Interval:
            while ITI_Float <= 30:
                # Choosing ITI Number randomly for ITI timer
                print('ITI ', ITI_Ticker,' Timer: Creating ITI Timer')
                ITI_Float = int(random.choice(ITI_Pool))
                print('ITI Timer', ITI_Ticker, ': Generated', ITI_Float, 'sec for ITI')
            print('ITI Timer', ITI_Ticker, ': Chose', ITI_Float, 'sec for ITI')
            # Exceptional case for ITI iterations for additional delays
            if const_ITI_Delay_Control == 1:
                if ITI_Ticker_Math%const_ITI_Delay_Div==0 and ITI_Ticker > 1:
                    print('ITI ', ITI_Ticker,' Extending additional', const_ITI_Delay_Amount,'sec after', const_ITI_Delay_Div,' ITI')
                    ITI_T = ITI_Float + const_ITI_Delay_Amount
                else:
                    ITI_T = ITI_Float
            else:
                ITI_T = ITI_Float
            # Starting ITI Timer
            p_Timer.ITI_T.setPeriod(1)
            p_Timer.ITI_T.setRepeats(ITI_T)
            p_Timer.ITI_T.start()
            print('ITI ', ITI_Ticker,' Timer: Started ITI Timer for', ITI_T, 'sec')
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
        if const_Mode == 1:
            pass
        if const_Mode == 3:
            p_Rig.o_Tone.turnOn()
        if const_Mode == 4:
            p_Rig.o_Tone.turnOn()
    def s_i_R_Lever_Press_rise():
        print('ITI ', ITI_Ticker,' Event: Left Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI ', ITI_Ticker,' Event: Sucrose Dispensed')
    def s_ITI_T_tick(count):
        if count == ITI_T - 2:
            if const_Mode == 1:
                pass
            if const_Mode == 4:
                p_Rig.o_Shock.turnOn()
        if count == ITI_T:
            p_Rig.o_R_Lever_Light.turnOff()
            print('ITI ', ITI_Ticker,' Event: Turn off Left Lever Light')
            if const_Mode == 1:
                pass
            if const_Mode == 3:
                p_Rig.o_Tone.turnOff()
            if const_Mode == 4:
                p_Rig.o_Shock.turnOff()
                p_Rig.o_Tone.turnOff()
            print('ITI ', ITI_Ticker,' Event: Completed, switching to ITI Timer Class')
            p_State.switch(ITI_Timer)

# =================+++++++================= #

class Finish:      #StateID = ?
    def s_State_enter():
        print('ITI Finish: ITI Scheduling finished, shutting down')
        syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# = #
