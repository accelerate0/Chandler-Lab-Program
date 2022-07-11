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

# Global Dynamic Variables (Do Not Change):
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
        print('Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Starting the global experimental', const_ExperimentTime,'sec timer')
        p_Timer.Global_T.start() # Turn on timer
        # Printing constants
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_DispenseTime =", const_DispenseTime, '\n',
        "const_RIFloat =", const_RIFloat, '\n')
        # Setting up RI Schedule via PyOp
        RI_Amount = const_ExperimentTime/const_RIFloat
        pyop.rand_int(const_RIFloat, RI_Amount)
        pyop.rand_int.output.sort()
        RI_Pool = pyop.rand_int.output
        print("(PyOP RI) Probability factor (prob/sec):", pyop.rand_int.prob)
        print("(PyOP RI) RI mean (sec):", pyop.rand_int.interval)
        print("(PyOP RI) Amount of RI intervals (This multiplied by RI mean should be equal to experimental time):", pyop.rand_int.amount)
        print('(PyOP RI) Generated RI Schedule:', '\n',
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
        print('Timer: Chose the', RI_Ticker, '-th number on the RI List Array')
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
        print('Event: Left Lever (active lever) was pressed, Initiating Dispense')
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Event: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
        p_State.switch(Timer)
    def s_i_R_Lever_Press_rise():
        print('Event: Right Lever (inactive lever) was pressed, nothing happens')

# = #
