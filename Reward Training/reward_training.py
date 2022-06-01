# Pynapse Source #

# From Rivera et al 2021
# After completing avoidance training, rats were placed in the same
# operant chambers with sucrose pellets available only during 30 s
# periods when a light cue positioned above the pellet dispenser
# was illuminated (see Figure 1). A pellet was dispensed with
# each lever press (one-to-one). Each reward conditioning session
# consisted of 20 trials and ∼180 s inter-trial intervals. A total
# of three sessions were given across 3 days, a point where most
# animals reached the criterion of limiting pressing to the period of
# the light cue.

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables:
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)
const_ExperimentTime = 4500     # Time of Entire Experiment

# Defining Variables
ITI_Ticker = 0
ITI_T = 0
ITI_T_30 = 0
ITI_Float = 0


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
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_ITI =", const_ITI, '\n', '\n', '\n'
        )
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        if count == 900:
            print('15 minutes have passed')
        elif count == 1800:
            print('30 minutes have passed')
        elif count == 2700:
            print('45 minutes have passed')
        elif count == 3600:
            print('60 minutes have passed')
        elif count == const_ExperimentTime:
            print('75 min has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Left Lever is Out')
        p_State.switch(ITI_Timer_First) # Switches to Trial class


# =================+++++++================= #

class ITI_Timer_First:      #StateID = ?
    def s_State_enter():
        print('ITI 1 Timer: Timer is initiating')
        ITI_Float = int(np.round(np.random.normal(const_ITI,5,1)))
        ITI_T = ITI_Float
        ITI_Ticker == ITI_Ticker + 1
        print('ITI 1 Timer: Randomly chose', ITI_Float, 'sec for the', ITI_Ticker, 'interval out of 20')
        print('ITI 1 Timer:Total time elapsed is 0 sec')
    def s_Global_T_tick(count):
        if count == ITI_T:
            print('ITI Event: Switching to ITI Event')
            p_State.switch(ITI_Event_First)

class ITI_Event_First:      #StateID = ?
    def s_State_enter():
        print('ITI 1 Event: Event Started')
        p_Rig.o_L_Lever_Light.turnOn()
        print('ITI 1 Event: Left Lever Light Turned On')
    def s_i_L_Lever_Press_rise():
        print('ITI 1 Event: Left Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 1 Event: Sucrose Dispensed')
    def s_Global_T_tick(count):
        ITI_T_30 = ITI_T + 30
        if count == ITI_T_30:
            p_Rig.o_L_Lever_Light.turnOff()
            print('ITI 1 Event: Turn off Left Lever Light')
            print('ITI 1 Event: Completed')
            p_State.switch(ITI_Timer_Loop)

# =================+++++++================= #

class ITI_Timer_Loop:      #StateID = ?
    def s_State_enter():
        print('ITI Loop: Timer is initiating')
        ITI_Float = int(np.round(np.random.normal(const_ITI,5,1)))
        ITI_T = ITI_Float + ITI_T_30
        ITI_Ticker == ITI_Ticker + 1
        print('ITI ', ITI_Ticker,' Loop: Randomly chose', ITI_Float, 'sec for the', ITI_Ticker, 'interval out of 20')
        print('ITI ', ITI_Ticker,' Loop: Total time elapsed is', ITI_T, 'sec')
        if ITI_Ticker == 20:
            print('ITI ', ITI_Ticker,' Loop: ITI has reached 20th trial')
            p_State.switch(Finish)
    def s_Global_T_tick(count):
        if count == ITI_T:
            print('ITI ', ITI_Ticker,' Event: Switching to ITI Event')
            p_State.switch(ITI_Event_Loop)

class ITI_Event_Loop:      #StateID = ?
    def s_State_enter():
        print('ITI ', ITI_Ticker,' Event: Event Started')
        p_Rig.o_L_Lever_Light.turnOn()
        print('ITI ', ITI_Ticker,' Event: Left Lever Light Turned On')
    def s_i_L_Lever_Press_rise():
        print('ITI ', ITI_Ticker,' Event: Left Lever was pressed')
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI ', ITI_Ticker,' Event: Sucrose Dispensed')
    def s_Global_T_tick(count):
        ITI_T_30 = ITI_T + 30
        if count == ITI_T_30:
            p_Rig.o_L_Lever_Light.turnOff()
            print('ITI ', ITI_Ticker,' Event: Turn off Left Lever Light')
            print('ITI ', ITI_Ticker,' Event: Completed')
            p_State.switch(ITI_Timer_Loop)

# =================+++++++================= #

class Finish:      #StateID = ?
    def s_State_enter():
        print('ITI 20: ITI Intervaling Finished, entering grace period')
    def s_Global_T_tick(count):
        print(const_ExperimentTime - count, 'sec before shutdown (Experiment Finished)')

# = #
