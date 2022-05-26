# Pynapse Source #
# V 4

import numpy as np

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#
#
# ==++== PRETEXT ==++==
#   Naming matters as well as presetting certain things in Pynapse+Synapse (EVERYTHING IS CASE SENSITIVE)
#   Therefore the following attributes needs to be declared in the Synapse program:
#
# ==++== TIMERS ==++==
# NOTE:
#    Timers can only be 8 Characters max and have only a 1000 sec maximum interval, therefore, the 1000 sec timer is repeated 3 times followed by a 600 sec timer
#    Fill timers into timer slot in synapse; Enable Epoch Store
# Timer Variables:
#    GlobA_T = Global 1000 sec Timer
#    GlobB_T = Global 600 sec Timer = GlobB_T
#    VI_T = Timer for VI intervaling
#    ITI_T = ITI Timer for ITI intervaling
#
# ==++== Channels ==++==
# NOTE: Regarding inputs and outputs
#    Variable names must be exact and case sensitive as well as (3-20 Characters):\\
#    Variable name nomenclature: o/i_L/R_NAME
#    o/i for output/input, L/R for Left/Right
# Channel Assignments:
#      For iH10_1 Controller:
#          Channel 1 = o_L_Lever_Extension
#          Channel 2 = i_L_Lever_Press
#          Channel 3 = o_L_Lever_Light
#          Channel 4 = o_Rew_Recep_Light
#          Channel 5 = o_House_Light
#          Channel 6 = o_Tone
#          Channel 7 = i_Rew_Recep_Beam_Brk
#          Channel 9 = o_Pellet_Dispenser
#          Channel 10 = o_Shock
#      For iH10_2 Controller:
#          Channel 1 = o_R_Lever_Extension
#          Channel 2 = i_R_Lever_Press
#          Channel 3 = o_R_Lever_Light


# Global Variables:
const_VISchedule = 30           # Variable interval schedule with mean interval (in sec)
const_CorrectResponse = 3       # Right lever press timeout threshold window following the end of the VI timer (in sec)
const_ITI = 180                 # Mean InterTrial Interval (ITI) (in sec)

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
ITI_T2 = ITI_T1 + ITI_Float_2 + 30
ITI_T3 = ITI_T2 + ITI_Float_3 + 30
ITI_T4 = ITI_T3 + ITI_Float_4 + 300 + 30
ITI_T5 = ITI_T4 + ITI_Float_5 + 30
ITI_T6 = ITI_T5 + ITI_Float_6 + 30
ITI_T7 = ITI_T6 + ITI_Float_7 + 300 + 30
ITI_T8 = ITI_T7 + ITI_Float_8 + 30
ITI_T9 = ITI_T8 + ITI_Float_9 + 30

# Displays Set Variables and Presets
print( "EXPERIMENTAL PRESETS:", '\n', '\n',
"const_VISchedule =", const_VISchedule, '\n',
"const_CorrectResponse =", const_CorrectResponse, '\n',
"const_ITI =", const_ITI, '\n', '\n', '\n',
"The numbers generated for VI are ", float_1, " ", float_2, " ", float_3, " seconds", '\n', '\n',
"The numbers chosen are ", ITI_Float_1, ITI_Float_2, ITI_Float_3, ITI_Float_4, ITI_Float_5, ITI_Float_6, ITI_Float_7, ITI_Float_8, ITI_Float_9, "seconds"'\n', '\n'
)

#==========================================================#
#                   Actual Program                         #
#==========================================================#
# Always class: Special class for Pynapse where conditionals here is always being checked


