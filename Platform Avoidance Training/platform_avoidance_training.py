# Pynapse Source #
# V 6

import numpy as np
import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Variables:
const_VISchedule = 30           # Variable interval schedule with mean interval (in sec)
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)
const_ExperimentTime = 3600     # Time of Entire Experiment

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
        "const_VISchedule =", const_VISchedule, '\n',
        "const_CorrectResponse =", const_CorrectResponse, '\n',
        "const_ExperimentTime =", const_ExperimentTime, '\n',
        "const_ITI =", const_ITI, '\n', '\n', '\n',
        "The numbers generated for VI are ", float_1, " ", float_2, " ", float_3, " seconds", '\n', '\n',
        "The numbers chosen are ", ITI_Float_1, ITI_Float_2, ITI_Float_3, ITI_Float_4, ITI_Float_5, ITI_Float_6, ITI_Float_7, ITI_Float_8, ITI_Float_9, "seconds"'\n', '\n'
        )
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        if count == const_ExperimentTime:
            print('60 min has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)
        # ===== Conditional Based ITI Scheduling ===== #
        # _____ First ITI Interval _____ #
        elif count == ITI_T1:
            print('ITI 1: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 1: Tone On')
        elif count == ITI_T1_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 1: Shock On')
        elif count == ITI_T1_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 1: Turn off Shock & Tone')
            print('ITI 1: Completed')
        # === #
        elif count == ITI_T2:
            print('ITI 2: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 2: Tone On')
        elif count == ITI_T2_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 2: Shock On')
        elif count == ITI_T2_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 2: Turn off Shock & Tone')
            print('ITI 2: Completed')
        # === #
        elif count == ITI_T3:
            print('ITI 3: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 3: Tone On')
        elif count == ITI_T3_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 3: Shock On')
        elif count == ITI_T3_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 3: Turn off Shock & Tone')
            print('ITI 3: Completed')
        # _____ Second ITI Interval _____ #
        elif count == ITI_T4:
            print('ITI 4: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 4: Tone On')
        elif count == ITI_T4_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 4: Shock On')
        elif count == ITI_T4_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 4: Turn off Shock & Tone')
            print('ITI 4: Completed')
        # === #
        elif count == ITI_T5:
            print('ITI 5: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 5: Tone On')
        elif count == ITI_T5_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 5: Shock On')
        elif count == ITI_T5_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 5: Turn off Shock & Tone')
            print('ITI 5: Completed')
        # === #
        elif count == ITI_T6:
            print('ITI 6: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 6: Tone On')
        elif count == ITI_T6_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 6: Shock On')
        elif count == ITI_T6_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 6: Turn off Shock & Tone')
            print('ITI 6: Completed')
        # === #
        elif count == ITI_T7:
            print('ITI 7: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 7: Tone On')
        elif count == ITI_T7_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 7: Shock On')
        elif count == ITI_T7_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 7: Turn off Shock & Tone')
            print('ITI 7: Completed')
        # _____ Third ITI Interval _____ #
        elif count == ITI_T8:
            print('ITI 8: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 8: Tone On')
        elif count == ITI_T8_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 8: Shock On')
        elif count == ITI_T8_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 8: Turn off Shock & Tone')
            print('ITI 8: Completed')
        # === #
        elif count == ITI_T9:
            print('ITI 9: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 9: Tone On')
        elif count == ITI_T9_28:
            p_Rig.o_Shock.turnOn()
            print('ITI 9: Shock On')
        elif count == ITI_T9_30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 9: Turn off Shock & Tone')
            print('ITI 9: Completed')
            print ("ITI Intervaling is done")

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: Light is On')
        p_Rig.o_L_Lever_Extension.turnOn() # Turns on left lever
        print('Pretrial: Lever is Out')
        p_State.switch(VI1_Timer) # Switches to Trial class

# =================+++++++================= #

class VI1_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(1) # First random ~30 sec timer
        p_Timer.VI_T.setRepeats(float_1)
        p_Timer.VI_T.start()
        print('VI 1: Timer Started')
    def s_VI_T_tick(count):
        if count == float_1:
            p_State.switch(VI1_Event)
class VI1_Event:    #StateID = ?
    def s_State_enter():
        print('VI 1: Entering Event')
        p_State.setTimeout(const_CorrectResponse, VI2_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        print('VI 1: Lever was pressed')
        p_State.switch(VI1_Reward)
class VI1_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 1: Sucrose dispensed')
        p_State.switch(VI2_Timer)

class VI2_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(1) # Second random ~30 sec timer
        p_Timer.VI_T.setRepeats(float_2)
        p_Timer.VI_T.start()
        print('VI 2: Timer Started')
    def s_VI_T_tick(count):
        if count == float_2:
            p_State.switch(VI2_Event)
class VI2_Event:    #StateID = ?
    def s_State_enter():
        print('VI 2: Entering Event')
        p_State.setTimeout(const_CorrectResponse, VI3_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI2_Reward)
        print('VI 2: Lever was pressed')
class VI2_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 2: Sucrose dispensed')
        p_State.switch(VI3_Timer)

class VI3_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(1) # Third random ~30 sec timer
        p_Timer.VI_T.setRepeats(float_3)
        p_Timer.VI_T.start()
        print('VI 3: Timer Started')
    def s_VI_T_tick(count):
        if count == float_3:
            p_State.switch(VI3_Event)
class VI3_Event:    #StateID = ?
    def s_State_enter():
        print('VI 3: Entering Event')
        p_State.setTimeout(const_CorrectResponse, VI1_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI3_Reward)
        print('VI 3: Lever was pressed')
class VI3_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        time.sleep(1)
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 3: Sucrose dispensed')
        p_State.switch(VI1_Timer)







# = #
