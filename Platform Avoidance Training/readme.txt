Quick Run Down on how to use:

+==============================+
SCRIPTS

There are two important scripts in this folder and choose one of the two"
  platform_avoidance_training_pynapse.py = more pynapse runtime oriented
  platform_avoidance_training_canonical.py = uses more complicated python functionalities
The rest you may ignore

+==============================+
TIMER PRESET IN iCON

Naming matters as well as presetting certain things in Pynapse+Synapse.
Therefore the following attributes needs to be declared in the Synapse program itself:
  Regarding Timers:
    Timer iCon Settings:
      General Options:
        Name: Global_Timer OR VI_T
        Epoc Save: checked
        ID: GloT
      Shape:
        Control: Trigger
        Period 1.000 seconds
        Repeats: 3600
        Early Pulse: Not checked
        Sync: Not checked
    Timer Function:
      VI_Timer: Timer variable responsible for VI Scheduling, defined by 3 randomly generated numbers
      Global_T: The global timer responsible for timing the entire experiment as well as the ITI portion

+==============================+
CHANNEL INPUT/OUTPUT PRESET IN iCON

  Regarding inputs and outputs: (Variable names must be exact and case sensitive)
      Format is:
          Controller
              Channel Assignment = Variable Name = Epoc Store ID

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

      Regarding Input/Output Logic Settings:
          Hal Input Port: Not checked
          Triggered Pulse: Not checked
          Sync: Not checked
          Invert Output: Not checked
          Epoc Store: Enabled
          Fill in the Epoch ID to the respected assignment
