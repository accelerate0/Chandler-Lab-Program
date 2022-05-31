# Pynapse Source #

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables:
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)
const_ExperimentTime = 3600    # Time of Entire Experiment

# Creating VI Scheduling
float_1 = int(np.round(np.random.normal(const_VISchedule,5,1))) # Random number generator via floating point of Gaussian function
float_2 = int(np.round(np.random.normal(const_VISchedule,5,1))) # (mean average, standard deviation, amount of numbers)
float_3 = int(np.round(np.random.normal(const_VISchedule,5,1))) # 3 for 3 VI intervals

# Creating ITI Scheduling
ITI_Float_1 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_2 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_3 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_4 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_5 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_6 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_7 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_8 = int(np.round(np.random.normal(const_ITI,5,1)))
ITI_Float_9 = int(np.round(np.random.normal(const_ITI,5,1)))

ITI_T1 = ITI_Float_1
ITI_T1_28 = ITI_T1 + 28
ITI_T1_30 = ITI_T1 + 30

ITI_T2 = ITI_T1 + ITI_Float_2 + 30
ITI_T2_28 = ITI_T2 + 28
ITI_T2_30 = ITI_T2 + 30

ITI_T3 = ITI_T2 + ITI_Float_3 + 30
ITI_T3_28 = ITI_T3 + 28
ITI_T3_30 = ITI_T3 + 30

ITI_T4 = ITI_T3 + ITI_Float_4 + 300 + 30
ITI_T4_28 = ITI_T4 + 28
ITI_T4_30 = ITI_T4 + 30

ITI_T5 = ITI_T4 + ITI_Float_5 + 30
ITI_T5_28 = ITI_T5 + 28
ITI_T5_30 = ITI_T5 + 30

ITI_T6 = ITI_T5 + ITI_Float_6 + 30
ITI_T6_28 = ITI_T6 + 28
ITI_T6_30 = ITI_T6 + 30

ITI_T7 = ITI_T6 + ITI_Float_7 + 300 + 30
ITI_T7_28 = ITI_T7 + 28
ITI_T7_30 = ITI_T7 + 30

ITI_T8 = ITI_T7 + ITI_Float_8 + 30
ITI_T8_28 = ITI_T8 + 28
ITI_T8_30 = ITI_T8 + 30

ITI_T9 = ITI_T8 + ITI_Float_9 + 30
ITI_T9_28 = ITI_T9 + 28
ITI_T9_30 = ITI_T9 + 30

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
        "const_CorrectResponse =", const_CorrectResponse, '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_ITI =", const_ITI, '\n', '\n', '\n',
        "The ITI numbers generated are ", ITI_Float_1, ITI_Float_2, ITI_Float_3, ITI_Float_4, ITI_Float_5, ITI_Float_6, ITI_Float_7, ITI_Float_8, ITI_Float_9, "seconds"'\n', '\n'
        )
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        if count == 900:
            print('15 minutes have passed')
        elif count == 1800:
            print('30 minutes have passed')
        elif count == 2700:
            print('45 minutes have passed')
        elif count == const_ExperimentTime:
            print('60 min has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Left Lever is Out')
        p_State.switch(ITI_1_Timer) # Switches to Trial class


# =================+++++++================= #
# === Conditional Based ITI Scheduling === #

# _____________ # ITI 1

class ITI_1_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 1: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_1:
            p_Rig.o_Tone.turnOn()
            print('ITI 1: Tone On')
            p_State.switch(ITI_1_Event)

class ITI_1_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 1: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 1: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T1_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 1: Shock On')
        elif count == ITI_T1_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 1: Turn off Shock & Tone')
            print('ITI 1: Completed')
            p_State.switch(ITI_2_Timer)

# _____________ # ITI 2

class ITI_2_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 2: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_2:
            p_Rig.o_Tone.turnOn()
            print('ITI 2: Tone On')
            p_State.switch(ITI_2_Event)

class ITI_2_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 2: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 2: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T2_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 2: Shock On')
        elif count == ITI_T2_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 2: Turn off Shock & Tone')
            print('ITI 2: Completed')
            p_State.switch(ITI_3_Timer)

# _____________ # ITI 3

class ITI_3_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 3: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_3:
            p_Rig.o_Tone.turnOn()
            print('ITI 3: Tone On')
            p_State.switch(ITI_3_Event)

class ITI_3_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 3: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 3: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T3_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 3: Shock On')
        elif count == ITI_T3_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 3: Turn off Shock & Tone')
            print('ITI 3: Completed')
            p_State.switch(ITI_4_Timer)

# _____________ # ITI 4

class ITI_4_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 4: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_4:
            p_Rig.o_Tone.turnOn()
            print('ITI 4: Tone On')
            p_State.switch(ITI_4_Event)

class ITI_4_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 4: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 4: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T4_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 4: Shock On')
        elif count == ITI_T4_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 4: Turn off Shock & Tone')
            print('ITI 4: Completed')
            p_State.switch(ITI_5_Timer)

# _____________ # ITI 5

class ITI_5_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 5: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_5:
            p_Rig.o_Tone.turnOn()
            print('ITI 5: Tone On')
            p_State.switch(ITI_5_Event)

class ITI_5_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 5: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 5: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T5_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 5: Shock On')
        elif count == ITI_T5_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 5: Turn off Shock & Tone')
            print('ITI 5: Completed')
            p_State.switch(ITI_6_Timer)

# _____________ # ITI 6

class ITI_6_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 6: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_6:
            p_Rig.o_Tone.turnOn()
            print('ITI 6: Tone On')
            p_State.switch(ITI_6_Event)

class ITI_6_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 6: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 6: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T6_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 6: Shock On')
        elif count == ITI_T6_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 6: Turn off Shock & Tone')
            print('ITI 6: Completed')
            p_State.switch(ITI_7_Timer)

# _____________ # ITI 7

class ITI_7_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 7: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_7:
            p_Rig.o_Tone.turnOn()
            print('ITI 7: Tone On')
            p_State.switch(ITI_7_Event)

class ITI_7_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 7: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 7: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T7_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 7: Shock On')
        elif count == ITI_T7_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 7: Turn off Shock & Tone')
            print('ITI 7: Completed')
            p_State.switch(ITI_8_Timer)

# _____________ # ITI 8

class ITI_8_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 8: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_8:
            p_Rig.o_Tone.turnOn()
            print('ITI 8: Tone On')
            p_State.switch(ITI_8_Event)

class ITI_8_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 8: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 8: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T8_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 8: Shock On')
        elif count == ITI_T8_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 8: Turn off Shock & Tone')
            print('ITI 8: Completed')
            p_State.switch(ITI_9_Timer)

# _____________ # ITI 9

class ITI_9_Timer:      #StateID = ?
    def s_State_enter():
        print('ITI 9: Timer Started')
    def s_Global_T_tick(count):
        if count == ITI_9:
            p_Rig.o_Tone.turnOn()
            print('ITI 9: Tone On')
            p_State.switch(ITI_9_Event)

class ITI_9_Event:      #StateID = ?
    def s_State_enter():
        print('ITI 9: Event Started')
    def s_i_L_Lever_Press_rise():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('ITI 9: Sucrose Dispensed')
    def s_Global_T_tick(count):
        if count == ITI_T9_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 9: Shock On')
        elif count == ITI_T9_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 9: Turn off Shock & Tone')
            print('ITI 9: Completed')
            p_State.switch(Finish)

class Finish:      #StateID = ?
    def s_State_enter():
        print('ITI Intervaling Finished, entering grace period')
    def s_Global_T_tick(count):
        print(const_ExperimentTime - count, 'sec before shutdown')







# = #
