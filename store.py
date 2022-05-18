# Reference Table, Will Either Delete Soon or Use to Integrate Pynapse Settings
def Channel()
    class iH10_1:
        output_Left_Lever_Extension = Channel.1a
        input_Left_Lever_Press = Channel.2a
        output_Left_Lever_Light	= Channel.3a
        output_Reward_Receptacle_Light = Channel.4a
        output_House_Light = Channel.5a
        output_Tone = Channel.6a
        input_Reward_Receptacle_Beam_Break = Channel.7a
        output_Pellet dispenser = Channel.9a
        output_Shock = Channel.10a
    class iH10_2:
        output_Right_Lever_Extension = Channel.1b
        input_Right_Lever_Press = Channel.2b
        output_Right_Lever_Light = Channel.3b






#==========================================================#
#             Array Handling (Needs Major Work)            #
#==========================================================#

class DIM:
    def __init__(DIM_A):
        DIM_A.0 = Lever Presses
        DIM_A.1 = Pellets delivered
        DIM_A.2 = Magazine Entries
        DIM_A.3 = Tone counter
        DIM_A.4 = InterBlock Interval counter
        DIM_A.5 = Shock counter
        DIM_A.data_zarray = numpy.zeros(DIM_A.1, DIM_A.2, DIM_A.3, DIM_A.4, DIM_A.5, DIM_A.6)
    DIM.B = 1
    DIM.C = 1
    DIM.D = 5000 # ARRAY OF TIMESTAMPS FOR PELLET DELIVERIES
    DIM.E = 5000 # ARRAY OF TIMESTAMPS FOR LEVER PRESSES
    DIM.F = 5000 # ARRAY OF TIMESTAMPS FOR PORT ENTRIES
    DIM.G = 5000 # ARRAY OF TIMESTAMPS FOR TONE ONSET
    DIM.H = 5000 # ARRAY OF TIMESTAMPS FOR SHOCK ONSET
    DIM.J = 5000 # ARRAY OF TIMESTAMPS FOR INTER BLOCK INTERVAL ONSET
    def __init__(DIM_X): # SESSION VARIABLES
        DIM_X.1 = VI Schedule timer
        DIM_X.2 = Session timer
        DIM_X.3 = ITI timer
class VI_OPTION_LIST:
    def __init__(y):
        y.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def __init(ITI_OPTION_LIST) # This list of options will be initialized into a ITI timer
        ITI_OPTION_LIST.LIST_I = [1, 2, 3, 4, 5]
class DISK:
    def __init__(VARS, A, C, D, E, F, G, H, J, X, Y, I)
    def __init__(DISKOPTIONS, FULLHEADERS)





# Construction of the Experiment
class Analogue_Output:
    def __init__(RightLever, on, off):
        RightLever.off = 0
        RightLever.on = 1
    def __init__(LightLever, on, off):
        LightLever.off = 0
        LightLever.on = 1
    def __init__(RightLight, on, off):
        RightLight.off = 0
        RightLight.on = 1
    def __init__(HouseLight, on, off):
        HouseLight.off = 0
        HouseLight.on = 1
# Experiment


import time

test = 0
timeout = 5   # [seconds]

timeout_start = time.time()
while time.time() < timeout_start + timeout:
    time.sleep(0.01) # Optimization so it does not hog CPU
    if test == 5:
        break
    test -= 1




# Generates Random Numbers For Random Timer
y_n_2_answer = input("Which Arithmetic Operation Would You Like To Perform [1/2]?" + '\n' + "1 = Floating Point" + '\n' + "2 = Pseudonumeric" + '\n')
if y_n_2_answer == "1": # Floating Point, Quicker
    import numpy as np
    float_1 = np.random.normal(Presets.const_VISchedule,3,1) #average, standard deviation, amount of numbers
    float_2 = np.random.normal(Presets.const_VISchedule,3,1) #average, standard deviation, amount of numbers
    float_3 = np.random.normal(Presets.const_VISchedule,3,1) #average, standard deviation, amount of numbers
    print("The numbers generated are ", float_1, " minutes")
elif y_n_2_answer == "2": # Pseudonumeric Generator
    random_num_rounded = 5 # BS Value
    while (random_num_rounded != Presets.const_VISchedule):
      random_num1 = random.randint(20, 40) # random integer from 20 to 40
      random_num2 = random.randint(10, 50) # random integer from 10 to 50
      random_num3 = random.randint(20, 40) # random integer from 20 to 40
      random_num_total_unrounded = (random_num1 + random_num2 + random_num3)/3
      random_num_rounded = round(random_num_total_unrounded)
      print(random_num_rounded, "was attempted as an average")
    else:
      print("The time set is", " ", random_num1, " ", random_num2, " ", random_num3, "(in seconds)")
else:
    print("Please enter 1 or 2")
