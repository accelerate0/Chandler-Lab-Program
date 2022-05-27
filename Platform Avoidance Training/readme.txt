READ BEFORE CONTINUING:

  ==++== PRETEXT ==++==
    Naming matters as well as presetting certain things in Pynapse+Synapse
    Everything in Pynapse is case-sensitive
    Never use spaces or non-alphanumeric characters, always use underscore (_) to denote spaces
    
  ==++== TIMERS ==++==
  Fill timers into timer slot in synapse; Enable Epoch Store
  Timer Variables:
     Global_T = Global Experimental sec Timer defined by const_ExperimentTime
     VI_T = Timer for VI intervaling
 
  ==++== Channels ==++==
  NOTE: Regarding inputs and outputs
     Variable names must be exact and case sensitive as well as (3-20 Characters):\\
     Variable name nomenclature: o/i_L/R_NAME
     o/i for output/input, L/R for Left/Right
  Channel Assignments:
       For iH10_1 Controller:
           Channel 1 = o_L_Lever_Extension
           Channel 2 = i_L_Lever_Press
           Channel 3 = o_L_Lever_Light
           Channel 4 = o_Rew_Recep_Light
           Channel 5 = o_House_Light
           Channel 6 = o_Tone
           Channel 7 = i_Rew_Recep_Beam_Brk
           Channel 9 = o_Pellet_Dispenser
           Channel 10 = o_Shock
       For iH10_2 Controller:
           Channel 1 = o_R_Lever_Extension
           Channel 2 = i_R_Lever_Press
           Channel 3 = o_R_Lever_Light
