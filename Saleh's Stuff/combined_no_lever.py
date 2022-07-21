# Pynapse Source #

import time
import pyopcond_dep as pyop

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_Trial_T1 = 300                # Setting of first trial timer (sec) (5 min = 300 sec)
const_Trial_T2 = 120                # Setting of second trial timer (sec) (2 min = 120 sec)
const_Trial_Amount = 1              # Amount of Trials
const_Latency = 30                  # Set the latency (sec) between on/off for tone, light blinking, etc
const_Options = 1                   # Set the program option
                                    # 1 = Right Lever Light Blink
                                    # 2 = Tone

# =================+++++++================= #
# ! DO NOT CHANGE ANYTHING HERE !

# Global Dynamic Variables:
Trial_Ticker = 0                     # Tracks amount of Trials has looped


#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        # Printing Experimental Constants on console
        print("EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_Trial_T1 (sec) =", const_Trial_T1, '\n',
        "const_Trial_Amount =", const_Trial_Amount, '\n',
        "const_Trial_T2 (sec) =", const_Trial_T2, '\n',
        "const_Latency (sec) =", const_Latency, '\n',
        "const_Options =", const_Options, '\n',
        '\n')
        # Switching to PreTrial Class
        p_State.switch(PreTrial)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_State.switch(Trial_Timer) # Switches to Trial class

# =================+++++++================= #

class Trial_Timer:      #StateID = ?
    def s_State_enter():
        global Trial_Ticker,
        Trial_Ticker = Trial_Ticker + 1
        if Trial_Ticker <= const_Trial_Amount:
            print('Trial ', Trial_Ticker,' Timer: Starting Trial 1 Timer')
            p_Timer.Trial_T.setPeriod(1)
            p_Timer.Trial_T.setRepeats(const_Trial_T1)
            p_Timer.Trial_T.start()
            print('Trial ', Trial_Ticker,' Timer: Trial 1 Timer Finished')
        else:
            p_State.switch(Finish)
    def s_Trial_T_tick(count):
        if count == const_Trial_T1:
            p_State.switch(Trial_Event)

class Trial_Event:      #StateID = ?
    def s_State_enter():
        if const_Options == 1:
            p_Rig.o_R_Lever_Light.turnOn()
            time.sleep(const_Latency)
            p_Rig.o_R_Lever_Light.turnOff()
            print('Trial ', Trial_Ticker,' Event: Blinked Right Lever Light')
        elif const_Options == 2:
            p_Rig.o_Tone.turnOn()
            time.sleep(const_Latency)
            p_Rig.o_Tone.turnOff()
            print('Trial ', Trial_Ticker,' Event: Tone Initiated')
        print('Trial ', Trial_Ticker,' Event: Starting Trial 2 Timer')
        p_Timer.Trial_T.setPeriod(1)
        p_Timer.Trial_T.setRepeats(const_Trial_T2)
        p_Timer.Trial_T.start()
    def s_Trial_T_tick(count):
        if count == const_Trial_T2:
            print('Trial ', Trial_Ticker,' Event: Trial 2 Timer Finished')
            p_State.switch(Trial_Timer)

# =================+++++++================= #

class Finish:      #StateID = ?
    def s_State_enter():
        print('Trial Finish: Shutting down')
        syn.setModeStr('Idle')

# = #
