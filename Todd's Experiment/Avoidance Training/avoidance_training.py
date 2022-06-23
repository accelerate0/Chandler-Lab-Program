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
const_VI_Mean = 30           # Variable interval schedule with mean interval (in sec)
const_VISchedule_Amt = 10       # Amount of VI schedule numbers generated
const_VICorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITISchedule_Amt = 5       # Amount of ITI schedule numbers generated
const_ITI_Mean = 180            # Mean Inter-Trial Interval (ITI) (in sec)
const_ITI_Interval = 9          # Amount of ITI
const_ITI_Add_Delay = 300

# =================+++++++================= #

# Global Dynamic VI Timer & Related Variables:
VI1_Float = 0
VI2_Float = 0
VI3_Float = 0
VI_Pool = 0
VI_Ticker = 1       # Keeps track of how many VI iterations have passed, starts at VI 1 interval
VI_Latency = 0
VI_Latency_Start = 0
VI_Latency_End = 0
# Global Dynamic Variables That Will Change During ITI:
ITI_Ticker = 0      # Keeps track of how many ITI iterations have passed, starts at ITI 1 interval
ITI_Float = 0       # Randomly generated number for ITI intervaling, in sec
ITI_T = 0           # The actual ITI summation value in sec which triggers the tone
ITI_Pool = 0
ITI_Interval = 0


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
        "Global: const_VICorrectResponse =", const_VICorrectResponse, '\n',
        "Global: const_ITISchedule_Amt =", const_ITISchedule_Amt, '\n',
        "Global: const_ITI_Interval =", const_ITI_Interval, '\n',
        "Global: const_ITI_Add_Delay =", const_ITI_Add_Delay, '\n',
        "Global: const_ITI_Mean =", const_ITI_Mean,
        '\n', '\n', '\n')
        # Setting Up Global Timer
        print('Global: Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Global: Starting the global experimental', const_ExperimentTime, ' sec timer')
        p_Timer.Global_T.start() # Turn on timer
        # Setting Up VI Timer Schedule via PyOp
        pyop.var_int(const_VISchedule_Amt, const_VI_Mean)
        VI_Pool = var_int.output_straight
        print("Global: Generated", VI_Pool, "VI Pool from PyOp")
        VI1_Float = int(random.choice(VI_Pool))
        VI2_Float = int(random.choice(VI_Pool))
        VI3_Float = int(random.choice(VI_Pool))
        print("Global: The VI numbers generated are ", VI1_Float, " ", VI2_Float, " ", VI3_Float, " seconds", '\n', '\n')
        # Setting Up ITI Timer Schedule via PyOp
        pyop.var_int(const_ITISchedule_Amt, const_ITI_Mean)
        ITI_Pool = var_int.output_straight
        print("Global: Generated:", ITI_Pool, "ITI Pool from PyOp")
        # Switch to PreTrial class
        print('Global: Switching to PreTrial class')
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        # Shuts down entire experiment
        if count == const_ExperimentTime:
            print(const_ExperimentTime, ' sec (60 min) has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        # Creates static experimental environment
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Lever is Out')
        print('Pretrial: Switching to VI Timer Class')
        p_State.switch(VI_Timer) # Switches to Trial class

# =================+++++++================= #

class VI_Timer:    #StateID = ?
    def s_State_enter():
        global VI_Ticker, VI_Float
        VI_Float = 0
        if VI_Ticker == 1:
            VI_Float = VI1_Float
            p_Timer.VI_T.setRepeats(VI_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        elif VI_Ticker == 2:
            VI_Float = VI2_Float
            p_Timer.VI_T.setRepeats(VI_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        elif VI_Ticker == 3:
            VI_Float = VI3_Float
            p_Timer.VI_T.setRepeats(VI_Float)
            print('VI ', VI_Ticker,' Timer: Initiating timer')
        p_Rig.o_L_Lever_Light.turnOff()
        print('VI ', VI_Ticker,' Timer: Turned off lever light')
        p_Timer.VI_T.setPeriod(1)
        p_Timer.VI_T.start()
        print('VI ', VI_Ticker,' Timer: Starting timer')
    def s_VI_T_tick(count):
        if count == VI_Float:
            print('VI ', VI_Ticker,' Timer: Interval complete, switching to Event class')
            p_State.switch(VI_Event)

class VI_Event:    #StateID = ?
    def s_State_enter():
        global VI_Latency_Start
        print('VI ', VI_Ticker,' Event: Starting Latency Measurement')
        VI_Latency_Start = time.time()
        print('VI ', VI_Ticker,' Event: Entering Event class')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI ', VI_Ticker,' Event: Left Lever Light On')
    def s_i_L_Lever_Press_rise():
        global VI_Latency_End, VI_Latency
        print('VI ', VI_Ticker,' Event: Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn()
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI ', VI_Ticker,' Event: Reward dispensed')
        print('VI ', VI_Ticker,' Event Switching to Reset class')
        VI_Latency_End = time.time()
        print('VI ', VI_Ticker,' Event: Ended Latency Measurement')
        VI_Latency = int(VI_Latency_End - VI_Latency_Start)
        print('VI ', VI_Ticker,' Event: Latency is', VI_Latency,' sec')
        print('VI ', VI_Ticker,' Event: Switching to VI to ITI Class')
        p_State.switch(VI_ITI)

class VI_ITI:   #StateID = ?
    def s_State_enter():
        global ITI_Float, ITI_T, ITI_Ticker
        print('VI ITI: Entered VI to ITI class')
        if ITI_Ticker < const_ITI_Interval + 1:
            ITI_Ticker = ITI_Ticker + 1
            print('VI ITI', ITI_Ticker,': Calculating ITI Timings')
            ITI_T = 0
            ITI_Float = 0
            while ITI_Float =< VI_Float + VI_Latency:
                ITI_Float = int(random.choice(ITI_Pool))
                print('VI ITI', ITI_Ticker, ': Chose', ITI_Float, ' sec as the ITI, chekcing ITI parameters')
                if ITI_Float => VI_Float + VI_Latency:
                    print('VI ITI', ITI_Ticker, ': Chose', ITI_Float, ' sec for the ITI')
                    ITI_T = ITI_Float - VI_Float - VI_Latency
                    print('VI ITI', ITI_Ticker, ': Calculated ', ITI_T, ' sec for the remaining delay')
                    if ITI_Ticker == 4 or ITI_Ticker == 7:
                        ITI_T = ITI_T + const_ITI_Add_Delay
                        print('VI ITI', ITI_Ticker, ': Adding an additional ', const_ITI_Add_Delay, ' sec delay for a', ITI_T, 'sec total delay')
                    break
            p_State.switch(ITI_Timer)
        else:
            print('VI ITI: ITI Ticker is greater than', const_ITI_Interval, 'sec, switching to VI Timer')
            p_State.switch(VI_Timer)

class ITI_Timer:  #StateID = ?
    def s_State_enter():
        p_Timer.ITI_T.setPeriod(1)
        p_Timer.ITI_T.setRepeats(ITI_T)
        p_Timer.ITI_T.start()
        print('ITI Timer', ITI_Ticker, ': Started the ITI delay timer as ', ITI_T, ' sec')
    def s_ITI_T_tick(count):
        if count == ITI_T - 30:
            print('ITI Timer', ITI_Ticker, ': Tone On')
            p_Rig.o_Tone.turnOn()
        if count == ITI_T - 28:
            print('ITI Timer', ITI_Ticker, ': Shock On')
            p_Rig.o_Shock.turnOn()
        if count == ITI_T:
            print('ITI Timer', ITI_Ticker, ': Shock & Tone Off')
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI Timer', ITI_Ticker, ': Switching to VI Check')
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
