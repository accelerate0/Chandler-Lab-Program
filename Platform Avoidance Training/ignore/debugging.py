class Always:       #StateID = ?
    def s_Mode_standby():
        p_Timer.Global_T.setPeriod(5) # Length (sec)
        p_Timer.Global_T.setRepeats(1) # Frequency
    def s_Mode_recprev():
        p_Timer.Global_T.turnOn() # Turn on timer
        p_State_switch(Test2)
    def s_Global_T_tick(count):
        print('5 sec timer finished')
        print('The Experiment is Complete')
        p_Rig.o_R_Lever_Extension.turnOn()

class Test1:     #StateID = ?
    def s_State_enter():
        p_Rig.o_R_Lever_Light.turnOn() # Turns on light
        print('Right Lever Light is On')
        p_State_switch(Test3)

class Test2:     #StateID = ?
    def s_State_enter():
        p_Rig.o_L_Lever_Light.turnOn() # Turns on left lever
        print('Left Lever Light is On')

class Test3:     #StateID = ?
    def s_State_enter():
        p_Rig.o_L_Lever_Extension.turnOn()
        print('left lever extended')
        print('all is done')
