# Pynapse Source #

#==========================================================#
#                      Dependencies                        #
#==========================================================#

import numpy as np
import time
import random
import pyopcond_dep as pyop

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_ExperimentTime = 3600     # Time of Entire Experiment
const_VI_Mean = 30              # VI scheduling mean interval (sec)
const_VISchedule_Amt = 10       # Amount of VI schedule numbers generated
const_ITISchedule_Amt = 5       # Amount of ITI schedule numbers generated
const_ITI_Mean = 180            # ITI scheduling mean interval (sec)
const_ITI_Interval = 9          # Amount of ITI's scheduling
const_ITI_Add_Delay = 300       # Additional ITI Delay

# =================+++++++================= #
# ! DO NOT CHANGE ANYTHING HERE !
# This is for controlling program flow and to follow & ensure specific, sequential executions of functions

# Global Dynamic VI Timer & Related Variables:
VI1_Float = 0       # Related to VI Timer 1 declaration & mathematics
VI2_Float = 0       # Related to VI Timer 2 declaration & mathematics
VI3_Float = 0       # Related to VI Timer 3 declaration & mathematics
VI_Pool = 0         # Related to PyOp VI array generation in number pools
VI_Ticker = 1       # Keeps track of how many VI iterations have passed, starts at VI 1 interval
VI_Timing = 0       # The actual VI Timer setting (sec) that is executed

