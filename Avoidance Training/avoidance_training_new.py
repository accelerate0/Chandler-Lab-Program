# Pynapse Source #

import numpy as np
import time
# ISSUES
# ITI Tone is 300 seconds FIXED?
# Keeps going after ITI 9 FIXED?
#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_VISchedule = 30           # Variable interval schedule with mean interval (in sec)
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)
const_ExperimentTime = 3600     # Time of Entire Experiment
# Static VI Timers:
VI1_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # Random number generator via floating point of Gaussian function
VI2_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # (mean average, standard deviation, amount of numbers)
VI3_Float = int(np.round(np.random.normal(const_VISchedule,5,1))) # 3 for 3 VI intervals
# Declaring Global Variables That Will Change During ITI:
ITI_Ticker = 1
ITI_Float = 0
ITI_T_1 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_T = 0
ITI_T_28 = 0
ITI_T_30 = 0
# Declaring Global Variables That Will Change During VI:
VI_Ticker = 1

#==========================================================#
#                   Actual Program                         #
#==========================================================#

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
        "The VI numbers generated are ", VI1_Float, " ", VI2_Float, " ", VI3_Float, " seconds", '\n', '\n')
        print('Switching to PreTrial class')
        print('ITI 1: Initiating ITI Intervaling')
        print('ITI 1: Generated', ITI_T_1, '(sec) as the first ITI')
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        global ITI_Ticker, ITI_Float, ITI_T, ITI_T_28, ITI_T_30
        if count == const_ExperimentTime:
            print(const_ExperimentTime, ' sec (60 min) has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)
        # ===== Conditional Based ITI Scheduling: 1 Time ===== #
        elif count == ITI_T_1:
            print('ITI 1: ITI Finished')
            ITI_T_28 = ITI_T_1 + 28
            ITI_T_30 = ITI_T_1 + 30
            p_Rig.o_Tone.turnOn()
            print('ITI 1: Tone On')
        # ===== Conditional Based ITI Scheduling: Looping 2-9 ===== #
        elif count == ITI_T_28:
            p_Rig.o_Shock.turnOn()
            print('ITI ', ITI_Ticker,': Shock On')
        elif count == ITI_T_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI ', ITI_Ticker,': Tone & Shock Off')
            ITI_Float = int(np.round(np.random.normal(const_ITI,5,1)))
            ITI_T = ITI_T_30 + ITI_Float
            ITI_Ticker = ITI_Ticker + 1
            print('ITI', ITI_Ticker, ': Using', ITI_Float, '(sec) for', ITI_Ticker, 'ITI interval')
            if 1 < ITI_Ticker <= 9:
                if ITI_Ticker == 4 or ITI_Ticker == 7:
                    print('Entering an additional 300 second ITI Delay')
                    ITI_T = ITI_T + 300
                    ITI_T_28 = ITI_T + 28
                    ITI_T_30 = ITI_T + 30
                else:
                    ITI_T_28 = ITI_T + 28
                    ITI_T_30 = ITI_T + 30
            elif ITI_Ticker == 10:
                print('ITI Finished')
            else:
                pass
        elif count == ITI_T:
            p_Rig.o_Tone.turnOn()
            print('ITI ', ITI_Ticker,': Tone On')

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Lever is Out')
        print('Pretrial: Switching to VI 1 Timer Class')
        p_State.switch(VI_Timer) # Switches to Trial class

# =================+++++++================= #

class VI_Timer:    #StateID = ?
    def s_State_enter():
        global VI_Ticker
        if VI_Ticker == 1:
            p_Timer.VI_T.setRepeats(VI1_Float)
            print('VI 1 Timer: Initiating timer')
        elif VI_Ticker == 2:
            p_Timer.VI_T.setRepeats(VI2_Float)
            print('VI 2 Timer: Initiating timer')
        elif VI_Ticker == 3:
            p_Timer.VI_T.setRepeats(VI3_Float)
            print('VI 3 Timer: Initiating timer')
        elif VI_Ticker == 4:
            p_Timer.VI_T.setRepeats(VI1_Float)
            print('VI Interval reset back to VI 1')
            print('VI 1 Timer: Initiating timer')
            VI_Ticker = 1
        print('Entering VI ', VI_Ticker)
        p_Rig.o_L_Lever_Light.turnOff()
        print('VI ', VI_Ticker,' Timer: Turned off lever light')
        p_Timer.VI_T.setPeriod(1) # First random ~30 sec timer
        p_Timer.VI_T.start()
        print('VI ', VI_Ticker,' Timer: Starting timer')
    def s_VI_T_tick(count):
        if VI_Ticker == 1:
            if count == VI1_Float:
                print('VI 1 Timer: Interval complete, switching to Event class')
                p_State.switch(VI_Event)
        elif VI_Ticker == 2:
            if count == VI2_Float:
                print('VI 2 Timer: Interval complete, switching to Event class')
                p_State.switch(VI_Event)
        elif VI_Ticker == 3:
            if count == VI3_Float:
                print('VI 3 Timer: Interval complete, switching to Event class')
                p_State.switch(VI_Event)
class VI_Event:    #StateID = ?
    def s_State_enter():
        print('VI ', VI_Ticker,' Event: Entering Event class')
        p_Rig.o_L_Lever_Light.turnOn()
        print('VI ', VI_Ticker,' Event: Left Lever Light On')
        p_State.setTimeout(const_CorrectResponse, VI_Reset) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        print('VI ', VI_Ticker,' Event: Lever was pressed, switching to Reward class')
        p_State.switch(VI_Reward)
class VI_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI ', VI_Ticker,' Reward: Sucrose dispensed')
        print('VI ', VI_Ticker,' Reward: Switching to Timer class')
        p_State.switch(VI_Reset)
class VI_Reset:   #StateID = ?
    def s_State_enter():
        global VI_Ticker
        VI_Ticker = VI_Ticker + 1
        print('VI Reset: Resetting VI Loop')
        p_State.switch(VI_Timer)


# = #
