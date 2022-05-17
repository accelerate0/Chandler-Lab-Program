import numpy # For Zero Arrays
import sys # For Program exiting
import random # For random number generator
import time # For timer

#==========================================================#
#             Setting Variables, Constant, Etc
#==========================================================#

class Channel:
    # Channel Inputs
    inpt_RightLever = '1'
    inpt_Magazine = '4'
    # Channel Outputs
    outpt_RightOut = '1'
    outpt_LeverLight = '2'
    outpt_Pellet = '3'
    outpt_Shock = '4'
    outpt_RightLight = '5'
    outpt_Tone = '6'
    outpt_HouseLight = '7'
    outpt_TTLTone = '9'
    outpt_TTLL = '10'

class Presets:
    # Constants
    const_SessionLength = 60 # Length of the entire experiment in minutes
    const_VISchedule = 30 # Variable interval schedule with mean interval of 30sec
    const_CorrectResponse = 3 # Right lever press following the end of the VI timer
    const_ITI = 180 # Mean Intertrial Interval in seconds
    const_Shutdown = 12

#==========================================================#
#                         Arrays
#==========================================================#

# =============NEED TO WORK ON=============== #
# Data - Totals
data_DIM_A = 6
data_DIM_B = 1 \SHOCK ARRAY - ARRAY MUST BE 0x0 so can be used in ZEROARRAY FUNCTION
data_array = ['1', '2', '3', '4', '5', '6']
# How to integrate SHOCK ARRAY aka ARRAY MUST BE 0x0 so can be used in ZEROARRAY FUNCTION
# Zeroarray via numpy aka such as zarray = numpy.zeros(100)
"""
data_A(0) = Lever Presses
data_A(1) = Pellets delivered
data_A(2) = Magazine Entries
data_A(3) = Tone counter
data_A(4) = InterBlock Interval counter
data_A(5) = Shock counter
"""

# ============================ #

# =============NEED TO WORK ON=============== #
#     TIMESTAMPS
DIM_C = 1
DIM_D = 5000 \ ARRAY OF TIMESTAMPS FOR PELLET DELIVERIES
DIM_E = 5000 \ ARRAY OF TIMESTAMPS FOR LEVER PRESSES
DIM F = 5000 \ ARRAY OF TIMESTAMPS FOR PORT ENTRIES
DIM G = 5000 \ ARRAY OF TIMESTAMPS FOR TONE ONSET
DIM H = 5000 \ ARRAY OF TIMESTAMPS FOR SHOCK ONSET
DIM J = 5000 \ ARRAY OF TIMESTAMPS FOR INTER BLOCK INTERVAL ONSET
# =============NEED TO WORK ON=============== #
# SESSION VARIABLES
DIM X = 3
\X(0) = VI Schedule timer
\X(1) = Session timer
\X(2) = ITI timer
# =============NEED TO WORK ON=============== #
#    LISTS
\VI OPTION LIST - This list will be initialized into a VI schedule
LIST Y = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
\ITI OPTION LIST - This list of options will be initialized into a ITI timer
LIST I = 1, 2, 3, 4, 5
# =============NEED TO WORK ON=============== #
#     DATA MANAGEMENT
DISKVARS = A, C, D, E, F, G, H, J, X, Y, I
DISKOPTIONS = FULLHEADERS








#==========================================================#
#                       Actual Program
#==========================================================#


# Displays Set Variables
print( "KEY VARIABLES:", '\n', '\n',

"INPUT CHANNEL SETTINGS:", '\n',
"inpt_RightLever =", Channel.inpt_RightLever, '\n',
"inpt_Magazine =", Channel.inpt_Magazine, '\n', '\n',

"OUTPUT CHANNEL SETTINGS:", '\n',
"outpt_RightOut =", Channel.outpt_RightOut, '\n',
"outpt_LeverLight =", Channel.outpt_LeverLight, '\n',
"outpt_Pellet =", Channel.outpt_Pellet, '\n',
"outpt_Shock =", Channel.outpt_Shock, '\n',
"outpt_RightLight=", Channel.outpt_RightLight, '\n',
"outpt_Tone =", Channel.outpt_Tone, '\n',
"outpt_HouseLight =", Channel.outpt_HouseLight, '\n',
"outpt_TTLTone =", Channel.outpt_TTLTone, '\n',
"outpt_TTLL =", Channel.outpt_TTLL, '\n', '\n',

"EXPERIMENTAL PRESETS:", '\n',
"const_SessionLength =", Presets.const_SessionLength, '\n',
"const_VISchedule =", Presets.const_VISchedule, '\n',
"const_CorrectResponse =", Presets.const_CorrectResponse, '\n',
"const_ITI =", Presets.const_ITI, '\n',
"const_Shutdown =", Presets.const_Shutdown, '\n'
)

# Double Check Measure
y_n_1_answer = input("Would you like to continue [y/n]?" + '\n')
if y_n_1_answer == "y":
    print('Proceeding on!')
elif y_n_1_answer == "n":
    sys.exit()
else:
    print("Please enter y or n")


# Generates Random Numbers For Random Timer
# Variable Interval Schedule (VISchedule) for lever press delivery of sucrose pellets
y_n_2_answer = input("Which Arithmetic Operation Would You Like To Perform [1/2]?" + '\n' + "1 = Floating Point" + '\n' + "2 = Pseudonumeric" + '\n')
if y_n_2_answer == "1": # Floating Point, Quicker
    import numpy as np
    float = np.random.normal(Presets.const_VISchedule,3,3) #average, standard deviation, amount of numbers
    print("The numbers generated are ", float, " minutes")
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
        


    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()
    inpt_RightLever = '1'
    inpt_Magazine = '4'
    outpt_RightOut = '1'
    outpt_LeverLight = '2'
    outpt_Pellet = '3'
    outpt_Shock = '4'

    outpt_Tone = '6'

    outpt_TTLTone = '9'
    outpt_TTLL = '10'
