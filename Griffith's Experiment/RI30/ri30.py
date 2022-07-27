# Pynapse Source #

import time
import pyopcond_dep as pyop
import random

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_ExperimentTime = 1800         # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense rate of the liquid dispenser (sec)
const_RIFloat = 30                  # RI mean based scheduling (sec), for example, an RI30 would be 30
const_Mode = 1                      # Set the active lever (both levers will be extended regardless)
# const_Mode = 1  , Left Lever active
# const_Mode = 2  , Right Lever active
# const_Mode = 3  , All Levers active

# Global Dynamic Variables (!Do Not Change!):
RI_Float = 0
RI_Pool = 0
RI_Ticker = -1
RI_Amount = 0

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        global RI_Pool, RI_Amount
        # Setting up experimental timer
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        p_Timer.Global_T.start() # Turn on timer
        print('Pretrial: Started the Global Timer for', const_ExperimentTime,'sec')
        # Printing constants
        print("Pretrial: EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime (sec) =", const_ExperimentTime, '\n',
        "const_DispenseTime (sec) =", const_DispenseTime, '\n',
        "const_RIFloat (sec) =", const_RIFloat, '\n',
        "const_Mode = ", const_Mode, '\n',
        '\n')
        # Setting up RI Schedule via PyOp
        RI_Amount = int(const_ExperimentTime/const_RIFloat)
        pyop.rand_int_withpi(const_RIFloat, RI_Amount)
        pyop.rand_int_withpi.output.sort()
        RI_Pool = pyop.rand_int_withpi.output
        print("Pretrial (PyOP RI): Probability factor (prob/sec):", pyop.rand_int_withpi.prob)
        print("Pretrial (PyOP RI): RI mean (sec):", pyop.rand_int_withpi.interval)
        print("Pretrial (PyOP RI): Amount of RI intervals (This multiplied by RI mean should be equal to experimental time):", pyop.rand_int_withpi.amount)
        print('Pretrial (PyOP RI): Generated RI Schedule:', '\n',
        'Generated', RI_Pool, '(sec) as the pool', '\n')
        # Switch
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        # Global Timer expiration condition
        if count == const_ExperimentTime:
            print(const_ExperimentTime, 'sec has passed and experiment is completed, shutting down')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)


# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Left Lever is Out')
        p_Rig.o_R_Lever_Extension.turnOn() # Turns on right lever
        print('Pretrial: Right Lever is Out')
        p_State.switch(Timer) # Switches to Trial class

# =================+++++++================= #

class Timer:      #StateID = ?
    def s_State_enter():
        global RI_Float, RI_Ticker, RI_State
        RI_State = 0
        RI_Ticker = RI_Ticker + 1
        RI_Float = int(RI_Pool[RI_Ticker])
        print('Timer: Chose the', RI_Ticker + 1, '-th number on the RI Pool')
        print('Timer: Waiting until', RI_Float, 'sec until reward opportunity')
        RI_State = 1
    def s_Global_T_tick(count):
        global RI_State
        if count == RI_Float and RI_State == 1:
            RI_State = 2
            print('Timer:', RI_Float, 'sec reached, switching to Event class')
            p_State.switch(Event)
        elif count > RI_Float and RI_State == 1:
            print('Timer: Due to latency in code execution or subject input, ', RI_Float, 'sec',
            'at', RI_Ticker, 'interval could not be completed, skipping & resetting back to Timer Class')
            p_State.switch(Timer)

class Event:      #StateID = ?
    def s_i_L_Lever_Press_rise():
        if const_Mode == 1:
            print('Event: Left Lever (active lever) was pressed, initiating Dispense')
            p_State.switch(Reward)
        if const_Mode == 2:
            print('Event: Left Lever (inactive lever) was pressed, nothing happens')
        if const_Mode == 3:
            print('Event: Left Lever (active lever) was pressed, initiating Dispense')
            p_State.switch(Reward)
    def s_i_R_Lever_Press_rise():
        if const_Mode == 1:
            print('Event: Right Lever (inactive lever) was pressed, nothing happens')
        if const_Mode == 2:
            print('Event: Right Lever (active lever) was pressed, initiating Dispense')
            p_State.switch(Reward)
        if const_Mode == 3:
            print('Event: Right Lever (active lever) was pressed, initiating Dispense')
            p_State.switch(Reward)

class Reward:      #StateID = ?
    def s_State_enter():
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Event: Dispensed at', const_DispenseTime, 'sec, reinitializing Trial Timer')
        p_State.switch(Timer)
# = #
