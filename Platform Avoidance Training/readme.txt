Quick Run Down on how to use:


+==============================+
SCRIPTS

There are two important scripts in this folder and choose one of the two"
  platform_avoidance_training_pynapse.py = more pynapse runtime oriented
  platform_avoidance_training_canonical.py = uses more complicated python functionalities
The rest you may ignore

+==============================+
DECLARING PRESETS

Naming matters as well as presetting certain things in Pynapse+Synapse. t
Therefore the following attributes needs to be declared in the Synapse program:

  Regarding Timers:
    Global_Timer
    VI_Timer
    ITI_Timer

  Regarding inputs and outputs: (Variable names must be exact and case sensitive)
      For iH10_1 Controller:
          Channel 1 = output_Left_Lever_Extension
          Channel 2 = input_Left_Lever_Press
          Channel 3 = output_Left_Lever_Light
          Channel 4 = output_Reward_Receptacle_Light
          Channel 5 = output_House_Light
          Channel 6 = output_Tone
          Channel 7 = input_Reward_Receptacle_Beam_Break
          Channel 9 = output_Pellet_Dispenser
          Channel 10 = output_Shock
      For iH10_2 Controller:
          Channel 1 = output_Right_Lever_Extension
          Channel 2 = input_Right_Lever_Press
          Channel 3 = output_Right_Lever_Light

+==============================+
DEBUGGING AND SAMPLE CODE:

-___________-
Check if each timer works (5 seconds):

class Test:   #StateID = 0
    def s_Mode_standby():
        p_Timer.INSERTTIMERNAME.setPeriod(5)
        p_Timer.INSERTTIMERNAME.setRepeats(1)
    def s_Mode_recprev():
        p_Timer.INSERTTIMERNAME.turnOn()
    def s_INSERTTIMERNAME_tick(count):
        print('done')
        syn.setModeStr('Idle')
-___________-
