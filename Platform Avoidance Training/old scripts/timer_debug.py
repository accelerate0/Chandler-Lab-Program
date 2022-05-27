# Pynapse Source #

experiment_time = 30
example_if = 5
example_param = 10
example_VI = 15

class Always:   #StateID = 0
    def s_Mode_recprev():
        p_Timer.Global_T.setPeriod(1)
        p_Timer.Global_T.setRepeats(experiment_time)
        p_Timer.Global_T.start()
    def s_Global_T_tick(count):
        if s_Global_T_tick(count) == 5:
            print('5 sec passed via if conditional statement')
    def s_Global_T_tick(example_param):
        print('10 sec passed via parameter statement')


class Trial:   #StateID = ?
    def s_State_enter():
        p_Timer.VI_T.setPeriod(1)
        p_Timer.VI_T.setRepeats(example_VI)
        p_Timer.VI_T.start()
        print('15 seconds passed')
        p_State.switch(Success)

class Fail:   #StateID = ?
    def s_State_enter():
        print('Script Failed')

class Success:   #StateID = ?
    def s_State_enter():
        print('Script Failed')
