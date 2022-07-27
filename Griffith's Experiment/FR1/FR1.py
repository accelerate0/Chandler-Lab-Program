# Pynapse Source #

import time

#==========================================================#
#             Setting Variables, Constant, Etc             #
#==========================================================#
# Change stuff here to configure experiment

# =================Experiment Related Variables================= #
const_ExperimentTime = 1800         # Time of Entire Experiment (sec)
const_DispenseTime = 1.665          # Dispense time of the liquid dispenser (sec)
                                    # 1.665 sec = 20 uL approx

# =================Mode Selection================= #
# Experimental Mode Selection:
const_Mode = 1

#____ const_Mode = 1 ___#
# Left Lever out only

#____ const_Mode = 2 ___#
# Right Lever out only

#____ const_Mode = 3 ___#
# Both Lever out, Left Lever active

#____ const_Mode = 4 ___#
# Both Lever out, Right Lever active

#____ const_Mode = 5 ___#
# Both Lever out, all Levers active

#==========================================================#
#                   Actual Program                         #
#==========================================================#

class Always:   #StateID = 0
    def s_Mode_recprev():
        print('Setting up Global Timer ')
        p_Timer.Global_T.setPeriod(1) # Length between ticks (sec)
        p_Timer.Global_T.setRepeats(const_ExperimentTime) # Amount of ticks
        print('Starting the global experimental', const_ExperimentTime,'sec timer')
        p_Timer.Global_T.start() # Turn on timer
        print( "EXPERIMENTAL PRESETS:", '\n', '\n',
        "const_ExperimentTime (sec) =", const_ExperimentTime, '\n',
        "const_DispenseTime (sec) =", const_DispenseTime, '\n',
        "const_Mode =", const_Mode, '\n',
        '\n')
        p_State.switch(PreTrial)
    def s_Global_T_tick(count):
        if count == const_ExperimentTime:
            print(const_ExperimentTime, 'sec has passed and experiment is completed, shutting down')
            syn.setModeStr('Idle') # Shuts down Synapse (based on Synapse API)

# =================+++++++================= #

class PreTrial:    #StateID = ?
    def s_State_enter():
        p_Rig.o_House_Light.turnOn()
        print('Pretrial: House Light is On')
        if const_Mode = 1:
            p_Rig.o_L_Lever_Extension.turnOn()
            print('Pretrial: Left Lever is out (active, no right lever extension)')
        if const_Mode = 2:
            p_Rig.o_R_Lever_Extension.turnOn()
            print('Pretrial: Right Lever is out (active, no left lever extension)')
        if const_Mode = 3:
            p_Rig.o_L_Lever_Extension.turnOn()
            print('Pretrial: Left Lever is out (active)')
            p_Rig.o_R_Lever_Extension.turnOn()
            print('Pretrial: Right Lever is out (inactive)')
        if const_Mode = 4:
            p_Rig.o_L_Lever_Extension.turnOn()
            print('Pretrial: Left Lever is out (inactive)')
            p_Rig.o_R_Lever_Extension.turnOn()
            print('Pretrial: Right Lever is out (active)')
        if const_Mode = 5:
            p_Rig.o_L_Lever_Extension.turnOn()
            print('Pretrial: Left Lever is out (active)')
            p_Rig.o_R_Lever_Extension.turnOn()
            print('Pretrial: Right Lever is out (active)')
        p_State.switch(Trial)

# =================+++++++================= #

class Trial:      #StateID = ?
    def s_State_enter():
        print('Trial: Initiating Trial class')
    def s_i_L_Lever_Press_rise():
        if const_Mode = 1:
            print('Trial: Left Lever pressed, dispensing')
            p_State.switch(Reward)
        if const_Mode = 3:
            print('Trial: Left Lever pressed, dispensing')
            p_State.switch(Reward)
        if const_Mode = 4:
            print('Trial: Left Lever pressed, nothing happens')
        if const_Mode = 5:
            print('Trial: Left Lever pressed, dispensing')
            p_State.switch(Reward)
    def s_i_R_Lever_Press_rise():
        if const_Mode = 2:
            print('Trial: Right Lever pressed, dispensing')
            p_State.switch(Reward)
        if const_Mode = 3:
            print('Trial: Right Lever pressed, nothing happens')
        if const_Mode = 4:
            print('Trial: Right Lever pressed, dispensing')
            p_State.switch(Reward)
        if const_Mode = 5:
            print('Trial: Right Lever pressed, dispensing')
            p_State.switch(Reward)

# =================+++++++================= #

class Reward:      #StateID = ?
    def s_State_enter():
        print('Reward: Initiating Dispense')
        p_Rig.o_Liq_Dispenser.turnOn()
        time.sleep(const_DispenseTime)
        p_Rig.o_Liq_Dispenser.turnOff()
        print('Reward: Dispended at', const_DispenseTime, 'sec, switching back to Trial class')
        p_State.switch(Trial)

# = #
