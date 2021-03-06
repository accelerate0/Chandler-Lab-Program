# Pynapse Source #

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#

# Global Static Variables:
const_Trial_T1 = 300                # Setting of first trial timer (sec) (5 min = 300 sec)
const_Trial_T2 = 120                # Setting of second trial timer (sec) (2 min = 120 sec)
const_Trial_Amount = 1              # Amount of Trials
const_Latency = 30                  # Set the latency (sec) between on/off for tone, light blinking, etc
const_Options = 1                   # Set the program option
                                    # 1 = Lever Light Blink
                                    # 2 = Tone
const_Options_LR = 1 # Set Left or Right lever light blink
# 1 = left
# 2 = right


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
        "const_Options_LR =", const_Options_LR, '\n',
        '\n')
        # Switching to PreTrial Class
        p_State.switch(PreTrial)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn() # Turns on light
        print('Pretrial: House Light is On')
        p_State.switch(Trial_Timer_1) # Switches to Trial class

# =================+++++++================= #

class Trial_Timer_1:      #StateID = ?
    def s_State_enter():
        global Trial_Ticker
        Trial_Ticker = Trial_Ticker + 1
        if Trial_Ticker <= const_Trial_Amount:
            p_Timer.Trial_T.setPeriod(1)
            p_Timer.Trial_T.setRepeats(const_Trial_T1)
            p_Timer.Trial_T.start()
            print('Trial ', Trial_Ticker,' Timer: Trial 1 Timer On')
        else:
            p_State.switch(Finish)
    def s_Trial_T_tick(count):
        if count == const_Trial_T1:
            print('Trial ', Trial_Ticker,' Timer: Trial 1 Timer Finished')
            p_State.switch(Trial_Event)

class Trial_Event:      #StateID = ?
    def s_State_enter():
        p_Timer.Trial_T.setPeriod(1)
        p_Timer.Trial_T.setRepeats(const_Latency)
        if const_Options == 1:
            p_Timer.Trial_T.start()
            if const_Options_LR == 1:
                p_Rig.o_L_Lever_Light.turnOn()
                print('Trial ', Trial_Ticker,' Event: Left Lever Light On')
            if const_Options_LR == 2:
                p_Rig.o_R_Lever_Light.turnOn()
                print('Trial ', Trial_Ticker,' Event: Right Lever Light On')
        elif const_Options == 2:
            p_Timer.Trial_T.start()
            p_Rig.o_Tone.turnOn()
            print('Trial ', Trial_Ticker,' Event: Tone On')
    def s_Trial_T_tick(count):
        if count == const_Latency:
            if const_Options == 1:
                if const_Options_LR == 1:
                    p_Rig.o_L_Lever_Light.turnOff()
                    print('Trial ', Trial_Ticker,' Event: Left Lever Light Off')
                if const_Options_LR == 2:
                    p_Rig.o_R_Lever_Light.turnOff()
                    print('Trial ', Trial_Ticker,' Event: Right Lever Light Off')
            elif const_Options == 2:
                p_Rig.o_Tone.turnOff()
                print('Trial ', Trial_Ticker,' Event: Tone Off')
            print('Trial ', Trial_Ticker,' Event:', const_Latency, 'sec Trial Timer Finished')
            p_State.switch(Trial_Timer_2)

class Trial_Timer_2:      #StateID = ?
    def s_State_enter():
        p_Timer.Trial_T.setPeriod(1)
        p_Timer.Trial_T.setRepeats(const_Trial_T2)
        p_Timer.Trial_T.start()
        print('Trial ', Trial_Ticker,' Event: Trial 2 Timer On')
    def s_Trial_T_tick(count):
        if count == const_Trial_T2:
            print('Trial ', Trial_Ticker,' Event: Trial 2 Timer Finished')
            p_State.switch(Trial_Timer_1)

# =================+++++++================= #

class Finish:      #StateID = ?
    def s_State_enter():
        print('Trial Finish: Shutting down')
        syn.setModeStr('Idle')

# = #
