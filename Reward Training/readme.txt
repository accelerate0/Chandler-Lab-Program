This script has been tested and found to be working

READ BEFORE CONTINUING:

==++== PRETEXT ==++==

    Naming matters as well as presetting certain things in Pynapse+Synapse
    Everything in Pynapse is case-sensitive
    Never use spaces or non-alphanumeric characters, always use underscore (_) to denote spaces


==++== TIMERS ==++==

  Fill timers into timer slot in the Synapse software
  Naming matters as well as presetting certain things in Pynapse+Synapse.
  Therefore the following attributes needs to be declared in the Synapse program itself:

      Timer iCon Settings:
        General Options:
            Name: Global_T
            Epoc Save: checked
            ID: GloT
        Shape:
            Control: Trigger
            Period 1.000 seconds
            Repeats: 1
                NOTE: This setting does not matter as it will be changed in the script
            Early Pulse: Not checked
            Sync: Not checked

      Timer Functions:
          Global_T: The global timer responsible for timing the entire experiment as well as the ITI portion, defined by const_ExperimentTime


==++== CHANNEL INPUT/OUTPUT ==++==

  NOTE: Regarding inputs and outputs
     Variable names must be exact and case sensitive as well as (3-20 Characters):
     Variable name nomenclature: o/i_L/R_NAME
     o/i for output/input, L/R for Left/Right

  Format is:
     Controller
         Channel Assignment = Variable Name = Epoc Store ID

         For iH10_1 Controller:
             Channel 1 = o_L_Lever_Extension
             Channel 2 = i_L_Lever_Press
             Channel 3 = o_L_Lever_Light
             Channel 4 = o_Reward_R_Light
             Channel 5 = o_House_Light
             Channel 6 = o_Tone
             Channel 7 = i_Reward_R_B_B
             Channel 9 = o_Pellet_Dispenser
             Channel 10 = o_Shock
         For iH10_2 Controller:
             Channel 1 = o_R_Lever_Extension
             Channel 2 = i_R_Lever_Press
             Channel 3 = o_R_Lever_Light

     Regarding Input/Output Logic Settings:
         Hal Input Port: Not checked
         Triggered Pulse: Not checked
         Sync: Not checked
         Invert Output: Not checked
         Epoc Store: Enabled
         Fill in the Epoch ID to the respected assignment



==++== CHANNEL INPUT/OUTPUT ==++==

  NOTE: There are 2 main global variables

         const_ITI = 180                 Mean InterTrial Interval (ITI) (in sec)
         const_ExperimentTime = 3600     Time of Entire Experiment (in sec)


==++== PYNAPSE ==++==

Steps to integrate code into Pynapse
    1) Open "confliction_training.py" in GitHub
    2) Click "Raw" button which is on the top right of the code display box
        Alternatively use this link:
        https://raw.githubusercontent.com/accelerate0/Chandler-Lab-Program/main/Reward%20Training/reward_training.py
    3) Copy and Paste the code into Pynapse
    4) Click Commit, make sure no error messages are displayed and the file has been loaded successfully