class Always:   #StateID = 0
    def s_Mode_standby():
        print('Setting up Global & ITI Timers')
        p_Timer.GlobA_T.setPeriod(1000) # Length (sec)
        p_Timer.GlobA_T.setRepeats(3) # Frequency
        p_Timer.ITI_T.setPeriod(1000) # Length (sec)
        p_Timer.ITI_T.setRepeats(4) # Frequency
    def s_Mode_recprev():
        print('Starting the global experimental 3000 sec timer')
        p_Timer.GlobA_T.turnOn() # Turn on timer
        print('Starting the 4000 sec ITI timer', '\n', 'NOTE: Experiment will finish before ITI timer completes')
        p_Timer.ITI_T.turnOn() # Turn on timer
    def s_GlobA_T_tick(count):
        if s_GlobA_T_tick(count) == 3000:
            print('3000 sec timer completed', '\n', 'Starting the last global experimental 600 sec timer')
            p_Timer.GlobB_T.setPeriod(600) # Length (sec)
            p_Timer.GlobB_T.setRepeats(1) # Frequency
            p_Timer.GlobB_T.turnOn() # Turn on timer
    def s_GlobB_T_tick(count):
        if s_GlobB_T_tick(count) == 600:
            print('600 sec timer complete', '\n', '60 min has passed and experiment is completed')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)
        # ===== Conditional Based ITI Scheduling ===== #
        # _____ First ITI Interval _____ #
    def s_ITI_T_tick(count):
        if s_ITI_T_tick(count) == ITI_T1:
            print('ITI 1: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 1: Tone On')
        if s_ITI_T_tick(count) == ITI_T1 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 1: Shock On')
        if s_ITI_T_tick(count) == ITI_T1 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 1: Turn off Shock & Tone')
            print('ITI 1: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T2:
            print('ITI 2: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 2: Tone On')
        if s_ITI_T_tick(count) == ITI_T2 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 2: Shock On')
        if s_ITI_T_tick(count) == ITI_T2 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 2: Turn off Shock & Tone')
            print('ITI 2: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T3:
            print('ITI 3: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 3: Tone On')
        if s_ITI_T_tick(count) == ITI_T3 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 3: Shock On')
        if s_ITI_T_tick(count) == ITI_T3 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 3: Turn off Shock & Tone')
            print('ITI 3: Completed')
        # _____ Second ITI Interval _____ #
        if s_ITI_T_tick(count) == ITI_T4:
            print('ITI 4: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 4: Tone On')
        if s_ITI_T_tick(count) == ITI_T4 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 4: Shock On')
        if s_ITI_T_tick(count) == ITI_T4 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 4: Turn off Shock & Tone')
            print('ITI 4: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T5:
            print('ITI 5: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 5: Tone On')
        if s_ITI_T_tick(count) == ITI_T5 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 5: Shock On')
        if s_ITI_T_tick(count) == ITI_T5 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 5: Turn off Shock & Tone')
            print('ITI 5: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T6:
            print('ITI 6: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 6: Tone On')
        if s_ITI_T_tick(count) == ITI_T6 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 6: Shock On')
        if s_ITI_T_tick(count) == ITI_T6 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 6: Turn off Shock & Tone')
            print('ITI 6: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T7:
            print('ITI 7: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 7: Tone On')
        if s_ITI_T_tick(count) == ITI_T7 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 7: Shock On')
        if s_ITI_T_tick(count) == ITI_T7 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 7: Turn off Shock & Tone')
            print('ITI 7: Completed')
        # _____ Third ITI Interval _____ #
        if s_ITI_T_tick(count) == ITI_T8:
            print('ITI 8: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 8: Tone On')
        if s_ITI_T_tick(count) == ITI_T8 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 8: Shock On')
        if s_ITI_T_tick(count) == ITI_T8 + 30:
            p_Rig.o_Tone.turnOff()
            p_Rig.o_Shock.turnOff()
            print('ITI 8: Turn off Shock & Tone')
            print('ITI 8: Completed')
        # === #
        if s_ITI_T_tick(count) == ITI_T9:
            print('ITI 9: Started')
            p_Rig.o_Tone.turnOn()
            print('ITI 9: Tone On')
        if s_ITI_T_tick(count) == ITI_T9 + 28:
            p_Rig.o_Shock.turnOn()
            print('ITI 9: Shock On')
        if s_ITI_T_tick(count) == ITI_T9 + 30:
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
        p_Timer.VI_T.turnOff()
        p_Timer.VI_T.setPeriod(float_1) # First random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
        p_Timer.VI_T.turnOn()
        print('VI 1: Started')
    def s_VI_T_tick(count):
        if s_VI_T_tick(count) == float_1:
            p_State.switch(VI1_Event)
class VI1_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimeout(const_CorrectResponse, VI2_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        print('VI 1: Lever was pressed')
        p_State.switch(VI1_Reward)
class VI1_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 1: Sucrose dispensed')
        p_State.switch(VI2_Timer)

class VI2_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.turnOff()
        p_Timer.VI_T.setPeriod(float_2) # Second random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
        p_Timer.VI_T.turnOn()
        print('VI 2: Started')
    def s_VI_T_tick(count):
        if s_VI_T_tick(count) == float_2:
            p_State.switch(VI2_Event)
class VI2_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimeout(const_CorrectResponse, VI3_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI2_Reward)
        print('VI 2: Lever was pressed')
class VI2_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 2: Sucrose dispensed')
        p_State.switch(VI3_Timer)

class VI3_Timer:    #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.turnOff()
        p_Timer.VI_T.setPeriod(float_3) # Third random ~30 sec timer
        p_Timer.VI_T.setRepeats(1)
        p_Timer.VI_T.turnOn()
        print('VI 3: Started')
    def s_VI_T_tick(count):
        if s_VI_T_tick(count) == float_3:
            p_State.switch(VI3_Event)
class VI3_Event:    #StateID = ?
    def s_State_enter():
        p_State.setTimeout(const_CorrectResponse, VI1_Timer) # Window Time aka Threshold, Goto Class
    def s_i_L_Lever_Press_rise():
        p_State.switch(VI3_Reward)
        print('VI 3: Lever was pressed')
class VI3_Reward:   #StateID = ?
    def s_State_enter():
        p_Rig.o_Pellet_Dispenser.turnOn() # Gives sucrose as reward
        p_Rig.o_Pellet_Dispenser.turnOff()
        print('VI 3: Sucrose dispensed')
        p_State.switch(VI1_Timer)







# = #