# Global Dynamic Variables That Will Change During ITI:
ITI_Ticker = 0      # Keeps track of how many ITI iterations have passed, starts at ITI 1 interval
ITI_Float = 0       # Randomly generated number for ITI intervaling choosing from ITI_Pool, in sec
ITI_T = 1           # The actual ITI summation value in sec which triggers the tone
ITI_Pool = 0        # Array generation of ITI number pools from PyOp
ITI_Interval = 0    # Keeps track of how many ITI's passed
ITI_Switch = 0      # Controls program flow and ensures correct order of execution in ITI

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        # Declaring changing Global Variables
        global VI1_Float, VI2_Float, VI3_Float, VI_Pool, ITI_Pool
        # Printing Constants on Console
        print( "Global: Printing Experimental Presets", '\n', '\n',
        "Global: const_ExperimentTime =", const_ExperimentTime, '\n',
        "Global: const_VI_Mean =", const_VI_Mean, '\n',
        "Global: const_VISchedule_Amt =", const_VISchedule_Amt, '\n',
        "Global: const_ITISchedule_Amt =", const_ITISchedule_Amt, '\n',
        "Global: const_ITI_Interval =", const_ITI_Interval, '\n',
        "Global: const_ITI_Add_Delay =", const_ITI_Add_Delay, '\n',
        "Global: const_ITI_Mean =", const_ITI_Mean,
        '\n', '\n', '\n')
        # Setting Up Global Timer
        print('Global: Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1)
        p_Timer.Global_T.setRepeats(const_ExperimentTime)
        print('Global: Starting the global experimental', const_ExperimentTime, ' sec timer')
        p_Timer.Global_T.start()
        # Setting Up VI Timer Schedule via PyOp
        pyop.var_int(const_VISchedule_Amt, const_VI_Mean)
        VI_Pool = pyop.var_int.output_straight
        print("Global: Generated", VI_Pool, "VI Pool from PyOp")
        while VI1_Float == 0 and VI2_Float == 0 and VI3_Float == 0:
            VI1_Float = int(random.choice(VI_Pool))
            VI2_Float = int(random.choice(VI_Pool))
            VI3_Float = int(random.choice(VI_Pool))
            if VI1_Float > 0 and VI2_Float > 0 and VI3_Float > 0:
                print("Global: The VI numbers generated are ", VI1_Float, " ", VI2_Float, " ", VI3_Float, " seconds", '\n', '\n')
                break
        # Setting Up ITI Timer Schedule via PyOp
        pyop.var_int(const_ITISchedule_Amt, const_ITI_Mean)
        ITI_Pool = pyop.var_int.output_straight
        print("Global: Generated:", ITI_Pool, "ITI Pool from PyOp")
        # Switch to PreTrial class
        print('Global: Switching to PreTrial class')
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        global ITI_Switch
        # Shuts down entire experiment
        if count == const_ExperimentTime:
            print(const_ExperimentTime, ' sec (60 min) has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)
        if count == count: # Anything here is always being checked and executed
            # Related to ITI, hacking Pynapse to allow parallel execution of ITI alongside VI
            # Using short 1 sec timers to force ITI's to occur and switching from ITI to ITI
            if ITI_Switch == 0:
                # Initiating ITI Timer creation for the first time
                print('ITI: Initializing the ITI Timer for the first time')
                ITI_Switch = 1
                p_Timer.ITI_T.setPeriod(1)
                p_Timer.ITI_T.setRepeats(ITI_Switch)
                p_Timer.ITI_T.start()
            if ITI_Switch == 3:
                # Initiating ITI Timer creation subsequently
                ITI_Switch = 1
                p_Timer.ITI_T.setPeriod(1)
                p_Timer.ITI_T.setRepeats(ITI_Switch)
                p_Timer.ITI_T.start()

    # ===== Conditional Based ITI Scheduling ===== #
    def s_ITI_T_tick(count):
        global ITI_Float, ITI_T, ITI_Ticker, ITI_Switch
        if count == 1 and ITI_Switch == 1:
            ITI_Switch = -1
            print('ITI Timer: Setting up the ITI Timer')
            if ITI_Ticker <= const_ITI_Interval:
                ITI_Ticker = ITI_Ticker + 1
                print('ITI Timer', ITI_Ticker, ': Entered')
                ITI_T = 0
                ITI_Float = 0
                while ITI_Float <= 30:
                    ITI_Float = int(random.choice(ITI_Pool))
                    print('ITI Timer', ITI_Ticker, ': Generated', ITI_Float, 'sec for ITI')
                    break
                if ITI_Ticker == 4 or ITI_Ticker == 7:
                    ITI_T = ITI_Float + const_ITI_Add_Delay
                    print('ITI Timer', ITI_Ticker, ': Added additional', const_ITI_Add_Delay, 'delay')
                else:
                    ITI_T = ITI_Float
                p_Timer.ITI_T.setPeriod(1)
                p_Timer.ITI_T.setRepeats(ITI_T)
                print('ITI Timer', ITI_Ticker, ': Started ITI Timer')
                p_Timer.ITI_T.start()
                ITI_Switch = 2
        if count == ITI_T - 30 and ITI_Switch == 2:
            p_Rig.o_Tone.turnOn()
            print('ITI Timer', ITI_Ticker, ': Tone On')
        if count == ITI_T - 28 and ITI_Switch == 2:
            p_Rig.o_Shock.turnOn()
            print('ITI Timer', ITI_Ticker, ': Shock On')
        if count == ITI_T and ITI_Switch == 2:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI Timer', ITI_Ticker, ': Shock & Tone Off')
            print('ITI Timer', ITI_Ticker, ': Reinitializing ITI Timer')
            ITI_Switch = 3



# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        # Creates static experimental environment
        p_Rig.o_House_Light.turnOn()
        print('Pretrial: Light is On')
        p_Rig.o_L_Lever_Extension.turnOn()
        print('Pretrial: Lever is Out')
        print('Pretrial: Switching to VI Timer Class')
        # Switch Class
        print('Pretrial: Switching to VI Timer Class')
        p_State.switch(VI_Timer)

# =================+++++++================= #

class VI_Timer:    #StateID = ?
    def s_State_enter():
        global VI_Timing
        VI_Timing = 0
        if VI_Ticker == 1:
            VI_Timing = VI1_Float
            p_Timer.VI_T.setRepeats(VI1_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        elif VI_Ticker == 2:
            VI_Timing = VI2_Float
            p_Timer.VI_T.setRepeats(VI2_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        elif VI_Ticker == 3:
            VI_Timing = VI3_Float
            p_Timer.VI_T.setRepeats(VI3_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        p_Timer.VI_T.setPeriod(1)
        p_Timer.VI_T.start()
        print('VI ', VI_Ticker,' Timer: VI Timer Started')
    def s_VI_T_tick(count):
        if count == VI_Timing:
            print('VI ', VI_Ticker,' Timer: Interval complete, switching to VI Event class')
            p_State.switch(VI_Event)

class VI_Event:    #StateID = ?
    def s_State_enter():
        print('VI ', VI_Ticker,' Event: Entering Event class')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI ', VI_Ticker,' Event: Left Lever Light On')
    def s_i_L_Lever_Press_rise():
        print('VI ', VI_Ticker,' Event: Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn()
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI ', VI_Ticker,' Event: Reward dispensed')
        p_Rig.o_L_Lever_Light.turnOff()
        print('VI ', VI_Ticker,' Event: Lever Lever Light Off')
        print('VI ', VI_Ticker,' Event: Switching to VI Check Class')
        p_State.switch(VI_Check)

class VI_Check:   #StateID = ?
    def s_State_enter():
        global VI_Ticker
        VI_Ticker = VI_Ticker + 1
        if VI_Ticker == 4:
            print('VI Reset: Ending', VI_Ticker - 1, 'VI and Reseting to VI 1')
            VI_Ticker = 1
        else:
            print('VI Reset: Ending', VI_Ticker - 1, 'VI and Entering VI', VI_Ticker)
        p_State.switch(VI_Timer)

# = #
